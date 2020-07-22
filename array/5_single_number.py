# In non-empty array every but one element appers twice
# Return single one element

def singleNumber(arr):
	res = arr[0]

	for i in range(1,len(arr)):
		res = res ^ arr[i]

	return res