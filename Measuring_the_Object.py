w,x,y,z=map(int,input().split())
a=x+y
b=y+z
c=x+z
if(w==a or w==b or w==c):
    print("YES")
elif(w==x or w==y or w==z):
    print("YES")
else:
    print("NO")