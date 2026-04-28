# Step 3

In this step you will add functionality so that your program can perform the basic 
Create Read Update and Delete (CRUD) functionality for the list of bookings.

As it is, our program can create (C) bookings, although at this stage only in RAM. We
also want our program to be able to store these bookings in a file. In our case 
we'll write these bookings to a CSV file. Our program should also be able to read this
file, update and delete required bookings, and write the updated booking details back to 
the file.

### Writing the bookings to a file

The code example in 'step3.py' writes the list of bookings to a csv file named 'bookings.csv' 
 just prior to the program finishing. In the line `writer.writerow(book.get_list())` the 
program calls a method `get_list()`. This method returns the booking as a list so that it is
in the appropriate format to be written to the CSV file. 
You need to add similar functionality to your program from the previous step. However, you 
will need to adjust the method function `def get_list(self)` function so that it returns all the
attributes for each booking in the returned list.

### Reading the bookings into a file

In a similar fashion you should be able to write some code which reads the bookings.csv file
into the `book_list` list. This code does not require any additional class functions. You should 
be able to use the code which reads a CSV into a list, and each row read from the file is 
added to the `book_list` list. It should be able to take advantage of the validation which 
already exists in the class setter functions. There is some sample code [here](https://sites.google.com/bssc.edu.au/bssd34/unit-3/area-of-study-1-programming/characteristics-of-data-sources) 
that you can use as a starting point under the heading **"Code examples for reading and writing 
to a CSV without headers from and to a list of lists"**. Hint: it is likely simplest to read
the file a line at a time into a List and then pass contents of the List to "__init__" function. 
You can possibly use the * or "splat" operator to assist eith this.

### Updating and deleting bookings

Several other changes have been made in 'step3.py'. The following functions: `add_bookings()`, 
`delete_booking()`, and 
 `update_booking()` have been added. A new while loop has been included with a match case
statement included to allow the user to choose whether they want to add, delete or update bookings.
_The match case structure is an alternate to using if/elif/else statements and makes the syntax
a little neater._
The `add_bookings()` has code that previously existed but is now placed in this function. 
The other
two functions have some incomplete code. I've provided some code in `def delete_booking()`. The 
code simply prints out all the values in the `book_list` list. It uses the `enumerate()` function
to assist with this so that the print statement in the for loop can print both the index value
and the list value. _We could do the same without an `enumerate()` function, but we would then be
responsible for setting `i = 0` prior to the `for` loop and then incrementing `i` using 
something like `i += 1` within
the loop. The enumerate function just makes the code neater, but you'll never see this type
of enumerate syntax in pseudocode in a VCAA VCE exam._ The purpose of the code in the 
`def delete_booking()` is that you can add some additional code which allows the user to
choose the index item they want to delete and then delete that item from the list. As such 
completing the `def delete_booking()` function only requires a few extra lines of code. A 
similar technique could be used in the `update_booking()` function that allows user to 
select the index for the record they need to update and then the field they want to update.
Remember, your code should already have setters for all the booking values and you can 
make use of these to update a value. For example if my code needs to update the `first` name
to 'John' for a booking at index '1' then the code to do this is `book_list[1].first = "John"`.

### What your completed Step 3 program should do
Your finished program should allow for the CRUD functionality on all four fields (first, last, 
mobile and no_of_guests). This will include the ability to read and write the records into a CSV 
file.

Save your completed file as **step3*firstamelastname*.py** - where _firstname_ is your first 
name and _lastname_ is your lastname. 

Return to [index](../README.md)
