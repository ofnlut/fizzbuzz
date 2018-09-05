from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/fizzbuzz/<int:value_id>')
def fizz_buzz(value_id):
    if value_id % 2 == 0:
        return 'Fizz', 200
    else:
        return 'Buzz', 200

@app.route('/fizzbuzz/<name>')
def no_fizz_buzz(name):
    return 'Error', 400


if __name__ == "__main__":
    app.run(port=34232)
 