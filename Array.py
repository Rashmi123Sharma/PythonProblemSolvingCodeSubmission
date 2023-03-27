# # # Let us say your expense for every month are listed below,
# # # January - 2200
# # # February - 2350
# # # March - 2600
# # # April - 2130
# # # May - 2190
# # # Create a list to store these monthly expenses and using that find out,





# # expense = {"January":2200,"February":2350,"March":2600,"April":2130,"May":2190}

# # # 1. In Feb, how many dollars you spent extra compare to January?
# # print(expense["February"]-expense["January"]);


# # # 2. Find out your total expense in first quarter (first three months) of the year.
# # print(expense["February"]+expense["January"]+expense["March"]);


# # # 3. Find out if you spent exactly 2000 dollars in any month

# # for x in expense:
# #     if(expense[x]==2000):
# #         print(expense[x])
# #     else :
# #         print("No month has 2000 expense");


# # # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

# # expense["June"]=1980;
# # print(expense);


# # # 5. You returned an item that you bought in a month of April and  got a refund of 200$. Make a correction to your monthly expense list
# # # based on this
# # expense["April"]=2130-  200;
# # print(expense);





# # You have a list of your favourite marvel super heros.
# # heros=['spider man','thor','hulk','iron man','captain america']
# # Using this find out,


# ros=['spider man','thor','hulk','iron man','captain america']

# # 1. Length of the list
# #print(len(ros));

# # 2. Add 'black panther' at the end of this list
# ros.append("black panther");
# print(ros);


# # 3. You realize that you need to add 'black panther' after 'hulk',
# #    so remove it from the list first and then add it after 'hulk'

# ros.remove("black panther");
# print(ros);

# ros.insert(3,"black panther");
# print(ros);


# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# ros[1:3]=['doctor strange']
# print(ros)

# # 5. Sort the list in alphabetical order
# ros.sort()
# print(ros)




## Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# maxnum= int(input ("Enter the number"));
# odd=[]
# for i in range(1,maxnum):
#     if(i%2!=0):
#         odd.append(i);
# print(odd);
        

