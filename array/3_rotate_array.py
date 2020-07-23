# The task is to rotate the array to the right by k steps

def rotateArray(arr):
    length = len(nums)
    if length == 1 or k == 0 or k == len(nums):
        return nums

    if k > length:
        k %= length
        
    nums[length-k:], nums[:length-k] = nums[:length-k], nums[length-k:]
