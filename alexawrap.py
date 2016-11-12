import logging

from flask import Flask
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.intent('GetMusicalNote', mapping={'note': 'Note'})
def get_note(note):
    text = "The note is %s" % note
    return statement(text).simple_card('Turning fork', text)


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
