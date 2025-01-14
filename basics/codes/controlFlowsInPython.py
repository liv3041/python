
# While Statement
# Fibonacci Series
a, b = 0,1
while a < 10:
    print(a,end=',')
    a,b = b, a+b
# In the above statement, first the rhs is evaluated then assigned to lhs. rhs is evaluated from left to right.
print("\n")
# if Statement
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative canged to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

""""
for statement

The for statement in python iterates over the items of any sequence be it a list or a string. In the order they appear in the sequence.
"""
print("\n")
rgb  = ["Red","Green","Blue"]
for colors in rgb:
    print(colors, end= ",")
print("\n")
# If we have to add "Ranger" to every element in the list rgb
for color in rgb:
    print(color + "Ranger",end=" , ")
 
#   Here in the above statement we are only printing elements of rgb by adding "Rangers" with every element.
print("\n")
print(rgb)

# Suppose we want to have the modified elements with "Ranger" in the list rgb
list = []
for color in rgb:
    list.append(color + " Ranger")

print("\n")
print(list)

# Now suppose we want to make ony "Red" color a ranger.

list = []
for color in rgb:
    if color == "Red":
        list.append(color + " Ranger")
    else:
        list.append(color)
print(list)

# Sample Collection 
users = {"Arthur Dent":"active","Ford Prefect":"active","Guy with bulldozer":"inactive"}
print("\n")
print(users)

# The below for loop will delete any element whose status is inactive
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print("\n")
print(users)

# Append all the user for whicb the status is 'active' in to the  active_users dictionary.
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# The range function in python works like [a,b) 
for i in range(5):
    print(i,end=',')
# range(5) = range(0,5) or mathematically [0,5)

qualities = ['kind','compassinate','patience','courage','brave']

# Two ways to iterate the list qualities:
# 1st approach
for q in range(len(qualities)):
    print(q,qualities[q])

# 2nd approach
i = 0
for q in qualities:
    print(i, q)
    i= i+1

print(sum(range(4)))
print(range(4))

# Break statement:Breaks out of the any loop

# The below loop will work for i = 4,6,8,9 and j = 2,2,2,3

for i in range (2,10):
    for j in range(2,i):
        if i%j == 0:
            print(f"{i} equals {j} * {i // j}")
            break

# continue statement : Any statement below the contniue statement will be skipped and the loop will go on

for num in range(2,10):
    if num %2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

""""
else clause in conditional statement executes when if clause is false


else clause in loop: 
- Is executed when the loop finishes without any interruption.
- If the loop is finished before  the loop is terminated by break, return or raise then else clause will be executed.

else clause in loop and else clause in try statement works more or less in the same way

"""
# The below if-statement inside the  j-loop will work for i = 4,6,8,9 and j = 2,2,2,3
# else clause will work for i = 2,3,4,7 ie, for all the i which didnt go inside the if-statment inside the j-loop.
for i in range(2,10):
    for j in range(2,i):
        if i%j == 0:
            print(i, 'equals',j,'*',i//j)
            break
    else:
        print(i,'is a prime number')

# pass statement: does nothing and can be used as a placeholder for any function, class, loop or conditional statement while working on the new code.
# while True:
#     pass
# The above loop is an infinite loop.
class MyEmptyClass:
    pass

def initlog(*args):
    pass

# Functions
def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end='')
        a,b = b,a+b
    print()

fib(2000)

def fib2(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result

f100 = fib2(100)
f100

def ask_ok(prompt,retries =4, remainder = 'Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y','ye','yes'}:
            return True
        if reply in {'n','no','nop','nop'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError ('invalid user response')
        print(remainder)


i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def parrot(voltage,state='a stiff',action='voom',type = 'Noorwegian Blue'):
    print("--The parrot wouldn't",action,end='')
    print("if you put", voltage, 'volts through it.')
    print("-- Lovely plumage the", type)
    print("-- It's", state, "!")

# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1000000, action='VOOOM')
# parrot(action='VOOOMM',voltage=10000000)
# parrot('a million', 'bereft of life','jump')
# parrot('a thousand', state='pushing up the daisies')


"""" Invaild Arguments"""
# parrot() required argument missing
# parrot(voltage=5.0,"dead") non-keyword argumetn after a keyword argument
# parrot(110,voltage=220) duplicate value for the same argument
# parrot(actor = 'Jhon') Unknown keyword argument

# def function(a):
#     pass

# function(0)


# **keywords => is a final formal parameter that recieves dictionary
# *arguments => is a formal parameter that recieves tuple.
def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind,"?")
    print("--I'm sorry, we're all out of",kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])

cheeseshop("Limburger","It's very runny, sir.",
"It's really very, ERY runny, sir.",
shopkeeper = "Nobita Nobi",
client = "Doraemon",
dessert = "Doracake")

# The order in which the keyword arguments are printed is guranteed to match
# the order in which they were provided in the function call.

def standard_arg(arg):
    print(arg)

standard_arg(2)
standard_arg(arg=2)

def pos_only_arg(arg,/):
    print(arg)

pos_only_arg(1)
# pos_only_arg(arg = 3) will throw an error

def kwd_only_arg(*,arg):
    print(arg)

# kwd_only_arg(3) will throw an error
kwd_only_arg(arg=3)

def combined_example(pos_only,/, standard, *,kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1,2,3) will throw an error
combined_example(1,2,kwd_only=3)
combined_example(1,standard=2,kwd_only=3)

def foo(name,/, **kwds):
    return 'name' in kwds

print(foo(1,**{'name':2}))

def concat(*args,sep="/"):
    return sep.join(args)

print(concat("earth",'mars',"venus"))
print(concat("earth",'mars',"venus",sep="."))

def parrot(voltage,state="a stiff",action="voom"):
    print("--The parrot wouldn't", action, end=' ')
    print("If you put", voltage, "volts through it.", end= ' ')
    print("E's", state, "!")

d = {"voltage":"four million","state":"bleedin' demised", "action":"VOOM"}
parrot(**d)

# Lambda Expressions:
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
f(0)
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
pairs

""""
Annotations: Annotations are stored in _annotations_ attribute of the function as a dictionary and have no effect
             on any other part of the function. Parameter annotations are defined by a colon after a parameter name,
             followed by an expression evaluating to the value of the annotation.
"""
def f(ham:str,eggs:str='eggs')->str:
    print("Annotations:",f.__annotations__)
    print("Arguments:",ham,eggs)
    return ham + ' and ' + eggs

f('spam')