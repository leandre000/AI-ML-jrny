# # Encode + decode to build name
# name_upper = "".join(bytes([ord(ch)]).decode("utf-8") for ch in "LEANDRE")
# name_lower = "".join(bytes([ord(ch.lower())]).decode("utf-8") for ch in "LEANDRE")
#
# print(name_upper, name_lower)

# def my_converter(x):
#  return x * 0.3048
#
# txt = f"A plane can be flying at {my_converter(3000)} meter altitude"
# print(txt)

# num1 = 10
# num2 = 5
# result = f"The sum of {num1} and {num2} is {num1+num2}"
#
# print(result)

#
# price= 2000000.1987
# formatted_price = f"The price is ${price:,.2f}"
# print(formatted_price)

#

txt1 = "My name is {fname}, I'm {age}".format(fname ="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "Muy name is {}, I'm {}".format("John",36)

txt = "The universe is {:,} years old.".format(1380000000000)
print(txt)