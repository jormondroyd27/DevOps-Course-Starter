import pytest, requests, os
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture 
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app. 
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', get_lists_stub)
    response = client.get('/')
    assert response.status_code == 200
    assert "Test card" in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    def json(self):
        return self.fake_response_data

def get_lists_stub(url, data):
    BOARD_ID = os.environ.get('BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{BOARD_ID}':
        fake_response_data = {
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'idList': os.environ.get('todo_list'), 'name': 'Test card', 'id': '456'}]
        }
    return StubResponse(fake_response_data)