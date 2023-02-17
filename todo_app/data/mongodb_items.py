from todo_app.data.todoitem import TodoItem
from bson import ObjectId
import os, pymongo
from dotenv import load_dotenv
load_dotenv()

connection_string = os.getenv('CONNECTION_STRING')
database_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')

client = pymongo.MongoClient(connection_string)

db = client.james_database

todo_collection = db.james_collection

# book = { 
# 	"author" : "J.R.R Tolkien", 
# 	"title" : "Lailas book 2" 
# 	}

# todo_collection.insert_one(book)

# for x in todo_collection.find():
#     print(x)

def fetch_tasks():
    tasks = []
    for task in todo_collection.find():
        tasks.append(TodoItem(id=task["_id"], title=task["title"], status=task["status"]))
    return tasks

    # title=task["title"]

def add_task_todo(title):
    todo_collection.insert_one({
        "title": title,
        "status": "TODO"
    })

def add_task_doing(title):
    todo_collection.insert_one({
        "title": title,
        "status": "DOING"
    })

def add_task_done(title):
    todo_collection.insert_one({
        "title": title,
        "status": "DONE"
    })

def update_status_todoing(id):
    my_query = { 
        "_id" : ObjectId(id) 
        }

    new_value = { 
        "$set": { 
            "status" : "DOING" 
            } }

    todo_collection.update_one(my_query, new_value)

def update_status_todone(id):
    my_query = { 
        "_id" : ObjectId(id) 
        }

    new_value = { 
        "$set": { 
            "status" : "DONE" 
            } }

    todo_collection.update_one(my_query, new_value)
    
def remove_task(id):
    todo_collection.delete_one({
        "_id" : ObjectId(id) 
    })