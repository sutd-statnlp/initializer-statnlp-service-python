from flask import Flask
from flask_restplus import Resource, fields
from initialapp import api
from initialapp.service.messageservice import MessageService

RESOURCE_FIELDS = api.model('Message', {
    'title': fields.String,
    'content': fields.String
})

MESSAGE_SERVICE = MessageService()

@api.route('/api/messages',endpoint='message-resource')
class MessageResource(Resource):
    @api.marshal_list_with(RESOURCE_FIELDS)
    def get(self):
        return MESSAGE_SERVICE.findAll()
    
    