# Task is to find the most effective way to buy and sell
# Values are stored in array, where index is day and the
# value is the price. You can buy only once before selling
# Return value should be the most profit or 0 if you can't
# make any.

def countProfit(array):
    if len(arr) == 1:
        return 0
        
    maxProfit = 0

    for i in range(len(arr)-1):
        diff = arr[i+1] -  arr[i]

        if diff > 0:
            maxProfit += diff

    return maxProfit
