import logging
import sys
import os

class MEHLogger(logging.Logger):

    LOG_FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    def __init__(self, config):
      if not os.path.exists(os.path.dirname(config.log_file)):
         os.makedirs(os.path.dirname(config.log_file))

      logging.Logger.__init__(self, 'misp_eventhandler')
      self.formatter = logging.Formatter(self.LOG_FORMATTER)
      self.setLevel(logging.INFO)
      self.propagate = False
      handler = logging.FileHandler(config.log_file)
      handler.setFormatter(self.formatter)
      self.addHandler(handler)
