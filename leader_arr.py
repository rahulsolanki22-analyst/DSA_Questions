def leader_arr(arr):
    n = len(arr)
    leader = []
    lead_right = arr[-1]
    leader.append(lead_right)

    for i in range(n-2,-1,-1):
        if arr[i]>lead_right:
            leader.append(arr[i])
            lead_right=arr[i]
    return leader[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(leader_arr(arr))