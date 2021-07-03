def maxSum(arr,m):
    if m<=0:
        return 0
    return max(arr[m-1]+maxSum(arr,m-2),maxSum(arr,m-1))




arr=list(map(int,input().split()))
m=len(arr)

res=maxSum(arr,m)
print(res)
