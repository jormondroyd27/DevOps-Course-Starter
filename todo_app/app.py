from flask import Flask, url_for, render_template, request
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

# routes the URL path
@app.route('/', methods=["GET"])
def index():
    # renders index.html to the route '/' and passes the argument get_items() from session_items.py file
    return render_template('index.html', get_items = get_items)

if __name__ == "__main__":
    app.run()
