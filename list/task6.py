#Given a list, write a Python program to swap first and last element of the list.

# a program that reverses python first and last list
def reverse_first_and_last(lst):
	size = len(lst)
	start = 0
	end = size - 1

	tmp = lst[start]

	lst[start] = lst[end]
	lst[end] = tmp
	return lst


# print the element
result = reverse_first_and_last([1])
print(result)
	
