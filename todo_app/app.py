from distutils.log import debug
from flask import Flask, url_for, render_template, redirect, request
from todo_app.flask_config import Config
from todo_app.data.trello_items import fetch_list, create_todo_card, create_doing_card, create_done_card, delete_card, move_card_doing, move_card_done

import os
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config())

SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
SECRET_SECRET = os.getenv('SECRET_SECRET')
BOARD_ID = os.getenv('BOARD_ID')
CARD_ID = os.getenv('CARD_ID')
TODO_LIST = os.getenv('todo_list')
DOING_LIST = os.getenv('doing_list')
DONE_LIST = os.getenv('done_list')
BOARD_ID = os.getenv('BOARD_ID')

@app.route('/', methods=["GET"])
def index():
    todo_lists = fetch_list(TODO_LIST)
    doing_lists = fetch_list(DOING_LIST)
    done_lists = fetch_list(DONE_LIST)
    return render_template('index.html', todo_lists=todo_lists, doing_lists=doing_lists, done_lists=done_lists)

@app.route('/addtodo', methods=["POST"])
def add_todo():
    name = request.form['name']
    create_todo_card(name)
    return redirect(url_for('index')) 

@app.route('/adddoing', methods=["POST"])
def add_doing():
    name = request.form['name']
    create_doing_card(name)
    return redirect(url_for('index')) 

@app.route('/adddone', methods=["POST"])
def add_done():
    name = request.form['name']
    create_done_card(name)
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    id = request.form['remove']
    delete_card(id)
    return redirect(url_for('index'))

@app.route('/move_doing/<id>', methods=["POST"])
def move_to_doing(id):
    id = request.form['move_to_doing']
    move_card_doing(id)
    return redirect(url_for('index'))

@app.route('/move_done/<id>', methods=["POST"])
def move_to_done(id):
    id = request.form['move_to_done']
    move_card_done(id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
