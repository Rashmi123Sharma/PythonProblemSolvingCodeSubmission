# a=input()
# b=input()
# count=0
# for i in range (len(b)):
#     if(a[i:i+2]==b[i:i+2] and  (len(a[i:i+2])==2) and (len(b[i:i+2])==2)):
#         count+=1
# print(count)



# non consecutively[1,2,3]
# arr=[1, 1, 2, 3,4,5,3,1]
# stack=[]
# for i in arr:
#     if(arr[i]==1  or  arr[i]==2 or  arr[i]==3 ):
#         stack.append(i)
#         if(stack[-1]==3):
#             print(stack)
#             break



# consecutively[1,2,3]
# def funct(arr):
#     for i in range(len(arr)):
#         if(arr[i:i+3]==[1,2,3]):
#             return True
#     else:
#         return False       
# a=funct([1, 1, 2, 3, 1])
# print(a)
# b=funct([1, 1, 2, 4, 1])
# print(b)
# c=funct([1, 1, 2, 1, 2, 3])
# print(c)
# d=funct([1, 2, 3, 1, 2, 3])
# print(d)


# str=input()
# res=" "
# for i in range(len(str)):
#     res+=str[:i+1]
# print(res)
