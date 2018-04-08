from abc import ABC, abstractmethod
from inflection import camelize


class Plugin(ABC):

    CONFIG_SEARCH_PATH = '/var/lib/misp_eventhandler/plugins/'

    def __init__(self, logger):
        self.logger = logger
        self._load_plugin_config()
        super().__init__()

    @abstractmethod
    def run(self, msg_model):
        pass

    def _load_plugin_config(self):
        pass
        #try:
        #    config.add_config("/var/lib/misp_eventhandler/plugins/%s/config.yml" % plugin_name)
        #except ConfigNotFoundError as e:
        #    self.logger.warning("No config file found for plugin %s!" % plugin_name)
        #    self.logger.warning("Expected config file: /var/lib/misp_eventhandler/plugins/%s/config.yml" % plugin_name)
