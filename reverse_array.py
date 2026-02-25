def reverse_arr(arr):
    n=len(arr)
    l = 0
    r = n-1
    while(l<r):
        arr[l] , arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    return arr

arr = [1,2,3,4,5]
print(reverse_arr(arr))