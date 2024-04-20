# Python's primitive data types are classes
x = 2
print(type(x))

x = 2.0
print(type(x))

x = {1, 2, 3}
print(type(x))

# A variable name doesn't have a type. Instead, it points to an object (e.g. of the class int, float, set, etc.).
# Check what type the object is the variable is pointing to
c = "abc"
isinstance(c, str)  # True
isinstance(c, int)  # False

# Type annotations
msg: str = "example string"
s: str
i: int = 3

# Type annotations are only a recommendation and aim to improve code readability.
# However, python doesn't check these annotations and variables can change their type despite being annotated.
s = 5   # This is valid