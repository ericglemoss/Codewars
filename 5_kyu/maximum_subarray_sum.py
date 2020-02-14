# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers.
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    count_n = 0
    count_p = 0
    
    if not arr:
        return 0
    
    for num in arr:
        if num < 0:
            count_n += 1
        else:
            count_p += 1
    if count_n == len(arr):
        return 0
    if count_p == len(arr):
        return sum(arr)
      
    mx = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        mx = max(mx, curr_max)

    return mx
