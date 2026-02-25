def two_sum(arr, k):
    seen=set()
    for num in arr:
        diff = k - num
        if diff in seen:
            return True
        seen.add(num)
    return False

arr = [2,7,8,11]
k = 9
print(two_sum(arr,k))

arr1 = [6,2,3,7]
k1=11
print(two_sum(arr1,k1))