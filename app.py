import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port=int(os.environ.get('PORT', 8000)),
            debug=True)
