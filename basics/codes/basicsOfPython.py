
""""
 Boolean Operations- and, or, not

 These are the Boolean operations, ordered by ascending priority:
  1. x or y := 
     if x is true, then x, else y. 
     This  is a short circuit operator, so it only evaluates the second argument if the first one is false.
  2. x and y := 
     if x is false, then x, else y.
     This is a shor circuit operator, so it only evaluates if the first argument is true.
  
  3. not x := if x is false, then True, else False. not has a lower priority than non-Boolean operators, so not a == b is 
     interpreted as not(a == b), and  a == not b is a syntax error.
    

"""

x = True
y = False
print(x or y)

x = 4
y = 20
# checks if x is true. If yes will return true.
print(x == 4 or y == 20)
# checks if x is true. If not then will check for y. If is true then will return true.
print(x == 30 or y == 20)

print(x == 30 or y == 30) #false

print("*******************************")
print(x == 4 and y == 20) #true
print(x == 4 and y == 30) #false
