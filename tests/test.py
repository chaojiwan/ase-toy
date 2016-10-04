from flask import Flask
from models import db, User

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xtifhtrqnydawd:n3xiwg41_vMzqBKG99pKt3gX4D@ec2-50-19-219-148.compute-1.amazonaws.com:5432/d9265ge1sbuard'
db.init_app(app)

app.secret_key = "development-key"


def test_signup():
    with app.app_context():
        newuser = User("mc", "chu", "tester@gmail.com", "password")
        print "test user: "+User.email
        db.session.add(newuser)
        db.session.commit()

        email = "tester@gmail.com"
        password = "password"
        user = User.query.filter_by(email=email).first()
        assert user is not None and user.check_password(password)
        print "sign up success."


def test_signin():
    with app.app_context():
        email = "test1@gmail.com"
        password = "password"
        print "test existing user: "+email
        user = User.query.filter_by(email=email).first()
        assert user is not None and user.check_password(password)
        print "log in success."

if __name__ == '__main__':
    app.run()
