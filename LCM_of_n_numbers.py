def lcm(a,b):
    l=max(a,b)
    while True:
        if l%a==0 and l%b==0:
            break
        else:
            l+=max(a,b)
    return l
a=int(input())
arr=list(map(int,input().split()))
r=lcm(arr[0],arr[1])
for i in range(2,a):
    r=lcm(r,arr[i])
print(r)
