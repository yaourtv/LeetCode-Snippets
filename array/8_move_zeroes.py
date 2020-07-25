# Move zeroes to the end of the given array

def moveZeroes(nums):
	lastPointer = 0

	for i in range(len(nums)):
		if nums[i] != 0:
			nums[lastPointer] = nums[i]
			lastPointer += 1

	for i in range(lastPointer, len(nums)):
    	nums[i] = 0
