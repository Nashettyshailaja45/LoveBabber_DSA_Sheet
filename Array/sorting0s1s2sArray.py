def sorting0s1s2sArray(arr,n):
    low=0
    mid=0
    high=n-1
    while(mid<high):
        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
arr=list(map(int,input().split()))
n=int(input())
print(sorting0s1s2sArray(arr,n))
