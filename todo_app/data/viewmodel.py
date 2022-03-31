class ViewModel:
    def __init__(self, todo_lists, doing_lists, done_lists):
        self._todo_lists = todo_lists
        self._doing_lists = doing_lists
        self._done_lists = done_lists
    @property
    def todo_lists(self):
        return self._todo_lists
    @property
    def doing_lists(self):
        return self._doing_lists
    @property
    def done_lists(self):
        return self._done_lists