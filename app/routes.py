from flask import Flask, Blueprint, render_template, request, redirect, url_for, session

app = Flask(__name__)
app = Blueprint('app', __name__)
app.secret_key = 'your_secret_key'  # to be replaced with a real secret key later (and not in the file later for security reasons)

@app.route('/')
def index():
    equation = "2 + 2 * 3"
    return render_template('index.html', equation=equation)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    # Logic to check the answer
    # ...
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
