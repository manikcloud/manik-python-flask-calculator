from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return str(result)

    except ValueError:
        return "Error: Invalid input"

@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 - num2
        return str(result)

    except ValueError:
        return "Error: Invalid input"

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 * num2
        return str(result)

    except ValueError:
        return "Error: Invalid input"

@app.route('/divide', methods=['POST'])
def divide():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        if num2 == 0:
            return "Error: Cannot divide by zero"
        result = num1 / num2
        return str(result)

    except ValueError:
        return "Error: Invalid input"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
