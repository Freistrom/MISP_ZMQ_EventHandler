import logging
import sys
import pdb
import importlib
from inflection import camelize

from errors.config_not_found_error import ConfigNotFoundError


class PluginProvider(object):

    def __init__(self, config, logger):
        logger.info("Load Plugins...")
        self.logger = logger
        self.plugins = []
        if not hasattr(config, 'plugins') or len(config.plugins) == 0:
            self._load_default_plugin()
        else:
            for plugin_name in config.plugins:
                self._load_plugin(plugin_name)

    def _get_class_name(self, plugin_name):
        return camelize(plugin_name)

    def _load_plugin(self, plugin_name):
        module = importlib.import_module("plugins.%s.%s" % (plugin_name, plugin_name))
        self.plugins.append(getattr(module, self._get_class_name(plugin_name))(self.logger))
        self.logger.info("Plugin %s initialized", plugin_name)

    def _load_default_plugin(self):
        self.logger.warn('No Plugins enabled! Load default plugin.')
        module = importlib.import_module("plugins.default.default")
        self.plugins.append(module.Default(self.logger))

