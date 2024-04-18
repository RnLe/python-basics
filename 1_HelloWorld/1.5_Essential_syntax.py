# Essential syntax

# Statements are usually single-line commands
print("abc")

# But python is capable of multi-line statements
print("abc",
      "def")

# It's also possible to execute multiple statements in one line (note the ; as separator)
a=1; b=2; c=3

print(a, b, c)

# Alternative
a, b, c = 4, 5, 6
# This is more common

print(a, b, c)

# Files can easily be created and written to using print (not even a module needed)
f = open("1.5_out.txt", "w")
print("Written to a file. Just like that.", file=f)
f.close()