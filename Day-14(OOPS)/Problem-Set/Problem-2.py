# 2. Implement __len__, __repr__, and __eq__ methods in a custom class.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __eq__(self, other):
        return (self.title == other.title) and (self.author == other.author)