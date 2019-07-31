import pytest

import src

@pytest.fixture
def instance_app():
    app_config = {'TESTING': True}
    running_app = src.create_app(app_config)
    return running_app

@pytest.fixture
def client(instance_app):
    return instance_app.test_client()