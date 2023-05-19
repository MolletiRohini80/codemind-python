arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=0
cc=0
for i in range(0,3):
    for j in range(0,3):
        if(arr[i]>brr[j] and i==j):
            c+=1
        elif(brr[j]>arr[i] and i==j):
            cc+=1
print(c,cc)