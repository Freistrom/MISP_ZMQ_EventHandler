import yaml
import pdb


class Config:

    DEFAULT_CONFIG_PATH = '/etc/misp_eventhandler/config.yml'

    def __init__(self, params):
        config_path = params.config_path or DEFAULT_CONFIG_PATH
        with open(params.config_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            for key,value in cfg.items():
                self._parse_section(key,value)

    def _parse_section(self, key, value):
        if type(value) == dict:
            for subkey,subvalue in value.items():
                self._parse_section(key+"_"+subkey, subvalue)
        else:
            setattr(self, key, value)


    def add_config(self, config_path):
        with open(config_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            for key,value in cfg.items():
                self._parse_section(key,value)



