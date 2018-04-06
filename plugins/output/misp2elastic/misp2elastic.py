from elasticsearch import Elasticsearch
from plugins.plugin import Plugin


class Misp2Elastic(Plugin):

    def __init__(self):
        try:
          self.es = Elasticsearch([{'host': 'localhost'}])
        except:
            print('error')
    def load(self, json):
        pass

    def exec(self, msg):
        try:
            self.es.create(index='misp_events', id=msg.id, doc_type=msg.__class__.__name__, body=msg.to_json())
        except:
            raise Exception('ERROR')
        return True

    def before_hook(self, json):
        pass

    def after_hook(self, json):
        pass

