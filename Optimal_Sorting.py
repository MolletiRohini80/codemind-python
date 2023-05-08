n=int(input())
for i in range(n):
    m=int(input())
    x=list(map(int,input().split()))
    k=[]
    for i in x:
        k.append(i)
    x.sort()
    if k==x:
        print("0")
    else:
        print(max(x)-min(x))