"""
List Square:
Write a program that takes a list of numbers as input and returns a new list where each element is the square of the corresponding element in the original list.
"""

def square_list(lst=None):

    if lst is None or not isinstance(lst, list):
        raise ValueError("Input must be a list")

    square_lst = []

    for i in lst:
        square_lst.append(i * i)
    return square_lst

try:
    content = square_list([1,2,3,4,5])
    # content = square_list("dewfe")
    print(content)
except ValueError as ve:
    print(f"Error: {ve}")