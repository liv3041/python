"""
List Comprehensions: Provide a concise way to create lists.


"""
# Create a list of squares from number 0 to 9

# Approch 1
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


# Approach 2
# While we are recreating this list squares the variable  x which still exists even after creation of the above list will be overridden.
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# Approach 3
squares = [x**2 for x in range(10)]
print(squares)

"""
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

[ (expression) for x in range(any_number) if (certain_condition) ]
"""

# Print all the pairs in [1,2,3] and [3,1,4] where x is not equal to y.

# Approach 1: List Comprehension
list_var = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(list_var)

# Approach 2: Intutive way to solve and print tuple.

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))

print(combs)
"""
In the above approach the list that will be printed will contain a tuple or a pair?

The parentheses () is used to create both tuple and pair. The only differnce they both have of
is size. A pair has exactly two elements. A tuple is a broader term for immutable collections of any size.

Note: A tuple can be a pair but a pair cannot be a tuple.

"""
list_var = [-4,-2,0,2,4]
print(list_var)

# make the value of elements in the above list double.
modified_list = [x*2 for x in list_var]
print(modified_list)

# create a seperate list for the elements with positive value.
positive_list = [x for x in list_var if x>=0]
print(positive_list)

# apply a function to all the elements
list_var = [abs(x) for x in list_var]
print(list_var)

freshfruit = [' banana',' loganberry','passion fruit ']
freshfruit_without_space = [weapon.strip() for weapon in freshfruit]
print(freshfruit_without_space)

# create a list of 2-tuple or a pair like (number, square of the number)
list_of_tuples = [(x, x**2) for x in range(6)]
print(list_of_tuples)

# flatten the below nested list.
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
unwrapped_nested_list = [num for elem in nested_list for num in elem]
print(unwrapped_nested_list)


# Print the list with elements as pi in the form of string, rounding off the decimal of any element list[i] up to the variable i where i = 1,2...n
from math import pi

pi_list = [str(round(pi,i))for i in range(1,7)]
print(pi_list)

# Nested List Comprehension
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# Transpose the above matrix such that rows = columns and columns equals rows


# Approach 1:

transposed_matrix = []
for i in range(4):
     transposed_row = []
     for row in matrix:
          transposed_row.append(row[i])
     transposed_matrix.append(transposed_row)

print(transposed_matrix)

# Approach 2:
transposed_matrix = []
for i in range(4):
        transposed_matrix.append([row[i]for row in matrix])
 
print(transposed_matrix)




# Approach 3:

transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix)

# Approach 4:
transposed_matrix = [list(row) for row in zip(*matrix)]
print(transposed_matrix)

# Approach 5: 
transposed_matrix = list(zip(*matrix))
print(transposed_matrix)

"""
del statement: use to remove an item from the list or to empty the list.
"""
books_to_be_read = ['The Yellow face','The Hitchhiking Galaxy','The Alchemist','Percy Jackson','Harry Potter','Emma']
print(books_to_be_read)

del books_to_be_read[0]
print(books_to_be_read)

del books_to_be_read[2:4]
print(books_to_be_read)

del books_to_be_read[:]
print(books_to_be_read)