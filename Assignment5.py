#generate 5 random passwords
import random
count=int(input("How many passwords you want: "))
pwd=" "
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="!@#$%^&*()"
d=random.randrange(0,1000)
z=a+b+c+str(d)
for i in range(count):
    pwd="".join(random.choice(z)for i in range(random.randrange(8,21)))
    print(pwd)


