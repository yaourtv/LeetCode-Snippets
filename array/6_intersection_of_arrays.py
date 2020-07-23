# Write a function to compute intersection of two arrays

def intersect(arr1, arr2):
	result = []

    for i in arr1:
        if i in arr2:
            result.append(i)
            nums2.remove(i)
                
    return result