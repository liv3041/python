

squares = [1,2,3,4,5]

# Like strings lists can be indexed and sliced.
print(squares[0])
print(squares[3])
print(squares[3:])
print(squares[-3:])

# Supports concatenation of other list.
squares = squares + [2,4,5,6,7,8]
print(squares)

# Strings are immutable but lists are mutable.
squares[1] = 90
print(squares)

# New elements in the list can be appended through append method or through concatenation.
squares.append(23)
print(squares)

squares = squares + [23]
print(squares)

print(squares[12])

print(len(squares))


# print(squares[len(squares)]) = 23 , this statement will generate an indexerror.


# The variable 'rgb' does not copy list ["Red","Green","Blue"] but refers to it.
rgb = ["Red","Green","Blue"]
# When I am assigning rgb to the variable rgba then both of them is referring to the same list ["Red","Blue","Green"]
rgba = rgb
print(rgb)
print(rgba)

print(id(rgb)==id(rgba))

# Since, rgb and rgba refers to the same list. Any changes done in the list using rgb as reference will also reflect in rgba
rgba.append("Pink")
print(rgb)


""""
Question 1: How can I make every color a ranger , by adding the string "Ranger" at the end of every element in the list?

Approach: 
Make rgb[0] which is now "Red" to rgb[0] = "Red Ranger". Suppose we have done that.
        Now our list is [ "Red Ranger", "Green","Blue"]
Now we have to make rgb[1] which is now "Green" to "Green Ranger". Suppose we have done that too.
        Now our list is ["Red Ranger", "Green Ranger","Blue"]
At last we have to make blue color now a ranger ie, we have to make rgb[2] which is now "Blue" a to rgb[2] = "Blue Ranger"
    Now our list will be ["Red Ranger", "Green Ranger","Blue Ranger"].

Basically we started from index 0, which is starting of the list and went to index = len(rgb) at the end of the list and concated
ranger.

Now we just have to think of all the tools in python that will help us to achieve this approach and hence solve this problem. Similar to but not limited in the same format.
Eg: for loop, map(), pandas, numpy,itertools

Question 2: How to make a specific color a "Ranger"? Lets say we want to make only red color a ranger in the list.

Approach:
If we want to make specific color a ranger first we identify that color in the list and then make it a ranger.
To identify the color in the list is simple for us human but a difficult for the Python Interpreter who executes every code line by line. We can also 
say that it thinks line by line with no memory of its own. So, we have to make it think correctly.

For any index i  where i = 1 to len(rgb) if(rgb[i]=="Red") then rgb[i] += "Ranger" else we do nothing

Simply the above statement means that we will iterate form index 0 to len(rgb) which is generalised as index i and find if the element or string that equals to "Red". If yes then concatenate "Ranger" If not then do nothing.

"""



# Manipulating lists through slices.

letters  = ['a','b','c','d','e','f','g']
print(letters)

print(letters[2:5])
letters[2:5] = ['C','D','E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

# Nested List - Works like a matrix
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g']

letters = [vowels,consonants]
print(letters)
# Will print vowels
print(letters[0])
# Will print consonants
print(letters[1])
# will print 'a' in the vowels.
print(letters[0][0])