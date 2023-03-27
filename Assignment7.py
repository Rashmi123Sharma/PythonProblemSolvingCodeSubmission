import re
story="An old man lived in the village. He was one of the most unfortunate people in the world.The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.The longer he lived, the more bile he was becoming and the more poisonous were his words.People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him."
a=re.findall("a",story)
# print(a)

b=re.findall("a.*e",story)
# print(b)

c=re.findall("[a-d]",story)
# print(c)

d=re.findall("a.*e",story)
# print(d)

e=re.findall("a.+e",story)
# print(e)

f=re.findall("^An",story)
# print(f)
