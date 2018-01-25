from flask import Flask
from flask_restplus import Api
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask('initialapp')

import initialapp.views

api = Api(app, version='1.0', title='StatNLP Service',
    description='StatNLP Service', doc=False
)

import initialapp.rest.messageresource
