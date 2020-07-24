# Array of digits represents a non-negative integer k
# Return array that represents k+1

def plusOne(digits):
	num = int("".join([str(i) for i in digits]))+1
        
    return [int(i) for i in str(num)]
