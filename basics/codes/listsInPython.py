

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

# add an item at the end of the list
squares[len(squares):] = [25]
print(squares)

# Insert an item at any given position
squares.insert(2,30)
print(squares)
# print(squares[len(squares)]) = 23 , this statement will generate an indexerror.

# Remove first item from the list whose value is equal to x.
squares.remove(25)
print(squares)

# Raises value error if given any value not present in the list
# squares.remove(89)

# Removes the value of the  9th index from the list squares.

squares.pop(9)
print(squares)

#  If index is not specified then removes and returns the last item in the list.
squares.pop()
print(squares)

# raises indexerror if the list is empty or if the index is out of bound.
# squares.pop(25)


# Reverses the list
squares.reverse()
print(squares)

# returns the index of 23 present between (inclusively: [0,8]) the list of subsequence, index 0 and index 8
print(squares.index(23, 0,8))

# Modifies the orginal list into ascending order
squares.sort()
print(squares)

# Modifies the original list into descending order
squares.sort(reverse=True)
print(squares)
# returns how many times 4 has appeared in the list.
print(squares.count(4))

# Removes all the items from the list.
squares.clear()
print(squares)

squares = [45,78,45]

print(squares[:])
print(squares.copy())
# removes all element from the list
del squares[:]
print(squares)

# Sorts without modifying the  original list.
squares = [16, 4, 1, 9]
sorted_squares = sorted(squares)
print(sorted_squares)  # Output: [1, 4, 9, 16]
print(squares)  # Original list remains unchanged: [16, 4, 1, 9]


# Methods like sort, insert and remove have no return type and will return none if printed
print(squares.sort())

# A multitype list cannot be sorted or compared. This will give an type error.
list = ['apple',34,89.99]
# list.sort()

print("-"*70)

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
print("-"*70 )



""""
Using list as a stack:

Functionality of a stack is:= (LIFO) Last in First out.
Suppose there is a stack of plates we are washing, and we are stacking up the plate on the top of one another.
So, the first plate we have washed will come first and then the second plate we have washed will come on the top of first, like this we will have n no of plates on the top of one another in a form of a stack.
If I want to take out a plate to serve a dish I will first take out the nth plate then the nth-1 plate till 1 or 0 depending upon index.

From above scenario:
 while stacking the plates we kept plate as : 1,2,3,4.....n
 while de-stacking the plates we went as n, n-1 , n-2,n-3, n-4......1

Now if we want to make list behave as stack then, the items of the list should be appended at the last and if we want to remove an element or access an element then it should also be done from the last index.




"""

stack = [3,4,5]
# adds element at the last index
stack.append(6)
stack.append(7)
print(stack)
# removes the element at the last index.
stack.pop()
print(stack)

""""
List as queue: FIFO, First in First out.

Just like any normal queue. Suppose there is 1,2,3...n lined up in a queue in the fashion
enqueue(1),enqueue(2),enqueue(3),...enqueue(n), item in the queue is always appended beside the next element.

Here, the queue will be dissolved in the same fashion dequeue(1),dequeue(2),dequeue(3)....dequeue(n) this can happen if 
1. I shift the index pointer when ever the element is dequeued so that the head will point to other element or 
2. if I shift the queue it self and always remove the 0th or 1st index.

The only difference between the approach 1 and 2 is the time complexity.
First will happen in  O(1) time and the second will happen in O(n) time.
Why so?

In first approach we are shifting and pointer variable as the list is dequeueing.

 
In the second approach we are shifting the list it self of size let say m.
Here the list is doind two work:
a. popping the 0th index.
b. again enqueuing all the elements into the list from 1 index. i.e shifting all the elements inside the list from 1 index.


"""

# first approach
from collections import deque

queue = deque()  # Initialize an empty deque

# Enqueue (add) elements
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])

# Dequeue (remove) elements
first_element = queue.popleft()  # Removes the first element
print(first_element)  # Output: 1
print(queue)  # Output: deque([2, 3])


print("-"*67)

# second approach
queue = []  

# Enqueue (add) elements
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  

# Dequeue (remove) elements
first_element = queue.pop(0)  # Removes the first element
print(first_element)  
print(queue)  
