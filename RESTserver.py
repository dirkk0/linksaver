from flask import Flask
from flask import json
from flask import request

from db_google import writeEntry

app = Flask(__name__)

@app.route('/messages', methods = ['POST'])
def api_messages():
    if request.headers['Content-Type'] == 'application/json':
        writeEntry(request.json['entry'],request.json['link'])
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run()