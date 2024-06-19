def findingKMinMax(arr,k):
    arr.sort()
    return arr[k-1]
arr=list(map(int,input().split()))
k=int(input())
print(findingKMinMax(arr,k))
