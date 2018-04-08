from plugins.plugin import Plugin

class Default(Plugin):

    def run(self, msg_model):
        self.logger.info(msg_model.to_json())
