#import asyncio
import zmq
import syslog
import os
import ConfigParser
import io
#import zmq.asyncio
import multiprocessing as mp
from multiprocessing import Process, Pool
from event_handler import EventHandler


ctx = zmq.Context()
#mp.set_start_method("fork")
pool = Pool(processes=mp.cpu_count())

class Main():

    def __init__(self):
        with open("../config.ini") as f:
          sample_config = f.read()
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.readfp(io.BytesIO(sample_config))

    #  ASYNC-Socket to talk to server
    def recv_and_process(self):
        print('Connecting to MISP-ZMQ Server...')
        s = ctx.socket(zmq.SUB)
        s.connect('tcp://192.168.0.24:50000')
        s.setsockopt(zmq.SUBSCRIBE, b'')
        print('MISP-Server connection established.')
        print('Subscribed and listening for MISP-Messages...\n')
        while True:
           # Process all parts of the message
           msg = s.recv_multipart()
           print('New MISP-Message received.')
           pool.apply_async(EventHandler, args=(msg))
           #p = Process(target = EventHandler.process(msg), args = msg)
           #p.start()
        s.close()
        print("Connection closed!")


if __name__ == "__main__":
    main = Main()
    main.recv_and_process()
