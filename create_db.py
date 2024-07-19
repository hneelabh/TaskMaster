import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

with app.app_context():
    print("Current working directory:", os.getcwd())
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
    if os.path.exists(os.path.join(base_dir, 'test.db')):
        print("Database file 'test.db' created successfully.")
    else:
        print("Database file 'test.db' not found.")
