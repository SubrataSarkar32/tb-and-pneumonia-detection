
from flask.ext.mail import Message

from app import app, mail


def send(recipient, subject, body):
    '''
    Send a mail to a recipient. The body is usually a rendered HTML template.
    The sender's credentials has been configured in the config.py file.
    '''
    sender = app.config['ADMINS'][0]
    message = Message(subject, sender=sender, recipients=[recipient])
    message.html = body
    mail.send(message)
