from flask import Flask, url_for, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

# routes the URL path
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', items=get_items())

# adding a new route and setting request method to POST
@app.route('/additem', methods=["POST"])
def additems():
    item = request.form['title']
    add_item(item)
    return redirect(url_for('index'))    

if __name__ == "__main__":
    app.run()