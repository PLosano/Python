# Variables

# They are used to contain information 

# Numercial Variables
# Integers, which correspond to the set of positive or negative integers (1, 2, 0, 123, -3, etc.)
account = 10
# Decimals, which, in addition to integers, include all decimal numbers (2.50, 5.99, -1.20)
length = 1876.79
width = 870.0

# It is important to keep in mind how the different numeric types can be mixed together and what the potential consequences are. If you mix different types, the most complex will be the one kept for the final result.

a = 7.5
b = 3
c = a/b
print(c)
# this will print 2.5, which is a float

a = 10
b = 5
c = a/b
print(c)
# it's a float

# you can force the conversion of a variable into a well-defined type

a = 14.0
# a is a float
a = int(a)
print(a)
# a is now an integer: it prints 14 and not 14.0

#Character Strings
city = 'New York'
film = 'taxi driver'
emptyString = ''

favoriteCityOne = "San Francisco"
favoriteCityTwo = "New York"
favorites = favoriteCityOne + favoriteCityTwo
print(favorites) # => "San FranciscoNew York"

favoriteCityOne = "San Francisco"
favoriteCityTwo = "New York"
favorites = "My favorite cities are " + favoriteCityOne + " and "+ favoriteCityTwo
print(favorites) # -> "My favorite cities are San Francisco and New York"

city = "Sydney"
numberTrips = 5
history = "I've been to " + city + " " + str(numberTrips) + " times "
print(history) # => "I've been to Sydney 5 times"

#Functions 
# Functions can group several statements in a block which will be called using a name. 
# Main purpose reuse a portion of code already written just by stating the function name 

# Examples
# len() :  a function that returns the length of an item. Do you remember strings? Using this function on a string tells you how many characters the string contains. 
# type() : lets you print the type of a variable.
# pow(a, b) : lets you calculate a to the power of b. It is equivalent to writing a**b.
# abs() :  returns the absolute value of a number.

a = "apple"
print(len(a))
print(type(a))
print(pow(4,2))
print(abs(-100))

#Write a function

def printPerimeter():
    dimension1 = 6
    dimension2 = 4
    dimension3 = 3
    perimeter = dimension1 + dimension2 + dimension3
    print(perimeter)

printPerimeter() # => 13

#Parameters 
# To overcome this limitation, you must make your function accept external numbers. You can do this by defining parameters.

def printPerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    print(perimeter)

printPerimeter(10, 11, 4) # => 25
printPerimeter(2, 2, 3.5) # => 7.5

# Parameters are variables declared in a function. The values that are passed as parameters are called arguments.

# Often, when you use a function in a code, you expect an answer that you can reuse to move forward in the code. This answer can be provided via the value returned by a function.

#Define a Return Value

def calculatePerimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    return perimeter

perimeter1 = calculatePerimeter(6, 4, 3)
perimeter2 = calculatePerimeter(10, 3, 11)

print("The perimeter of my first triangle is", perimeter1, "and that of my second is", perimeter2)

#Class & Objects

# In programming, this concept of a group or category of objects is called a class.
# A class can be considered as the construction diagram for an object that will define the characteristics of all objects of this type and their features.
# Let's take a concrete example with a Car class. The plan of a car can be defined by:
# its characteristics, called attributes: it must have four wheels, a color, a shape, an engine power, etc.
# its functionalities, called methods: it can drive, brake, etc.

var1 = 14
var2 = 1031

# In reality, you have created two instances of the int class, two objects each with a single attribute: its value. The same is true for floats or strings: every time you create a variable of one of these types, you are actually creating objects in Python with the value you assign to them as an attribute.
# The use of a method is always done via the   variableName.method()  notation. For example, strings have a method called   lower()  which will transform all the text contained in an object into lower case. 

a = "HELLO WORLD!"
a.lower()

#String Methods 
#upper() :  returns the whole text in upper case.
#capitalize() :  returns the whole text in lowercase with the first letter capitalized.
#replace(old, new) :  this method takes two arguments: old and new, both of which are strings.  The method returns the original string with all occurrences of old replaced with new. 
#find(string)  returns either the index of the first occurrence of the string passed in the  argument, or -1 if it does not find it.

text = "here os an EXAMPLE of a STRING"
a = text.upper()
print(a)
print(text.capitalize())
print(text.replace('EXAMPLE', "test"))
print(text.find('an'))
print(text.find('two'))

b = "This is A TEST"
print(b.capitalize())

a = 4 

def polynomial (a, b, c, x):
        return a*x**2 + b*x + c 
b = a 
b *= a
c = 1 
resul = polynomial(a, b, c, 0)
a +=3 
a = 0

print(a)
print(b)
print(c)

#Lists 
# Declare a List to Store Your Items

#Lists are objects that can contain a collection of objects of any type.  We can have a list containing several integers (1, 2, 50, 2,000 or more, it doesn't matter), a list containing floats, a list containing strings, or even a list mixing objects of different types.
#Lists are ordered objects - This number is called an index and it starts at 0 (not 1!). 

