def movingNegNumbers(arr):
    positive=[]
    negative=[]
    for i in arr:
        if(i>=0):
            positive.append(i)
        else:
            negative.append(i)
    return positive+negative

arr=list(map(int,input().split()))
print(movingNegNumbers(arr))
        


