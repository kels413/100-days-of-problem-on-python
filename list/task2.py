"""
List Reversal:
Write a program that reverses a given list. For example, if the input is [1, 2, 3, 4], the output should be [4, 3, 2, 1].
"""

def reverse_list(lst=None):
    reversed_lst = []
    if lst is not None and isinstance(lst, list):
        for i in reversed(lst):
            reversed_lst.append(i)
        return reversed_lst
    else:
        raise ValueError("sorry only list is allowed")
      
try:
    # content = reverse_list([1,2,3,4,5])
    content = reverse_list("kelly")
    print(content)
except  ValueError as ve:
    print(f"Error: {ve}")