customerName = ['Marion Weaver', 'Alberto Mendoza', 'Katharine Tyler', 'Isaac Steele']

# assign the value 'Marianne Weaver' to the first name in our list
# it is index 0, because indices start at 0 in python!
customerName[0] = 'Marianne Weaver'
print(customerName[0])


#Python also lets you use negative indices to access or modify an item. The index -1 corresponds to the last item of the list, -2 to the second last, and so on. You can also access an index range by using the  :  operator. For example, 1:3 will let you access items two to four.
# print the last item
print(customerName[-1])

# access the second item to the 3rd
print(customerName[1:3])

# access all items from the beginning to the second
print(customerName[:2])

strangeList = [4, 10.2, 'Marion Weaver', ['another list', 1]]

# print the 4th item of the list
print(strangeList[3])

#Thanks to the different list methods, we can:

#search for a specific item in the list.
#add a new item at the end.
#insert a new item at a specific index.
#delete an item from the list.

list = []
list.append(7)
list.append(5)
print(list) # => [7, 5]

list = []
list.append(7) # -> [7]
list.append(5) # -> [7, 5]
list.insert(1,12) # [7, 12, 5]
list[0] = 4 # -> [4, 12, 5]
list.remove(12) # [4, 5]
list.index(5) # prints 1
list.extend([1, 2, 3]) # [4, 5, 1, 2, 3]
del list[3] # [4, 5, 1, 3]

# The   len()  function lets you retrieve the size of your list:
list = [1, 2, 3]
len(list) # will print 3

#Dictionaries
# Dictionaries are another type of object, similar to lists, but which will let you do this with a single variable! Indeed, a dictionary is a list of items organized via a system of keys. With a real dictionary, you look up a word to access its definition. In programming, this word corresponds to the key and the definition to the value associated with it. This is called a key-value pair. 
# Each key in a dictionary must be unique. Strings are generally used to define keys, but this is not a requirement, per se.

accounts = {'Marion Weaver': 10000, 'Alberto Mendoza': 150, 'Katharine Tyler': 300, 'Isaac Steele': 1800.74}
print(accounts['Alberto Mendoza']) # -> 150

#Here are the operations frequently carried out with dictionaries:
#Access the value of an item
#Add a new item (a new key-value pair)
#Delete an item via its key

accounts['Marion Weaver'] -= 2000 # I subtract 2000 from David's account
accounts['Kristian Roach'] = 1000 # I add a new individual in my dictionary
print(accounts['Kristian Roach']) # I print the value of Kristian's account

accounts.pop('Alberto Mendoza') # deletes Alberto Mendoza from our dictionary

#Len can be use to 
len(accounts) # -> 3

#Tuples

#The last type of collection we will look at are tuples. These are very similar to lists:
#They are ordered objects, so we can access the different items stored in a tuple from their index.
#You can store any kind of object in a tuple.
#The main difference is that once a tuple has been declared, it cannot be modified. It is then said that it is immutable.

my_tuple = (1, 2, 3, 'a', 'b')

print(my_tuple[1]) # -> 2
print(my_tuple[4]) # -> 'b'

a, b = (1, 'apple')
print(a) # -> 1
print(b) # -> 'apple'

# Conditional Structures
#IF -> Everything indented below the if is executed if the condition is true, otherwise the program runs everything indented below the else.

name = input( 'What is your name, dear stranger?')

if len(name) > 0:
    print("Hello", name, "!")
else:
    print("Hello, world!")

# In Python, the boolean can take the values True and False. Now see how to declare booleans in Python:
thisCourseIsGreat = True
itsAuthorIsVeryHumble = False

weather = "The weather is great!"
weather.startswith("The weather") # -> True

#Comparison Operators
#==  equal to (two values are exactly the same)
#!=  different from
#<  less than
#<=  less than or equal to
#>  greater than
#>=  greater than or equal to

2 == 2 # -> True
2 == 3 # -> False
4 != 4 # -> False
4!= 5 # -> True
1 < 2 # -> True
1 < 1 # -> False
1 <= 1 # -> True
3 > 4 # -> False
5 > 4 # -> True
5 >= 4 # -> True

age=15

if age>=21:
    # Do something if age is greater than or equal to 21

#Logical Operators
#These operators will let you mix several Boolean values: specific Boolean values or expression results. There are three of them:

#and : the AND operator.
#The final result is true only when all expressions/values are true. For example: the result of  expression1 and expression2  will be True only if   expression1  is true AND expression2  is also true.

#or : the OR operator.
#The final result is true when at least one of the expressions/values is true. For example: the result of  expression1  or  expression2   will be at True if   expression1  is true OR expression2  is true.

#not : the NOT operator.
#This simply reverses the result of the given expression. For example, the result of   not(expression)  is true when   expression  is false.

True and True # True
True and False # False
False and False # False
True or False # True
True or True # True
False or False # False
not(True) # False
not(False) # True

True and True and True # True
True and True and False # False
True or False or False # True
False or False or False # False

