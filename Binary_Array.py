n=int(input())
s=list(map(int,input().split()))
for i in range(n):
    if s[i]!=0 and s[i]!=1:
        print("False")
        break
else:
    print("True")