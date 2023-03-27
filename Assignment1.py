# dhundna hai bada sa paragraph more than 100 words
# 1.slicing(particular word)
# 2.starts with something and ends with something(any word starts with a like that:all words)
# 3.make this para wavy (first word capital,second lower)
# 4.find the words on this particular address and reverse them:17,34,51,70,80,90,23,63,98(print with vevy)




impwords=[]
story="An old man lived in the village. He was one of the most unfortunate people in the world.The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.The longer he lived, the more bile he was becoming and the more poisonous were his words.People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him."
impwords.append(story[7:11]);
impwords.append(story[24:31]);
impwords.append(story[56:67]);
print(impwords);


arr=[]
updated=story.split(" ");
for i in updated:
    print(i)
    if(i.startswith("a") and i.endswith("d")):
        arr.append(i)
print(arr)


arr=[]
updated=story.split(" ");
for i in updated:
    print(i)
    if(i.startswith("c") and i.endswith("d")):
        arr.append(i)
print(arr)





story="An old man lived in the village. He was one of the most unfortunate people in the world.The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.The longer he lived, the more bile he was becoming and the more poisonous were his words.People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him."
res=" ";
newa=[];
updated=story.split(" ");
for i in range(len(updated)):
    if(i%2==0 or i==0):
        newa.append(updated[i].lower())
    else :
        newa.append(updated[i].upper())
for i in newa:
    res+=i+" ";
print(res);


story="An old man lived in the village. He was one of the most unfortunate people in the world.The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.The longer he lived, the more bile he was becoming and the more poisonous were his words.People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him."
res=" ";
newa=[];
updated=story.split(" ");
for i in range(len(updated)):
    if(i%2==0 or i==0):
        newa.append(updated[i].lower())
    else :
        newa.append(updated[i].upper())
for i in range(len(newa)):
    if(i==16 or i==33 or i==50 or i==69 or i==79 or i==89 or i==22 or i==62 or i==97):
        newa[i]=newa[i][::-1]
for i in newa:
    res+=i+" ";
print(res);




a= "abcbcbcbca";
count=0
for i in range(len(a)):
    if(a[i:i+3]=="cbc"):
        count+=1;
print(count);


a="abcbcbcbca";
print(a.count("cbc"));




