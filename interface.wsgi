#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/uwsg/iotplatform/')
from interface import app as application
application.secret_key = '23333333'

