#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/")

from simple-flask-api-modular import app as application
application.secret_key = 'simple key'
