import time
import json
import syslog
import threading
import models


class EventHandler():

    def __init__(self, plugin_provider, logger):
        self.cond = threading.Condition()
        self.logger = logger
        self.plugin_provider = plugin_provider
        self.logger.info("Initialize EventHandler")

    def process(self, msg):
        self.logger.info('Start processing MISP-Event')
        self._parse_msg(msg)
        try:
            for plugin in self.plugin_provider.plugins:
                self.logger.info("Run Plugin %s for Message type %s" % (plugin.__class__.__name__, self.type))
                plugin.run(self._msg_model())
        except:
            raise Exception("Error during MISP-Event processing!")

        self.logger.info("MISP-Channel: {}".format(self.channel))
        self.logger.info("MSG-Type: {}".format(self.type))
        self.logger.info('MISP Message Processing done')

    def _parse_msg(self, msg):
        try:
            parts = msg.decode('utf-8').split(maxsplit=1)
            self.msg = json.loads(parts[1])
            self.channel = parts[0]
            self.type = list(self.msg.keys())[0]
        except:
            raise Exception("Error during MISP-Message parsing!")

    def _msg_model(self):
        class_name = self.type.capitalize()
        return getattr(models, class_name).from_json(self.msg)
