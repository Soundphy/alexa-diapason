import logging

from flask import Flask
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

DIAPASON_URL = "https://diapason.reset.etsii.upm.es/v0/alexa/"

@ask.intent('GetMusicalNote', mapping={'note': 'Note'})
def get_note(note):
    DIAPASON_URL_NOTE = DIAPASON_URL + note
    text = "<speak><audio src='%s' /></speak>" % DIAPASON_URL_NOTE
    return statement(text).simple_card('Turning fork', text)


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
