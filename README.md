MISP ZMQ Event Handler
========================

[MISP](https://github.com/MISP/MISP) support [ZMQ](http://zguide.zeromq.org/) as an Event Message Broker for PubSub to extend the MISP API.

The MISP-ZMQ-EventHandler is an multi threaded, fast and reliable, modularized and extensible MISP-Event processing Engine. 

With the MISP-ZMQ-EventHandler you can write own plugins for bulk processing like Detectors or insert MISP-Events to any Database for further processing. It will be also possible to execute analysing tasks in near real-time and refine IOC's by setting new sighting automaticly or update Firewalls- and IDPS-Rules.

In further versions CUDA support and distributed processing will be implemented for complex tasks like machine learning and natural language processing. 

Any ideas welcome. This tool is under development and it is not working well yet.

---------------

### Installation

Use

```bash
pip3 install -r requirements.txt
```

Or 

```bash
make init
```

Install it systemwide

```bash
sudo python3 setup.py install
```

Run the Client by using

```bash
sudo systemctl enable misp_event_handler.service
sudo systemctl start misp_event_handler.service
```

Logfile stored in */var/log/misp_event_handler.log*

### Plugins

Plugins must be implemented by Using a well formed Abstract Class src.plugins.Plugin
There are multiple types of Plugins like Output-, Compute- and Filter-Plugins.

*will follow*

### Tests

Use setup.py to run nose-Tests

```bash
python3 setup.py test
```

Or use the integrated Makefile

```bash
make test
```

Run a single Tests for plugins
```bash
python3 ./setup.py nosetests --nocapture -w plugins/output/misp2elastic/tests/misp2elastic_test.py
```

### Documentation

*will follow*
