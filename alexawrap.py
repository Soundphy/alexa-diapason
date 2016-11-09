from flask import Flask, request
import traceback

app = Flask(__name__)

#Template of the response required by Alexa - JSON format
toAlexaTemplate = '''{
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "SSML",
      "ssml": "<speak><audio src="https://%s.mp3" /></speak>"
    }
  }
}
'''

@app.route('/token', methods=['POST'])
def post_handler():
    if request.method == 'POST':
        try:
            getdata = request.get_json(force=True)
            note = getdata['request']['intent']['slots']['Note']['value']
            toAlexa = toAlexaTemplate % note
            return (toAlexa)
        except Exception:
            return traceback.format_exc()

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
