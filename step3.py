import csv

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

    def get_list(self):
        return [self._first,self.last]

def add_bookings():
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

def delete_booking():
    for i, book in enumerate(book_list):
        print(f"{i}, {book}")

def update_booking():
    pass

while True:
    choice = int(input("select a number for what you want to do \n1)Add booking," +""
                "\n2)Delete Booking, \n3)Update Booking, \n4)Quit\n:"))
    match choice:
        case 1:
            add_bookings()
        case 2:
            delete_booking()
        case 3:
            update_booking()
        case 4:
            break


for book in book_list:
    print(book)

with open('bookings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for book in book_list:
        writer.writerow(book.get_list())