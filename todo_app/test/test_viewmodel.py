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