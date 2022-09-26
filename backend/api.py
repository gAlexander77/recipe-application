#!/usr/bin/env python3

from flask import Flask
import src.sql as sql
import logging

app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True

print("flask works!")
print("ctrl+c: quit")
