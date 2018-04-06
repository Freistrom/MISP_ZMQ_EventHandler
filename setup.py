# -*- coding: utf-8 -*-

# Learn more: https://github.com/dpautz/misp_zmq_event_handler/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MISP_ZMQ_EventHandler',
    version='0.1.0',
    description='MISP Event Handler for ZMQ PubSub Events',
    long_description=readme,
    author='David SPautz',
    author_email='d.spautz@web.de',
    url='https://github.com/dspautz/misp_zmq_event_handler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite = 'nose.collector'
)
