"""
List Concatenation:
Create a function that takes two lists as input and returns a new list that is the concatenation of the two input lists. For example, if the input lists are [1, 2, 3] and [4, 5, 6], the output should be [1, 2, 3, 4, 5, 6].
"""

# function signature

def two_list(lst1=None, lst2=None):
    if lst1 is None or not isinstance(lst1, list):
        raise ValueError("Input must be a list")
    
    if lst2 is None or not isinstance(lst2, list):
        raise ValueError("Input must be a list")
    
    result = lst1 + lst2
    return result

try:
    # concatnate = two_list([1,2,3,4,5], [6,7,8,9,10])
    concatnate = two_list([1,2,3,4,5], ["efawf"])
    print(concatnate)
except ValueError as ve:
    print(f"Error: {ve}")
