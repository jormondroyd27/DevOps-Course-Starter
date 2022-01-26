import requests
import os

SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SECRET_SECRET = os.getenv('SECRET_SECRET')
BOARD_ID = os.getenv('BOARD_ID')
CARD_ID = os.getenv('CARD_ID')
TODO_LIST = os.getenv('todo_list')
DOING_LIST = os.getenv('doing_list')
DONE_LIST = os.getenv('done_list')
BOARD_ID = os.getenv('BOARD_ID')

def fetch_list(list):
    url = f"https://api.trello.com/1/boards/{BOARD_ID}"
    query = {
        'key' : SECRET_KEY,
        'token' : SECRET_TOKEN,
        'cards' : 'open',
        'lists' : 'open'
    }
    response = requests.get(url, data=query).json()
    todo_cards = []
    for list_items in response['cards']:
        if list_items['idList'] == list:
            todo_cards.append(list_items)
    return todo_cards

    

    
    
    
    
    


# get doing cards




# get done cards
