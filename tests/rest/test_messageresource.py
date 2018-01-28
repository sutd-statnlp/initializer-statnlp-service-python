
from flask import json
from initialapp import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_getMessages(client):
    resp = client.get('/api/messages')
    data = json.loads(resp.data)

    assert len(data) > 0