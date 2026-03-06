book_list = []

class Booking:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f'{self.first} {self.last}'

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        if value == "":
            raise ValueError("No firstname given")
        self._first = value


while True:
    first = input('What is your first name: ')
    last = input('What is your last name: ')

    try:
        newbook = Booking(first, last)
    except ValueError as e:
        print(e)
    else:
         book_list.append(newbook)

    ask = input("do you want to add more (y/n)")
    if ask == "n":
        break

for book in book_list:
    print(book)