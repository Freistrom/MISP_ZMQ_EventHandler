import zmq
import syslog
import os
import io
import argparse
import pdb
import multiprocessing as mp
from multiprocessing import Queue
from multiprocessing import Process, Pool
from event_handler import EventHandler

from config import Config
from logger import MEHLogger
from plugin_provider import PluginProvider


class Main(object):

    def __init__(self, params):
        self.ctx = zmq.Context()
        self.pool = Pool(processes=mp.cpu_count())
        self.config = Config(params)
        self.logger = MEHLogger(self.config)
        self.plugin_provider = PluginProvider(self.config, self.logger)
        self.event_handler = EventHandler(self.plugin_provider, self.logger)

    def start(self):
        self.logger.info('Connecting to MISP-ZMQ Server at %s:%s' % (self.config.misp_host, self.config.misp_port))
        s = self.ctx.socket(zmq.SUB)
        s.connect('tcp://%s:%s' % (self.config.misp_host, self.config.misp_port))
        s.setsockopt(zmq.SUBSCRIBE, b'')
        self.logger.info('MISP-Server connection established.')
        self.logger.info('Subscribed and listening for MISP-Messages...')
        while True:
           msg = s.recv_multipart()
           self.logger.info('New MISP-Message received.')
           Process(target = self.process, args=msg).start()
        s.close()
        self.logger.info("Connection closed!")

    def process(self, msg):
        self.event_handler.process(msg)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='MISP ZMQ EventHandler listening for new ZMQ Events.')
    parser.add_argument('-c', '--config', dest='config_path',
                                    action='store',
                                    default="/etc/misp_eventhandler/config.yml",
                                    metavar="FILE",
                                    help='Path to config file (default: /etc/misp_eventhandler/config.yml)'
    )
    parser.add_argument('-r', '--host', dest='host',
                                  action='store_const',
                                  const="host",
                                  default="localhost",
                                  help='MISP ZMQ IP Address (default: localhost)'
    )
    parser.add_argument('-p', '--port', dest='port',
                                  default=50000,
                                  type=int,
                                  help='MIPS ZMQ Port (default: 50000)'
    )
    parser.add_argument('-e', '--env', dest='env',
                                  action='store_const',
                                  const="env",
                                  default="production",
                                  help='Define execution environment (default: production)'
    )
    parser.add_argument('-d', '--deamon', dest='deamon',
                                  action='store_true',
                                  default=False,
                                  help='Run in background as a deamon (default: False)'
    )
    parser.add_argument('--log-level', dest='log_level',
                                  action='store_const',
                                  default="info",
                                  const="log_level",
                                  help='define log level (default: info)'
    )

    main = Main(parser.parse_args())
    main.start()
