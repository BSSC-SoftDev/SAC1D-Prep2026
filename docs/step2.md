# Step 2

In this step you will add validation. 

As adding or updating a booking should ideally involve some form of validation we
need to consider where validation code should occur. For example, our code could 
check the values it will assign to `first`, and `last` etc. prior to the Booking being
instantiated via the line of code `newbook = Booking(first, last)`. However, it makes 
sense that the `Booking` class code in the code's `__init__` method checks that the 
data it's been supplied is valid. This is part of the idea of OOP programming - in that
we would like the class to be robust. So if our program tries to instantiate a Booking object
with erroneous data, then our `Booking` class can handle it appropriately. 

However, there is an issue with such an approach, in that `__init()__` is not a constructor 
and the Booking object is already created by the time `__init()__` runs. See the page [here](https://sites.google.com/bssc.edu.au/bssd34/unit-3/area-of-study-1-programming/principles-of-oop) 
under the heading **"Object Initialisation: The __init__() Method"** which discusses this.
As such we'll treat the `__init__()` function like it's a 
constructor and use a Pythonic way to ensure any bookings with errors don't get added to our 
Bookings list.

### protected and private variables
Most OOP languages allow for protected and private variables. Protected and private 
variables within a class (or an object), cannot be directly accessed by code other
than by the code which is part of the class definition. Python does not support truly
protected and private variables, but does have some techniques to mimic this behaviour. 
See the page [here](https://sites.google.com/bssc.edu.au/bssd34/unit-3/area-of-study-1-programming/principles-of-oop) 
under the heading **"Encapsulation: Access Modifiers"** for more details. To complete this step 
we will make use of single underscore variables 
(which are commonly referred to as protected values). These variables are not truly protected 
but Python programmers agree to treat them as such. 

The new protected variables we will introduce will have the same name as the attributes
from step1.py program, but with an underscore in front of them. The new variables are as
follows.

`_first`,
`_last`,
`_mobile`, and
`_no_of_guests`

### @property, @xxxx.setter decorators
As with protected and private variables, most OOP languages support getter and setter 
functions. These functions are designed to get and set the values of the attributes
(variables) which are part of the class(or object). Python does have getter and setter
functions which are created by the use of certain decorators. In Python decorators are
lines of code that begin with '@' symbol. 

### Getters, Setters, and the @property Decorator
In traditional Object-Oriented languages, developers write explicit "getter" and "setter" 
methods (like `get_score()` and `set_score()`) to safely read and modify an object's attributes. 
Python achieves this same goal in a much cleaner way using decorators.

**What are Decorators?** In Python, a decorator is a special command that alters how a method 
behaves. They are placed on the line immediately above a method definition and always begin 
with the @ symbol.

**The `@property` Decorator (The Getter):** Adding `@property` above a method transforms it into 
a "getter." This allows you to access the method as if it were a simple attribute 
(e.g., typing `user.score` instead of calling `user.get_score()`). Because of this elegant 
syntax, writing separate, traditional getter functions in Python is considered redundant.

**The Redundant `@<attribute>.getter`:** You might occasionally see references to an explicit 
`@xxxx.getter` decorator. While Python does technically support this, it is almost never used. 
This is because the `@property` decorator inherently acts as the getter by default, making a 
separate `@xxxx.getter` declaration completely redundant.

**The @<attribute>.setter Decorator:** To safely modify that same attribute, you use a 
corresponding setter decorator, such as `@score.setter`. This allows you to run background 
logic—like error checking or validation—whenever someone tries to assign a new value to 
it using standard equals-sign syntax (e.g., `user.score = 100`).

**The "Property" Naming Confusion:**
Be aware that the word "property" can be a point of confusion for Python learners. 
In Python, a "property" is specifically a method that has been wrapped 
with the @property decorator. However, more typical of other programming languages, a "property"
refers to an "attribute" or "variable" within a class or object.


### Complete step 2
The code in **step2.py** is a modified version of **step1.py**. This code has in effect 
changed the attribute (or class variable) named `first` into a property called 
`first`. At the same time it has introduced an attribute named `_first`. It has also 
introduced two class functions - that perform the function of getting and setting. Within
the setter function, it performs validation and raises a ValueError if no firstname was
supplied. This code technique can be quite confusing at first inspection, 
and I suggest you watch https://youtu.be/k4efInGWlYI for 
an explanation of this technique if it's not clear.

Within the while loop, the code handles any error within the try except block. Bookings
only get appended to the `book_list` where no error was raised.

In a similar way you update should your code to Step1 to make this same change, and also 
the following changes.

* Make `last` a property and introduce `_last` as an attribute. Perform existence validation
so that an empty string can't be assigned to `_last`.
* Make `mobile` a property and introduce `_mobile` as an attribute. Perform existence validation
so that an empty string can't be assigned to `_mobile`.
* Make `no_of_guests` a property and introduce `_no_of_guests` as an attribute. Perform validation
so that the value will only be assigned to `_no_of_guests` if it is an 
integer between and including the values 1 and 4. When raising this error - ideally your
program displays the appropriate error type and details to the user:
  * nothing entered
  * not a valid integer
  * not a number between 1 and 4

If any of the values above is not valid then a ValueError is raised the booking is not 
added to the list. 

Save your completed file as **step2*firstamelastname*.py** - where _firstname_ is your first 
name and _lastname_ is your lastname. 

Return to [index](../README.md)
