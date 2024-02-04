#Given a list, write a Python program to swap first and last element of the list.


def reverse_first_and_last(lst):
	first = lst[0]
	last  = lst[-1]
	tmp = first

	list[first] = last
	list[last] = tmp
	print(last)
	return lst


result = reverse_first_and_last([1,2,3,4,5])

print(result)
	
