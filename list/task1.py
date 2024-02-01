"""List Sum:
Create a function that takes a list of numbers as input and returns the sum of all the elements in the list.
"""

# def list_sum(lists = []):
#     sum = 0
#     if isinstance(lists, list):
#         for i in lists:
#             sum += i
#         return sum
#     else:
#         print("not allowed")
    

# # total = list_sum("ikjoijn")
# total = list_sum([1,2,3,4,5])
# print(f"The Total is {total}")


# so I prefer this code to the first one cause of how 
# simple it is.

# Found out yesterday that sum function also takes big O(n) to be honest i thought it takes big O(1) just as len function, well we learn everyday, lol 😂.....


def lst_sum(lst=None):
    if lst is None or not isinstance(lst, list):
        raise ValueError("input must be a list")
    return sum(lst) # call the python builtin sum method

# total = lst_sum([1,2,3,4,5])
try:
    total = lst_sum("ikjoijn")
    print(f"this is the Total {total}")
except ValueError as e:
   print(f"error: {e}")


