# server.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=1300)