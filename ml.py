# # Encode + decode to build name
# name_upper = "".join(bytes([ord(ch)]).decode("utf-8") for ch in "LEANDRE")
# name_lower = "".join(bytes([ord(ch.lower())]).decode("utf-8") for ch in "LEANDRE")
#
# print(name_upper, name_lower)

def my_converter(x):
 return x * 0.3048

txt = f"A plane can be flying at {my_converter(3000)} meter altitude"

print(txt)