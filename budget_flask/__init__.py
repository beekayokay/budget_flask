from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6C2E1DB1B3A914D0BEC00336BA63F33B253253E45E7B63B2939896D84819B538'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from budget_flask import routes
