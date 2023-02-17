from flask import Flask, url_for, render_template, redirect, request
from todo_app.flask_config import Config
from todo_app.data.mongodb_items import fetch_tasks, add_task_todo, add_task_doing, add_task_done, update_status_todoing, update_status_todone, remove_task
from todo_app.data.taskmodel import TaskModel
import os
import requests
from dotenv import load_dotenv
load_dotenv()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # TODO_LIST = os.getenv('todo_list')
    # DOING_LIST = os.getenv('doing_list')
    # DONE_LIST = os.getenv('done_list')

    # @app.route('/', methods=["GET"])
    # def index():
    #     todo_lists = fetch_list(TODO_LIST)
    #     doing_lists = fetch_list(DOING_LIST)
    #     done_lists = fetch_list(DONE_LIST)
    #     item_view_model = ViewModel(todo_lists, doing_lists, done_lists)
    #     return render_template('index.html', view_model=item_view_model)

    @app.route('/', methods=["GET"])
    def index():
        all_tasks = fetch_tasks()
        task_view_model = TaskModel(all_tasks)
        return render_template('index.html', task_model=task_view_model)

    @app.route('/addtasktodo', methods=["POST"])
    def add_todo():
        name = request.form['name']
        add_task_todo(name)
        return redirect(url_for('index')) 

    @app.route('/addtaskdoing', methods=["POST"])
    def add_doing():
        name = request.form['name']
        add_task_doing(name)
        return redirect(url_for('index')) 

    @app.route('/addtaskdone', methods=["POST"])
    def add_done():
        name = request.form['name']
        add_task_done(name)
        return redirect(url_for('index'))

    @app.route('/delete/<id>', methods=["POST"])
    def delete(id):
        task = request.form['remove']
        remove_task(task)
        return redirect(url_for('index'))

    @app.route('/move_doing/<id>', methods=["POST"])
    def move_to_doing(id):
        task = request.form['move_to_doing']
        update_status_todoing(task)
        return redirect(url_for('index'))

    @app.route('/move_done/<id>', methods=["POST"])
    def move_to_done(id):
        task = request.form['move_to_done']
        update_status_todone(task)
        return redirect(url_for('index'))

    return app

if __name__ == "__main__":
    app = create_app() 
    app.run(debug=True)


