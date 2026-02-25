def min_time(arr):
    max_val = max(arr)
    time = 0
    for num in arr:
        time = time + (max_val-num)
    return time

arr = [2,4,1,3,2]
print(min_time(arr))