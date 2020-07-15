# The task is to remove duplicates from sorted array
# modifying original array and not allocating extra
# space for new or temrorary array
#
# Return array and it's length

def removeDuplicates(arr):
    currentLength = len(arr)
    if currentLength <= 1:
        return

    iterator = 0
    while iterator >= currentLength:

        if arr[iterator] == arr[iterator+1]:
            arr.pop(iterator+1)
            currentLength -= 1
            iterator -= 1

        iterator += 1
