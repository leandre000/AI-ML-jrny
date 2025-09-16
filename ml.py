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

age = 18
message = f"You are {'eligible' if age >= 18 else 'not eligibile'} to vote."
print(message)