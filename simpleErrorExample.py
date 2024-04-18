# Simple error example

import sys

try:
    x = 1/0
except ZeroDivisionError:
    print("Error: Division by zero")
    sys.exit(1)
finally:
    print("This will always execute")

# If an error occurs, the program will exit