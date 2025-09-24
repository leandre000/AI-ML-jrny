def simple_function(x, y=None):
    if y is None:
        y = []
    return y
result1 = simple_function(1)
result2 = simple_function(2, [])
result3 = simple_function(3)

print(result1)
print(result2)
print(result3)
