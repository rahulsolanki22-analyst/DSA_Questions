def sum_subarr(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += arr[j]
            total += curr_sum
    return total

arr = [3,1,2]
print(sum_subarr(arr))