# # # random generate indian phone numbers.
# # #find duplet tripelt and quad of which digit.and in which numbers.
# # #probability manuplation logic. triplet probaility must inc with setting.

import random
import string
d=[]
triplet=[]
dig= string.digits
for i in range (100):
    a=str(random.randint(6,9))
    b="".join(random.choice(dig)for i in range(9))
    c=a+b
    d.append(c)
print(d)
for ph in d[:50]:
    m=len(ph)//2
    a=ph.replace(ph[m:m+3],str(random.randint(0,9))*3)
    triplet.append(a)
for i in d[50:]:
    triplet.append(i)
print(triplet)
for ph in triplet:
    count=0
    n=0
    cn=0
    for i in range  (len(ph)-5):
        if(ph[i]==ph[i+1]==ph[i+2]==ph[i+3]):
            count+=1
            a=ph.replace((ph[i:i+4]),"")
            # print(a,ph,count)
   
        elif(a[i]==a[i+1]==a[i+2]):
            n+=1
            b=a.replace((a[i:i+3]),"")
            # print(b,ph,n)
   
        elif(b[i]==b[i+1] ):
            cn+=1
            c=b.replace((b[i:i+2]),"")
            # print(c,ph,cn)
           
           
            
            
    print(f"{ph} Phone number has {count} duplets {n} triplets {cn} quads ")