from curses import A_DIM


class TodoItem:
    def __init__(self, id, title) -> None:
        self.id = id
        self.title = title
        pass