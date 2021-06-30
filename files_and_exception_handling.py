# print(1/0) # ZeroDivisionError
#
# num = 9
# if num > 8 # SyntaxError
#     print(num)
#
# # We will create a file with required permission and see what errors/exception are possible to be seen
# # First iteration
# file = open("order.txt") # open() takes a string arg with file name
# print(file) # Let's see the outcome and record it
#
# # Second iteration
# try:
#     file = open("order.txt")
#     print("File found") # `try` block required except or will throw and error
# except FileNotFoundError as errmsg: # creating alias same as nick name
#     print(f"File not found: {errmsg}")
# finally: # `finally` will execute regardless of `try` and `except` block execution, also used to clean up code
#     print("Thank you for visiting! See you again!")
#
# # Let's create a file called order.txt - naming is essential so ensure it has the same name as above
#
# Let's apply; 1) DRY - 2) OOP - 3) Python packaging
#
# Continued in `program.py` to keep things tidy!