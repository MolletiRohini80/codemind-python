n=int(input())
t=n
s=0
while(n!=0):
    d=n%10
    s=s*10+d
    n=n//10
if(t==s):
    print("Palindrome")
else:
    print("Not Palindrome")