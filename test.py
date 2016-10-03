from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xtifhtrqnydawd:n3xiwg41_vMzqBKG99pKt3gX4D@ec2-50-19-219-148.compute-1.amazonaws.com:5432/d9265ge1sbuard'
db.init_app(app)

app.secret_key = "development-key"

def test_signup():
	with app.app_context():
		newuser = User("mc", "chu", "test1@gmail.com", "password")
		db.session.add(newuser)
		db.session.commit()

		email = "test1@gmail.com"
		password = "password"
		user = User.query.filter_by(email=email).first()
		assert user is not None and user.check_password(password)

def test_signin():
	with app.app_context():
		email = "test1@gmail.com"
		password = "password"
		user = User.query.filter_by(email=email).first()
		assert user is not None and user.check_password(password)

if __name__ == '__main__':
    app.run()
