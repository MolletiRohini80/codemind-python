a,b,c,d,e=map(int,input().split())
m=(a+b+c+d+e)/5
if m>=90:
    print("Grade A")
elif m>=80:
    print("Grade B")
elif m>=70:
    print("Grade C")
elif m>=60:
    print("Grade D")
elif m>=40:
    print("Grade E")
else:
    print("Grade F")