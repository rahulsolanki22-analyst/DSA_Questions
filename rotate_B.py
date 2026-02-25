def rotate_B(arr,b):
    return arr[-b:]+arr[:-b]
arr=[1,2,3,4]
b = 2
print(rotate_B(arr,b))