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

# txt1 = "My name is {fname}, I'm {age}".format(fname ="John", age=36)
# txt2 = "My name is {0}, I'm {1}".format("John", 36)
# txt3 = "Muy name is {}, I'm {}".format("John",36)
#
# txt = "The universe is {:,} years old.".format(1380000000000)
# print(txt)

# String for testing
# name = "Mugisha"
# space_text = "   Mugisha   "   # with spaces for strip examples
# num_text = "123"               # numeric string
# mixed_text = "Mugisha123"      # letters + numbers
#
# #isalpha() → checks if all characters are alphabets
# print(name.isalpha())      # True
# print(mixed_text.isalpha()) # False
#
# #isdecimal() → checks if all characters are decimal digits
# print(num_text.isdecimal()) # True
# print(name.isdecimal())     # False
#
# #isdigit() → checks if all characters are digits
# print(num_text.isdigit())   # True
# print(name.isdigit())       # False
#
# #isnumeric() → checks if all characters are numeric (digits, fractions, Roman numerals, etc.)
# print(num_text.isnumeric()) # True
# print(name.isnumeric())     # False
#
# #lower() → converts all characters to lowercase
# print(name.lower())   # "mugisha"
#
# #islower() → checks if all characters are lowercase
# print(name.lower().islower()) # True
# print(name.islower())         # False
#
# #upper() → converts all characters to uppercase
# print(name.upper())   # "MUGISHA"
#
# #isupper() → checks if all characters are uppercase
# print(name.upper().isupper()) # True
# print(name.isupper())         # False
#
# #swapcase() → swaps uppercase to lowercase and vice versa
# print(name.swapcase())  # "mUGISHA"
#
# #isspace() → checks if string contains ONLY whitespace
# print("   ".isspace())   # True
# print(name.isspace())    # False
#
# #strip() → removes spaces from BOTH sides
# print(space_text.strip())   # "Mugisha"
#
# #lstrip() → removes spaces from the LEFT side
# print(space_text.lstrip())  # "Mugisha   "
#
# #rstrip() → removes spaces from the RIGHT side
# print(space_text.rstrip())  # "   Mugisha"
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # True
print(x is y)   # False
print(x == y)   # True

