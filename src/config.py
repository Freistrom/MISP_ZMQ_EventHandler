import yaml
import pdb

DEFAULT_CONFIG_PATH = '/etc/misp_eventhandler/config.yml'


class Config:

    def __init__(self, path=None, params=None):
        if path:
            config_path = path
        elif params:
            config_path = params.config_path or DEFAULT_CONFIG_PATH

        self._load_from_file(config_path)

    def _parse_section(self, key, value):
        if type(value) == dict:
            for subkey,subvalue in value.items():
                self._parse_section(key+"_"+subkey, subvalue)
        else:
            setattr(self, key, value)

    def _load_from_file(self, config_path):
        with open(config_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            for key,value in cfg.items():
                self._parse_section(key,value)



