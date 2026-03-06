book_list = []


class Booking:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f'{self.first} {self.last}'

while True:
    first = input('What is your first name: ')
    last = input('What is your last name: ')

    newbook = Booking(first, last)

    book_list.append(newbook)

    ask = input("do you want to add more (y/n)")
    if ask == "n":
        break

for book in book_list:
    print(book)
