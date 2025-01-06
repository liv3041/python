"""
Syntax Errors:
- Parsing errors are known as syntax errors.
- Syntax recalls to trepass and prints the point where error is found.
- File/line number are printed where error has occured.

Eg: - ZeroDivisionError: (1/0) 
    - NameError 
    - TypeError - Eg: Trying to convert integer based data type to string 
    - ValueError. Eg : print(int("testValue"))

Exceptions:
- Even with correct code, errors do occur.
- Errors detected during excecution known as exceptions.
- During this time, the error can be resolved by referring to built-in exceptions.

Exception Handling:
- Code keeping few exceptions in mind.
- Used as decision makers (just like flow control)
- There are catch and throw mechanism.


Catch Mechanism:
- Catch: 
   ```
     try:
        #do something
        pass
     except ValueError:
        #Handle ValueError exception
        pass
    except(KeyError, MemoryError):
        # Handle multiple exception
        # Key Error and Memory Error
        pass
    except:
      # handle all other exceptions
      pass
      
    '''
        
- Multiple Catch:
    '''
        try:
           n1,n2 = eval(input("Input 2 numbers, Seperated by coma: "))
           ans = n1/n2
           print("Answer :", ans)
        except ZeroDivisionError:
            print("Division by Zero is Error!")
        except SyntaxError:
            print("Comma is missing. Enter Numbers seperated by comma. Eg: 5.6")
        except:
            print("Wrong Input")
        else:
            print("No Exception")
        finally:
           print("This will execute no matter what")
    '''
- Catch all:


"""

# try:
#     n1,n2 = eval(input("Input 2 numbers, Seperated by coma: "))
#     ans = n1/n2
#     print("Answer :", ans)
# except ZeroDivisionError:
#     print("Division by Zero is Error!")
# except SyntaxError:
#     print("Comma is missing. Enter Numbers seperated by comma. Eg: 5,6")
# except:
#     print("Wrong Input")
# else:
#     print("No Exception")
# finally:
#     print("This will execute no matter what")

""""
Exception Handling:
- Throw mechanism
- Rethrow mechanism
- Custom/ user-defined exceptions

Throw/ReThrow Mechanism
- Raise: It helps you forcefully call for any specefic exception.
- ReRaise: Exception was raised but don't intend to handle it.
            Raise statement helps to re-raise the exception 

"""
try:
  raise NameError("Hello World!")
except NameError:
  print("Exception Pop!!")

"""
Custom/User-Defined Exception:
- Custom exceptions can be described by initiating class.
- Errors should be derived from exception class.
- User-defined error can be called using raise syntax.

"""
class Error(Exception):
#  Base class of other exceptions.
 pass

class ValueTooSmallError(Error):
#   Raised when the input value is too small
    pass

class ValueTooLargeError(Error):
#   Raised when the inpt value is too large
    pass

# out main progrma


# Guess the number 
number = 10

while True:
   try:
      i_num = int(input("Enter a number : "))

      if i_num <number:
         raise ValueTooSmallError
      elif i_num > number:
         raise ValueTooLargeError
      break
   except ValueTooSmallError:
      print("This value is too small, try agin!")
      print()
   except ValueTooLargeError:
      print("This value is too large, try agin!")
      print()

print("Congratulations! you guessed the right number.")

