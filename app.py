from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero"
            result = num1 / num2
        else:
            return "Error: Invalid operator"
        
        return str(result)

    except ValueError:
        return "Error: Invalid input"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
