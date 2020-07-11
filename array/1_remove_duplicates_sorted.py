# The task is to remove duplicates from sorted array
# modifying original array and not allocating extra
# space for new or temrorary array
#
# Return array and it's length

def removeDuplicates(arr):
	currentLength = len(arr)
	if currentLength <= 1:
		return (arr, currentLength)

	iterator = 0
	while True:
		print("DEBUG 1: " + str(iterator) + " " + str(currentLength) + str(arr))
		if iterator >= currentLength - 1:
			break

		if arr[iterator] == arr[iterator+1]:
			print("DEBUG 2: " + str(iterator) + " " + str(currentLength) + str(arr))
			arr.pop(iterator+1)
			currentLength -= 1
			iterator -= 1

		iterator += 1
		print("DEBUG 3: " + str(iterator) + " " + str(currentLength) + str(arr))

	return (arr, currentLength)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1]))
print(removeDuplicates([]))
