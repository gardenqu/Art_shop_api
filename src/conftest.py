from src.flaskdr import create_app
from src.flaskdr.api_restful import api
import pytest


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True


    with app.app_context():
        with app.test_client() as client:
            yield client