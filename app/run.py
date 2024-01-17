from flask import Flask
from routes import app as routes_app

app = Flask(__name__)
app.register_blueprint(routes_app)

@app.route('/')
def index():
    return "This will be overridden by routes.py"

if __name__ == '__main__':
    app.run(debug=True)
