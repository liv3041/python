
""""
String:
A string is a textual data or a sequence of characters used to represent text.

String Literal:
A fixed sequence of characters (emaphasis on fixed) directly defined in code that remains
constant all the while.

Literal String Expressions:
1. Start and end with quote marks.
2. Contain the text between the quote marks.
3. Can use single quote or double quote marks as delimiters, but not both on the
   same string.




"""
 
""" *******************************************************************************************"""
# strings enclosed in single quotes or double quotes are the same.
print("2025 is coming.")
print('Only 1 hour left for 2025.')

""" *******************************************************************************************"""

# to quote a quote we use backslash + quotation mark (\' or \")
print("ain\'t") 
print("\"Hurray!\"")
""" *******************************************************************************************"""

# For new line
print("This is an absurd statement.\nWith no meaning.")

""""
If you don't want characters prefaced by \ to be interpreted as special
characters, you can use raw strings 'r' before the first quote.
"""
print('This\is\an\absurd\planet.')
print(r'This\is\an\absurd\planet.')
print('This\nis\nan\nabsurd\nplanet.')
print(r'This\is\an\absurd\planet.')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

""""
 String literals can span multiple lines by using triple quotes ''' ''' or """" """"
 To avoid adding a newline one can use back slash character.
"""
""" *******************************************************************************************"""
# Strings can be concatenated by  + operator and repeated with * operator
print(3 * 'Guten Nacht!  tuschuss 2024: \n' + "2025 kommt")

# Two string literals next to each other are automatically concatenated.
print("Py" "thon")
text = "This is an absurd planet. " "A planet of randomeness and grief."
print(text)
text = 'This is an absurd planet. ' 'A planet of randomeness and grief.'
print(text)

# Below statement will not work as we cannot concatenate a string literal with variable
# print(text "Humans and Animals are Mammals.")

""""
Use plus sign (+) to concatenate:
1. variable and string literal
2. string literal and string literal
3. variable and variable
"""
print(text+"Humans and Animals are Mammals.")



# Strings can be indexed. We can access characters in string like arrays.For Example:
word = "Are you afraid of spiders? Then what about spiderman?"
word = "Python"
print(word[2] + word[4] + word[0])
# -1 represents last character in our string and -2 represents second last characters in our string.
print(word[-1]+word[-2])

# Indexing : is used to obtain individual characters.
# Slicing: is used to obtain  substring within a string.

print(word[0:7]) # characters from position 0 (included) to 7 (excluded)
print(word[3:7]) # characters from position 3 (included) to 7 (excluded)
print(word[:-1]) #characters form beginning to the last character(excluded)
print(word[0:]) # characters from beginning to the end
print(word[:])  # characters from beginning to the end
print(word[-2:])

""""

String slicing is easier if we can imagine the strings with index.

        +---+---+---+---+---+---+
        | P | y | t | h | o | n |
        +---+---+---+---+---+---+
        0   1   2   3   4   5   6
       -6  -5  -4  -3  -2  -1

"""
#  Below statement will give an error because the string is of length 6.
print(len(word))
# print(word[42])

# All the below statement will be executed
print(word[4:42]) # on
print(word[42:])  # " "
print(word[:42]) # Python

# Python string are immutable and cannot be reassigned while indexing.
# word[2] = "u"
print(word)

word = "Boar"
print(word)
