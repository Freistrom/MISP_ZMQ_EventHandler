import time
import json
import models
import syslog


class EventHandler():

    def __init__(self, msg):
        try:
            print("Initializing MISP-Message...")
            parts = msg.decode('utf-8').split(maxsplit=1)
            self.msg = json.loads(parts[1])
            self.channel = parts[0]
            self.type = list(self.msg.keys())[0]
            print("MISP-Channel: {}".format(self.channel))
            print("MSG-Type: {}".format(self.type))
            print("Initializing MISP-Message done.")
            self.process()
        except Exception as e:
            print("Error during MISP-Event initializing!")
            print(e)

    def process(self):
        try:
            print('--- Start processing MISP-Event')
            model = globals['models.{}',format(self.type)]
            status = models.Status.from_json(self, self.msg)
            print("Status: {}".format(status.status))
            print("Timestamp: {}".format(status.uptime))
            print('--- Processing done.\n')
        except:
            raise Exception("Error during MISP-Event processing!")
