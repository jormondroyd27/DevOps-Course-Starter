# from pymongo import mongomock
# import pytest
# from dotenv import load_dotenv, find_dotenv
# from todo_app.app import create_app

# @pytest.fixture
# def client():
#     file_path = find_dotenv('.env.test')
#     load_dotenv(file_path, override=True)

#     with mongomock.patch(servers=(('fakemongo.com', 27017),)):
#         test_app = create_app()
#         with test_app.test_client() as client:
#             yield client

# from todo_app.data.todo_item import TodoItem
# from todo_app.data.viewmodel import ViewModel

# def test_todo_items():
#     item = TodoItem("123", "test item")
#     viewmodel = ViewModel([item], [], [])
#     assert viewmodel.todo_lists == [item]

# def test_doing_items():
#     item = TodoItem("123", "test item")
#     viewmodel = ViewModel([], [item], [])
#     assert viewmodel.doing_lists == [item]

# def test_done_items():
#     item = TodoItem("123", "test item")
#     viewmodel = ViewModel([], [], [item])
#     assert viewmodel.done_lists == [item]