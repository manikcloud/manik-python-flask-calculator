from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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

        return redirect(url_for('result', result=result))

    return render_template('index.html')

@app.route('/result/<float:result>')
def result(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
