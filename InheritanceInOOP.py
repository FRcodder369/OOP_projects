
class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def open(self):
        print(f'opened the {self.name} which has {self.pages} pages')
b1 = Book('Py Programming', 800)


class Textbook(Book):
    print('a new textbook')
    def __init__(self, field, grade, name, pages):
        Book.__init__(self, name, pages)
        self.field = field
        self.grade = grade

    def open(self):
        print(f'opened {self.name} in field: {self.field} {self.grade} grade')


t1 = Textbook('math', 5, 'mathof5', 150)



for book in [b1, t1]:
    book.open()