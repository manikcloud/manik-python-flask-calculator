import os
from flask import Flask, render_template, request, redirect, url_for

# create a Flask application instance
app = Flask(__name__)

# define the index route
@app.route('/')
def index():
    return render_template('index.html')

# define the result route
@app.route('/result')
def result():
    return render_template('result.html')

# define the error route
@app.route('/error')
def error():
    return render_template('error.html')

# define the calculate route
@app.route('/calculate', methods=['POST'])
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
    except ValueError:
        return redirect(url_for('error'))

    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return redirect(url_for('error'))
        result = num1 / num2
    else:
        return redirect(url_for('error'))

    return render_template('result.html', result=result)

# define the health check route
@app.route('/health')
def health():
    return 'OK'

# run the application
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
