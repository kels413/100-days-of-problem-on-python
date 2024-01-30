"""
List Filtering:
Create a function that takes a list of numbers and returns a new list containing only the even numbers from the original list.
"""

def even_list(lst=None):
    even_lst = []

    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst

content = even_list([1,2,3,4,5,6,7,8,9,10])
print(content)