def angle(h,m):
    if(h==12):
        h=0
    if(m==60):
        m=0
        h+=1
        if(h>12):
            h=h-12
    hour=0.5*(h*60+m)
    minute=6*m
    angle=abs(hour-minute)
    angle=min(360-angle,angle)
    return angle
h,m=map(int,input().split(":"))
print(angle(h,m))