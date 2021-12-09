from .. import mailsender, db
from flask import current_app, render_template, Blueprint
from flask_mail import Message
from smtplib import SMTPException

def sendMail(to, subject, template, **kwargs):

    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    try:

        msg.body = render_template(f'{template}.txt', **kwargs)

        #msg.html = render_template(f'{template}.html', **kwargs)


        result = mailsender.send(msg)

    except SMTPException as e:
        print(str(e))
        return "Mail deliver failed"
    return True

mail = Blueprint('mail', __name__, url_prefix='/mail')