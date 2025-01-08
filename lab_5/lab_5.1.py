class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        if self.year is None:
            return f"{self.title}-книга написанная автором {self.author}"
        else:
            return f"{self.title}-книга написанная автором {self.author} и опубликованная в  {self.title}?!\nP.S.Шучу,на самом деле в {self.year} году."


book = Book("1984", "Джордж Оруэлл")
book_2 = Book("1984", "Джордж Оруэлл",year=1949)
print(book_2.get_info())


