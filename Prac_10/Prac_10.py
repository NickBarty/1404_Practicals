from flask import Flask

app = Flask(__name__)


@app.route('/greet')
def greet():
    return "Hello"


@app.route('/')
def hello_world():
    return '<h1>Hello World :) </h1>'


if __name__ == '__main__':
    app.run()
