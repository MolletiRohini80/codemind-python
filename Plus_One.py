n=int(input())
a=list(map(str,input().strip().split()))
d=''
for i in a:
    d+=i
d=int(d)
d+=1
d=str(d)
print(*d)