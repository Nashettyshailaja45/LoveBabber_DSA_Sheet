def minMaxOfArray(arr):
    arr.sort()
    s=arr[0],arr[-1]
    return s
arr=list(map(int,input().split()))
print(minMaxOfArray(arr))
