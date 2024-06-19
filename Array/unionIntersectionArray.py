def unionIntersectionArray(arr1,arr2):
    s=set(arr1)
    k=set(arr2)
    return s.union(k),s.intersection(k)
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(unionIntersectionArray(arr1,arr2))
