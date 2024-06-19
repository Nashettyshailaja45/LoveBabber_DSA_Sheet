def contiguousSumSubarray(arr):
    currsum=arr[0]
    prevsum=arr[0]
    for i in range(1,len(arr)):
        currsum=max(arr[i],currsum+arr[i])
        if(currsum>=prevsum):
            prevsum=currsum
    return currsum
arr=list(map(int,input().split()))
print(contiguousSumSubarray(arr))
