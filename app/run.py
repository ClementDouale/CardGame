from flask import Flask
from routes import bp  # Import the Blueprint
import os

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')
app.register_blueprint(bp, url_prefix='/')  # Registering the Blueprint


if __name__ == '__main__':
    app.run(debug=True)
