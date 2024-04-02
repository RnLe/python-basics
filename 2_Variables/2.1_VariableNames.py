# Variable names can start with a letter or an underscore "_"
# Using leading underscores is not recommended as it conflicts with python-internal variable names

# Okay
a = 1
b = "abc"
a = a + 1

# Error
a = c + 1  # c isn't declared

# Special characters and case sensitivity
aLongName = 3
a_long_name = 4
unüblich = 5 # Okay, but uncommon

# Not okay
no spaces allowed = 5
this-doesnt-work-either = 6