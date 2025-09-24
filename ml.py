def simple_function(x, y=[0]):
    y.append(x)
    return y
result1 = simple_function(1)
result2 = simple_function(2, [3])
result3 = simple_function(4)

print(result1)
print(result2)
print(result3)