False or True and True # True
not(False) and True or False # True

(True and False) or True # True
not(True and False or not(True)) # True

#The  in  Operator
# Another useful logical operator in Python is the   in  operator. This returns   True  when a value is found in a sequence (a string or a list);  False , if not.

myList = [4, 2, 3, 2, 10]
myStringList = ["a", "b", "c", "d"]
myString = "The weather is really good today!"

4 in myList # True
0 in myList # False
0 in myStringList # False
"c" in myStringList # True
"e" in myStringList # False
"weather" in myString # True
"really" in myString # True
"rain?" in myString # False

# We could use two nested if statements, but Python can link several conditions thanks to the keyword   elif  (contraction of else and if). Here is the general form:

if condition1:
    # instructions
elif condition2:
    # instructions
else:
    # instructions

account = input("What is your account balance?")
account = int(account) # transform the answer into an integer

if account >= 10000:
    print("Loan granted!")
elif account >= 100 and account < 10000:
    print("Loan in process of validation: under study")
else:
    print("Loan refused")

#Loops 
# For loops are used when you know in advance how many times an action will be repeated.

myList = [7,2,4,10]

for i in myList:
    print(i)

myString = "Items"

for elt in myString:
    print(elt)

#To do this, you will use the   range(start, stop, step)  function, which will generate a collection of numbers according to three parameters:

#start : the first number of the sequence.

#stop  corresponds to the last number of the sequence, non-inclusive. The function will generate numbers from   start  to   stop-1.

#step :  the step between each generated number.

for i in range(0, 5, 1):
    print(i) # -> print from 0 to 4 by steps of 1 (end - 1)

for i in range(0, 5):
    print(i) # -> prints from 0 to 4 also (default step is 1)

for i in range(5):
    print(i) # -> prints from 0 to 4 also (default start is 0)

for i in range(0, 5, 2):
    print(i) # -> print 0, 2 then 4

#While 
#the while loop will run as long as a condition is met. It is a kind of combination of a for loop and an if structure. The number of repetitions is not defined in advance, but via a condition to be fulfilled, as with an if. This is called a conditional loop.#

while expressionLogic:
    # block to execute

numberTrees = 0

while numberTrees < 10:
    numberTrees += 1
    print("I planted", numberTrees, "trees")

print("I have a nice forest!")

# Skip Some Statements Within Your Loop

#For example, you want to repeat something 10 times, but skip (at least partially) when the value is 2 or 5. In Python, to force the start of the next loop iteration, use the keyword continue:

for i in range(10):
    # statements executed at each iteration
    print(i)
    if (i == 2) or (i == 5):
        print("Special case")
        continue
    # statements not executed if i == 2 or 5
    print("i != 2 & i != 5")

# You can also decide to interrupt the loop, for example when looking for a particular item in a list. For this, you will use the   break  keyword.

basket = ["apple", "orange", "banana"]

for fruit in basket:
    if fruit == "orange":
        print("I have an orange!")
        break

a = ['foo', 'bar', 'baz', 'qux', 'corge']
 
while a:
   if len(a) < 3:
      break
   print(a.pop())
print('Done.')

# Module
# A module is a Python file containing a set of predefined and operational functions, classes, and variables, which you can use as you wish in your code!
# Here is a simplified example of a geometry module:
'''
Module geometry.py
'''
# variables
pi = 3.14159265359
phi = 1.6180

# function that calculates the area
def area(obj):
    if type(obj) == square:
        return obj.a**2

# definitions of some classes
class square(object):
    def __init__(self,a):
        self.a = a

class triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

# To import a module, you will need the  import  keyword. Here is an example with our geometry module:
import geometry

squa = geometry.square(4)
tri = geometry.triangle(3, 6, 5)

print(geometry.pi) # -> 3.14159265359

geometry.area(squa) # -> 16

# All items included in the geometry module can be used via the   moduleName.  notation, i.e.,  moduleName.function()  or   moduleName.variable. So, in the above example, we can use  geometry.area()  or  geometry.pi. If you don't want to rewrite geometry every time, you have two other options:

import geometry as geo # we can now access geo.area() or geo.pi

#Or, import specific functions that you can then use as native Python functions/variables (without the  .  notation):

from geometry import pi
print(pi) # -> 3.14159265359

# A particular case of this last method is to import in one line all the objects contained in a module via the  *  notation.
from geometry import *

# A package (sometimes called a library) is a collection, a set of Python modules. As you have seen above, a module is a Python file. A package is simply a folder containing several Python files (.py) and an additional file named   __init__.py. This differentiates a package from an ordinary folder containing only Python codes.

# Packages in Data Analysis 
# Packages are ubiquitous in data analysis with Python. Indeed, many packages have been created specifically to address the issues that this subject involves. As you progress, you will be required to:
# manipulate your data to facilitate analysis.
# make various relevant graphs representing the behavior of your data.
# use statistical methods.
# run machine learning algorithms of varying complexity.

import numpy as np
np.sqrt(16) # -> 4.0