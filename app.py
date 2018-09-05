from flask import Flask

app = Flask(__name__)

"""
    If the url route is even respond with Fizz,
    if the route is odd respond with Buzz.
"""
@app.route('/fizzbuzz/<int:value_id>')
def fizz_buzz(value_id):
    if value_id % 2 == 0:
        return 'Fizz', 200
    else:
        return 'Buzz', 200

# Any string route respond with error
@app.route('/fizzbuzz/<name>')
def no_fizz_buzz(name):
    return 'Error', 400


if __name__ == "__main__":
    app.run(port=34232)
 