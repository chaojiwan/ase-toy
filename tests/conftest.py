from flask import Flask

app = Flask(__name__)

@pytest.fixture
def app():
    app = create_app()
    return app