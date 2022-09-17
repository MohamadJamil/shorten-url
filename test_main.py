from urllib import response
from urlshort import create_app

def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data

def test_api(client):
    response = client.get('/')
    assert b'API' in response.data