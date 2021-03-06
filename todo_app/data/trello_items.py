import requests
import os

from todo_app.data.todo_item import TodoItem

def fetch_list(list_id):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    BOARD_ID = os.getenv('BOARD_ID')
    url = f"https://api.trello.com/1/boards/{BOARD_ID}"
    query = {
        'key' : SECRET_KEY,
        'token' : SECRET_TOKEN,
        'cards' : 'open',
        'lists' : 'open'
    }
    response = requests.get(url, data=query).json()
    items: list_id[TodoItem] = []
    for card in response['cards']:
        if card['idList'] == list_id:
            item = TodoItem(card["id"], card["name"])
            items.append(item)
    return items

def create_todo_card(name):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    TODO_LIST = os.getenv('todo_list')
    url = f'https://api.trello.com/1/cards'
    query = {
        'idList' : TODO_LIST,
        'name' : name,
        'key' : SECRET_KEY,
        'token' : SECRET_TOKEN,
    }
    return requests.post(url, data=query).json()

def create_doing_card(name):
    DOING_LIST = os.getenv('doing_list')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    url = f'https://api.trello.com/1/cards'
    query = {
        'idList' : DOING_LIST,
        'name' : name,
        'key' : SECRET_KEY,
        'token' : SECRET_TOKEN,
    }
    return requests.post(url, data=query).json()

def create_done_card(name):
    DONE_LIST = os.getenv('done_list')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    url = f'https://api.trello.com/1/cards'
    query = {
        'idList' : DONE_LIST,
        'name' : name,
        'key' : SECRET_KEY,
        'token' : SECRET_TOKEN,
    }
    return requests.post(url, data=query).json()

def delete_card(id):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    url = f'https://api.trello.com/1/cards/{id}?key={SECRET_KEY}&token={SECRET_TOKEN}'
    headers = {
    "Accept": "application/json"
    }
    return requests.delete(url, data=headers).json()

def move_card_doing(id):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    DOING_LIST = os.getenv('doing_list')
    url = f'https://api.trello.com/1/cards/{id}?idList={DOING_LIST}&key={SECRET_KEY}&token={SECRET_TOKEN}'
    headers = {
    "Accept": "application/json"
    }
    return requests.put(url, data=headers).json()

def move_card_done(id):
    DONE_LIST = os.getenv('done_list')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_TOKEN = os.getenv('SECRET_TOKEN')
    url = f'https://api.trello.com/1/cards/{id}?idList={DONE_LIST}&key={SECRET_KEY}&token={SECRET_TOKEN}'
    headers = {
    "Accept": "application/json"
    }
    return requests.put(url, data=headers).json()