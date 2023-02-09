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
