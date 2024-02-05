#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

def swap_pos(param1, param2, lst):
    # save the first element
    tmp = lst[param1]

    lst[param1] = lst[param2]

    lst[param2] = tmp

    return lst



# print the element
result = swap_pos(1,5,[1,2,3,4,5])
print(result)
	

