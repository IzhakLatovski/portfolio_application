from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return "HELLO FROM MY WEBSITE 222"

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')