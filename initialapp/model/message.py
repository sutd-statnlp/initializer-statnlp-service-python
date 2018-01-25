

class Message(object):
    def __init__(self, title, content):
      self.title = title
      self.content = content

    def toJSON(self):
      return {'title': self.title, 'content': self.content}