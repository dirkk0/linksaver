from flask import Flask
from flask import json
from flask import request

from db_sqlite import writeEntry

# uncomment the next line for google spreadsheet support.
# from db_google import writeEntry  #<---- this line
# dont forget to create a credential.json file from
# the credentials_template.json!

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