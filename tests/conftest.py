import pytest

from authz import create_app

# yek instance az app ro dorost mikonim ke betonim app ro insert konim

@pytest.fixture
def app():
    app = create_app()
    return app

# ye human misazim ke betone test kone

@pytest.fixture
def client(app):
    return app.test_client()


