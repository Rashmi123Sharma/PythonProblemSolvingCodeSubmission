# from datetime import datetime
# # date = input("Enter first date (YYYY-MM-DD hh:mm:ss): ")
# # a = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
# # date_ = input("Enter second date (YYYY-MM-DD hh:mm:ss): ")
# # b= datetime.strptime(date_, "%Y-%m-%d %H:%M:%S")
# # date__ = input("Enter third date (YYYY-MM-DD hh:mm:ss): ")
# # c= datetime.strptime(date__, "%Y-%m-%d %H:%M:%S")

# a=datetime(year=1974,month=4,day=15,hour=5,minute=16,second=5)
# b=datetime(year=1972,month=4,day=29,hour=7,minute=19,second=5)
# c=datetime(year=2005,month=4,day=3,hour=9,minute=21,second=9)

# if((b-a)<(a-b)):
#     x1=a-b
#     y=x1.days//365
#     m=(x1.days-y*365)//30
#     d=(x1.days-y*365-m*30)
#     h=x1.seconds//3600
#     minute=(x1.seconds%3600)//60
#     sec=x1.seconds%60
#     print(f"a is younger than b by {str(x1.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")

# if((c-a)<(a-c)):
#     x1=a-c
#     y=x1.days//365
#     m=(x1.days-y*365)//30
#     d=(x1.days-y*365-m*30)
#     h=x1.seconds//3600
#     minute=(x1.seconds%3600)//60
#     sec=x1.seconds%60
#     print(f"a is younger than c by {str(x1.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")


# if((a-b)>(b-a)):
#     x=a-b
#     y=x.days//365
#     m=(x.days-y*365)//30
#     d=(x.days-y*365-m*30)
#     h=x.seconds//3600
#     minute=(x.seconds%3600)//60
#     sec=x.seconds%60
#     print(f"b is older than a by {str(x.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")


# if((c-b)<(b-c)):
#     x1=b-c
#     y=x1.days//365
#     m=(x1.days-y*365)//30
#     d=(x1.days-y*365-m*30)
#     h=x1.seconds//3600
#     minute=(x1.seconds%3600)//60
#     sec=x1.seconds%60
#     print(f"b is younger than c by {str(x1.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")

 

# if((a-c)>(c-a)):
#     x=a-c
#     y=x.days//365
#     m=(x.days-y*365)//30
#     d=(x.days-y*365-m*30)
#     h=x1.seconds//3600
#     minute=(x1.seconds%3600)//60
#     sec=x1.seconds%60
#     print(f"c is older than a by {str(x.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")

  


# if((b-c)>(c-b)):
#     x=b-c
#     y=x.days//365
#     m=(x.days-y*365)//30
#     d=(x.days-y*365-m*30)
#     h=x1.seconds//3600
#     minute=(x1.seconds%3600)//60
#     sec=x1.seconds%60
#     print(f"c is older than b by {str(x.days)}  days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds")






from datetime import datetime 
a=datetime(year=1974,month=4,day=15,hour=0,minute=16,second=5)
b=datetime(year=1972,month=4,day=29,hour=0,minute=19,second=5)
c=datetime(year=2005,month=4,day=3,hour=0,minute=21,second=9)

if (a>b):
    x=a-b
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"a is older to b by {(a-b).days} days  {str(y)} years {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"b is younger to a by {(a-b).days} days {str(y)} years {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"a is older to b by {(a-b).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"b is younger to a by {(a-b).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours  {str(minute)} minutes {str(sec)} seconds ")
    
if(b>a):
    x=a-b
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"b is older to a by {(b-a).days} days  {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"a is younger to b by {(b-a).days} days {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"b is older to a by {(b-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"a is younger to b by {(b-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
 
if(a>c):
    x=a-c
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"a is older to c by {(c-a).days} days {str(y)} years  {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"c is younger to a by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"a is older to c by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"c is younger to a by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
 
if(c>a):
    x=c-a
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"c is older to a by {(c-a).days} days {str(y)} years  {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"a is younger to c by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"c is older to a by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"a is younger to c by {(c-a).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")

if(b>c):
    x=b-c
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"b is older to c by {(b-c).days} days {str(y)} years  {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"c is younger to b by {(b-c).days} days {str(y)} years {str(m)} months {str(d)} days {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"b is older to c by {(b-c).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"c is younger to b by {(b-c).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")

if(c>b):
    x=c-b
    y=x.days//365
    m=(x.days-y*365)//30
    d=(x.days-y*365-m*30)
    h=x.seconds//3600
    minute=(x.seconds%3600)//60
    sec=x.seconds%60
    if(h==0):
        print(f"c is older to b by {(c-b).days} days {str(y)} years  {str(m)} months {str(d)} days  {str(minute)} minutes {str(sec)} seconds ")
        print(f"b is younger to c by {(c-b).days} days {str(y)} years {str(m)} months {str(d)} days {str(minute)} minutes {str(sec)} seconds ")
    
    else:
    
        print(f"c is older to b by {(c-b).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")
        print(f"b is younger to c by {(c-b).days} days {str(y)} years {str(m)} months {str(d)} days {str(h)} hours {str(minute)} minutes {str(sec)} seconds ")

    
    
    
    
    
    
    


