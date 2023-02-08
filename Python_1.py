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

