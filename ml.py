# a = [1, 2, 3]
# b = a.copy() # make the snapshot for this time first but a = b involves use of the same memory
# b[0] = 100
# print(b)
# print(a)
#
# def func (a):
#     return a * 2
# result = func([1, 2, 3]) + func([4, 5, 6])
# print(result)
#
# for i in [0,1,2]:
#     print(i, end=" ")
# print(i)
#
# s = "Hello"
# s += " World"
# print(s)
#
# def add (a, b=5):
#     return a + b
# print(add(10))
#
# x = [1, 2, 3]
# y = x.copy()
# y.append(4)
# print(len(x))
#
# num = 10
# while num > 0:
#     num -= 2
# print(num)
#
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a & b)
#
# x = [1, 2, 3]
# x.insert(0,0)
# print(x)
#
# def test ():
#     return [x for x in range(5)]
# result = test()
# print(type(result))
# print(result)
#
# a = 10
#
#
# # Practice
# strings = ["Name", "fullname"]
# s = "Hello"
# #
# # s *= " World"
# print(s)
#
# # Function default values
# def add (a, b=[]):
#     b.append(a)
#     return b
# result1 = (add(10, [20]))
# print(result1)
#
# result2 = add(5)
# print(result2)

def simple_function(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return y

result1 = simple_function(1)
result2 = simple_function(2, [])
result3 = simple_function(3)

print(result1)
print(result2)
print(result3)
