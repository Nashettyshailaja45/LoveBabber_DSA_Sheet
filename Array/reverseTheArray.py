"""

# Method 1

def reversingArray(arr):
    arr.reverse()
    return arr

arr=list(map(int,input().split()))
print(reversingArray(arr))
"""

"""
# Method 2
def reversingArray(arr):
    return arr[::-1]
arr=list(map(int,input().split()))
print(reversingArray(arr))
        
"""

# Method 3
def reversingArray(arr):
    start=0
    end=len(arr)-1
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
arr=list(map(int,input().split()))
print(reversingArray(arr))
        

    
