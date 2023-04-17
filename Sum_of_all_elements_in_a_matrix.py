N,M=map(int, input().split())
mat=[]
s=0
for i in range(N):
    sub_lst=list(map(int,input().split()))
    mat.append(sub_lst)
for i in mat:
    s=s+sum(i)
print(s)
    
