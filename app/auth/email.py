from flask import render_template, current_app
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_token()
    send_email('[Twipy] Reset Your Password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))


def send_registration_email(user):
    token = user.get_token()
    send_email('[Twipy] Welcome',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/welcome.txt',
                                         user=user, token=token),
               html_body=render_template('email/welcome.html',
                                         user=user, token=token))
