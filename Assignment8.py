import re
story='''  ramzan abb This classic_ fable_ (story) tells the story abbbbb of a very slow tortoise (turtle) and a speedy hare (rabbit).
The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than he,
but the race leads to surprising results.What Is Great About It: Have you ever heard the English expression,
“Slow and steady wins the race”? This story is the basis for that common phrase.This timeless (classic) short 
story teaches a lesson that we all know but can sometimes forget: Natural talent is no substitute for hard work,
and overconfidence often leads to failure.

'''
# print(len(story))

# tortoise
z=re.findall(r"\bto.....e\b",story)
# print(z)
a=re.findall(r"\bt\w.{5}e\b",story)
# print(a)


# hare reverse
b=re.findall("h.{2}e",story)
# print(b)
# for i in b:
#     c=i[::-1]
# print(c)


# having a and b in between 
d=re.findall(r"\b\w+.[ab]+\w\b",story)
# print(d)
# print(set(d))



# Write a Python program that matches a string that has an a followed by one or more b's.
e=re.findall(r"\b a.*b\b",story)
print(e)


# 
# f=re.findall(r"\bS.*e\b",story)print(f)



# Write a Python program to find sequences of lowercase letters joined by an underscore.
# g=re.findall(r"\b[a-z]+_",story)
# print(g)




# Write a Python program that matches a word containing 'z', not the start or end of the word. 

h=re.findall(r"\w* z\w*",story)
# print(h)