
def append_example():

    names = ["Leandre", "Emma", "Liam"]
    names.append("Olivia")
    print(names)

def clear_example():

    names = ["Leandre", "Emma", "Liam"]
    names.clear()
    print(names)

def copy_example():

    names = ["Leandre", "Emma", "Liam"]
    new_names = names.copy()
    print(new_names)

def count_example():
    names = ["Leandre", "Emma", "Liam", "Leandre"]
    count = names.count("Leandre")
    print(count)

def extend_example():
   
    names = ["Leandre", "Emma", "Liam"]
    more_names = ["Olivia", "Lucas"]
    names.extend(more_names)
    print(names)  # Output: ['Leandre', 'Emma', 'Liam', 'Olivia', 'Lucas']

def index_example():
    """
    Example of using the `index()` method to find the index of an element in a list.
    """
    names = ["Leandre", "Emma", "Liam"]
    index = names.index("Liam")
    print(index)  # Output: 2

def insert_example():
    """
    Example of using the `insert()` method to add an element at a specific position in a list.
    """
    names = ["Leandre", "Emma", "Liam"]
    names.insert(1, "Olivia")
    print(names)  # Output: ['Leandre', 'Olivia', 'Emma', 'Liam']

def pop_example():
    """
    Example of using the `pop()` method to remove and return an element from a list.
    """
    names = ["Leandre", "Emma", "Liam"]
    removed_name = names.pop(1)
    print(names)  # Output: ['Leandre', 'Liam']
    print(removed_name)  # Output: Emma

def remove_example():
    """
    Example of using the `remove()` method to remove the first occurrence of an element from a list.
    """
    names = ["Leandre", "Emma", "Liam", "Leandre"]
    names.remove("Leandre")
    print(names)  # Output: ['Emma', 'Liam', 'Leandre']

def reverse_example():
    """
    Example of using the `reverse()` method to reverse the order of elements in a list.
    """
    names = ["Leandre", "Emma", "Liam"]
    names.reverse()
    print(names)  # Output: ['Liam', 'Emma', 'Leandre']

def sort_example():
    """
    Example of using the `sort()` method to sort the elements in a list.
    """
    names = ["Leandre", "Emma", "Liam"]
    names.sort()
    print(names)  # Output: ['Emma', 'Liam', 'Leandre']

# Call all the example functions
append_example()
clear_example()
copy_example()
count_example()
extend_example()
index_example()
insert_example()
pop_example()
remove_example()
reverse_example()
sort_example()
