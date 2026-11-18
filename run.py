from flask import Flask
from flask_sqlalchemy import SQLAlchemy

run = Flask(__name__)

run.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg://postgres:admin1234@localhost:5432/uni_site"
)

db = SQLAlchemy(run)

class admins(db.Model):
    __tablename__="admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

with run.app_context():

    username = "nabil"
    password = "2004"
    admin = admins.query.filter_by(
        username=username,
        password=password
    ).first()

    if admin:
        print("Admin exists!")
    else:
        print("Admin not found!")

if __name__ == "__main__":
    run.run(debug=True)