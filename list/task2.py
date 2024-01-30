"""
List Reversal:
Write a program that reverses a given list. For example, if the input is [1, 2, 3, 4], the output should be [4, 3, 2, 1].
"""

def reverse_list(lst=None):
    reversed_lst = []
    for i in reversed(lst):
        reversed_lst.append(i)
    return reversed_lst
      
content = reverse_list([1,2,3,4,5])
print(content)
