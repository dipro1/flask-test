from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"Hello {name}"
    return "Hello"


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_value = float(celsius)
    except ValueError:
        # Not a valid number
        return f'"{celsius}" is not a valid number. Please enter a numeric value.'

    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
    return f"{celsius_value}°C is {fahrenheit_value:.2f}°F"


if __name__ == '__main__':
    app.run()