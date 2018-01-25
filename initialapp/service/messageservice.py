
from initialapp.model.message import Message
import logging

class MessageService(object):

    def __init__(self):
        logging.info('Create MessageService')

    def findAll(self):
        messages = []
        for i in range(0,8):
            messages.append(Message('title' + `i`, 'content' + `i`))
        return messages

