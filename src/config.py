import yaml


class Config:
  
    def __init__(self, params):
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


    def add_config(self, cfg):
        for key,value in cfg.items():
            self._parse_section(key,value)



