def odd_indices(lst):
	new_list=[]
	for i in range(len(lst)):
		if i%2!=0:
			new_list.append(lst[i])
	return new_list
	