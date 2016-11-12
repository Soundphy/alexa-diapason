import logging

from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent = True)
ask = Ask(app, '/')


logging.getLogger('flask_ask').setLevel(logging.DEBUG)

DIAPASON_URL = "https://diapason.reset.etsii.upm.es/v0/alexa/"

@ask.launch
def launch():
    welcome_text = 'Welcome'
    help_text ='Ask me for a musical note to be played'
    return question(welcome_text).reprompt(help_text)

@ask.intent('GetMusicalNote', mapping={'note': 'Note'})
def get_note(note):
    lnotes = open('speech_assets/LIST_OF_NOTES').read().split()
    if note in lnotes:
        DIAPASON_URL_NOTE = DIAPASON_URL + note
        text = "<speak><audio src='%s' /></speak>" % DIAPASON_URL_NOTE
        card_text = "Playing note " + note
    else:
        text = "The available musical notes are: A, B, C, D, E, F, G"
        card_text = "The available musical notes are: A, B, C, D, E, F, G"
    return statement(text).simple_card('Turning fork', card_text)

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = 'Ask me for a musical note to be played'
    return question(speech_text).reprompt(speech_text).simple_card('Tuning fork', speech_text)

@ask.session_ended
def session_ended():
    return "", 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
