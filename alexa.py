'''
Simulation of Alexa service

'''
import requests


fromAlexa = '''{
  "version": "string",
  "session": {
    "new": true,
    "sessionId": "string",
    "application": {
      "applicationId": "string"
    },
    "attributes": {},
    "user": {
      "userId": "string",
      "accessToken": "string"
    }
  },
  "request": {
  "type": "IntentRequest",
  "requestId": "string",
  "timestamp": "string",
  "locale": "string",
  "intent": {
    "name": "GetMusicalNote",
    "slots": {
      "Note": {
        "name": "Note",
        "value": "A"
      }
    }
  }
}
}'''
r = requests.post('http://localhost:5000/token', data = fromAlexa)
#r = requests.post('http://alexadiapason-cuacuak.rhcloud.com/token',
#    data = fromAlexa)
print(r.text)


