from memory_profiler import profile

@profile
def build_array_gen(n):
    for i in range(n):
        yield i
       
@profile 
def build_array(n):
    return [i for i in range(n)]


toBuild = 1000000

a = list(build_array_gen(toBuild))
b = build_array(toBuild)
c = []

print(f"Length of a: {len(a)}")
print(f"Length of b: {len(b)}")
print(f"Length of c: {len(c)}")
print(f"Memory of a: {a.__sizeof__()}")
print(f"Memory of b: {b.__sizeof__()}")
print(f"Memory of c: {c.__sizeof__()}")