from todo_app.data.todo_item import TodoItem
from todo_app.data.viewmodel import ViewModel

def test_todo_items():
    item = TodoItem("123", "test item")
    viewmodel = ViewModel([item], [], [])
    assert viewmodel.todo_lists == [item]

def test_doing_items():
    item = TodoItem("123", "test item")
    viewmodel = ViewModel([], [item], [])
    assert viewmodel.doing_lists == [item]

def test_done_items():
    item = TodoItem("123", "test item")
    viewmodel = ViewModel([], [], [item])
    assert viewmodel.done_lists == [item]

# 1. A user can add a new item to the to do list - e2e
# 2. The app can handle a response from Trello's API - integration
# 3. The item sets a completed_at field to the current time when it is marked as 'Done' - unit
