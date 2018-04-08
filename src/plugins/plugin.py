from abc import ABC, abstractmethod
from inflection import camelize
from config import Config

CONFIG_SEARCH_PATH = '/var/lib/misp_eventhandler/plugins/'

class Plugin(ABC):


    def __init__(self, logger):
        self.logger = logger
        self._load_plugin_config()
        super().__init__()

    @abstractmethod
    def run(self, msg_model):
        pass

    @abstractmethod
    def before_hook(self):
        pass

    @abstractmethod
    def after_hook(self):
        pass

    def _load_plugin_config(self):
        self.logger.info(self.__class__.__name__)
        config_path = CONFIG_SEARCH_PATH
        config_path += self.__class__.__name__.lower()
        config_path += "/config.yml"
        self.config = Config(path = config_path)
