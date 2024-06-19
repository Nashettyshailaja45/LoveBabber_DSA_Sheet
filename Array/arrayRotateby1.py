def arrayRotateBy1(arr):
    last_element=arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last_element
    return arr
arr=list(map(int,input().split()))
print(arrayRotateBy1(arr))
