# Custom error example
class MyError(Exception):
    """A custom exception class for specific errors."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

def divide(a, b):
    if b == 0:
        raise MyError("You cannot divide by zero!", code=400)
    return a / b

try:
    result = divide(10, 0)
except MyError as error:
    print(f"Error occurred: {error}")
    print(f"Error code: {error.code}")