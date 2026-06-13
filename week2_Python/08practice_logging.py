# Exercises 2.8
# Ask the user for a number with input() and print its square; letters must print "not a number", not crash.
# try:
#     num =int (input("Please enter  a number"))
#     print(f" Square of that number is : {num*num}")
# except ValueError:
#     print("not a number")


# Loop over ['5','12','x','7','']: collect successes, count failures.
# good=[]
# bad=0 #counter
# for value in ['5','12','x','7','']:
#     try :
#         good.append(int(value))
#     except ValueError:
#         bad+=1
# print(good)
# print("failures :",bad)

# Open a filename from a variable; if missing, create it containing "created fresh".
# filename = "missing.txt"
# try :
#     with open(filename,"r") as f:
#         data=f.read()
#         print("File found! Reading data...")
# except FileNotFoundError:
#     print(f"File not found. Creating {filename}...")
#     with open(filename, "w") as f:
#         f.write("created fresh")
# except Exception as e :
#     print("Unexpected error",e)
# finally:
#     pass


# Write safe_divide(a, b) that returns None on division by zero and logs a warning.

import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s%(levelname)s%(message)s")
def safe_divide(a, b):
    if b ==0:
        logging.error("❌❌❌Waring!! its a zero")
        return None
    result = a/b 
    return result
# Let's test it:
# print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: None (and logs the warning!)