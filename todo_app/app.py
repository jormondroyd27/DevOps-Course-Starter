from flask import Flask, url_for, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

# routes the URL path
@app.route('/', methods=["GET"])
def index():
    # renders index.html to the route '/' and passes the argument get_items() from session_items.py file
    return render_template('index.html', get_items = get_items)

# adding a new route and setting request method to POST
@app.route('/additem', methods=["POST"])
def additems():
    # retrieve the item title from the form data
    item = request.form['title']
    # call add_item function with the item
    add_item(item)
    # redirect user back to the index page
    return redirect(url_for('index'))




if __name__ == "__main__":
    app.run()
