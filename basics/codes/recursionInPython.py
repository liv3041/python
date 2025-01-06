""""
Recursion

- Factorial of any number is the product of all the integers from to that X number.
  Eg: The factorial of 5 = 1*2*3*4*5 = 120

  Why to use Recursion?
  - Follows DRY principle ie, do not repeat yourself.
  - Makes code cleaner and easy to read.
  - Break down bigger problems to small problems.
  - Makes sequence generation easier with nested iteration.


"""

def fact(x):
    if x ==1:
        return 1
    else:
        return (x * fact(x-1))
number = 9
print("Factorial of ",number, ": ", fact(number))