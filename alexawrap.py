import logging
import configparser

from flask import Flask, render_template
from flask_ask import Ask, statement, question


app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent = True)
ask = Ask(app, '/')


logging.getLogger('flask_ask').setLevel(logging.DEBUG)

DIAPASON_URL = "https://diapason.reset.etsii.upm.es/v0/alexa/"

@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    return question(welcome_text).reprompt(help_text)

@ask.intent('GetMusicalNote', mapping={'note': 'Note'})
def get_note(note):
    lnotes = open('speech_assets/LIST_OF_NOTES').read().split()
    if note in lnotes:
        DIAPASON_URL_NOTE = DIAPASON_URL + note
        text = "<speak><audio src='%s' /></speak>" % DIAPASON_URL_NOTE
        card_text = "Playing note " + note
        return statement(text).simple_card('Turning fork', card_text)
    else:
        text = render_template('wrong_note', notes=','.join(lnotes))
        return statement(text)

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    return question(help_text).reprompt(help_text).simple_card('Tuning fork', help_text)

@ask.session_ended
def session_ended():
    return "", 200

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('server.ini')
    app.run(host=config['server']['host'],
            port=int(config['server']['port']),
            threaded=True, debug=True)
