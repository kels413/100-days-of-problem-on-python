"""
List Filtering:
Create a function that takes a list of numbers and returns a new list containing only the even numbers from the original list.
"""

def even_list(lst=None):
    if lst is None or not isinstance(lst, list):
        raise ValueError("Input must be a list")
    
    even_lst = []

    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst

try:
    content = even_list([1,2,3,4,5,6,7,8,9,10])
    # content = even_list("devae")
    print(content)
except ValueError as ve:
    print(f"Error: {ve}")


# case to check later
    # a case where the user should input a string in
    # between the list or any datatype that is not integer