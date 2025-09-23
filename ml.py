#
# thislist = ["apple", "banana", "cherry"]
# # thislist[1] = "blackcurrant"
# thislist[1:2] = "blackcurrant"
#
# print(thislist)
#
#

# original_list = ["Leandre", "Emma", "Liam"]
# new_list = ["Olivia", "Lucas"]
#
# original_list[1:1] = new_list
#
# print(original_list)


# thislist = ["apple","banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
#
#
# thistuple = ("kiwi", "mango")
#
#
# thislist.extend(list(thistuple))
# print(thislist)
#
#
# merged = thislist + list(thistuple)
# print(merged)
#
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist.remove("banana")
# print(thislist)

# fruits = ["apple", "banana", "cherry",1,2,4]
#
# removed = fruits.pop()
# print("Removed:", removed)
# print(fruits)
#

# fruits = ["apple", "banana", "cherry"]
#
# fruits.clear()       # removes everything
# print(fruits)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana", "indimu", "amapera", "peas"]
# thislist.sort(key=str.lower)
#
#
# reversed_items = [item[::-1] for item in thislist]
#
# print(reversed_items)


fruits = ["Apple", "Banana", "Cherry", "Date", "Elderbelly", "fig", "Grape"]

fruits.sort(key=str.lower)
reversed_list = [item[::-1] for item in fruits]

print(reversed_list)
