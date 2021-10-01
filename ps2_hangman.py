# Problem Set 2
# Name: Rashmi
# Time Spent: 3 days 

import random
                
 
print("शब्दों कि सूची लोड हो रही है......")
WORDLIST_FILENAME = "w.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()
print("  ", len(wordlist),"लोड किए गए शब्द।" )
word = random.choice(wordlist)                                        

print("खेल में आपका स्वागत है")
guesses = ''
print("मैं एक ऐसे शब्द के बारे में सोच रहा हूं जो",len(word),"अक्षर लंबा है")
 
                
turns = 8             
 
 
while turns > 0:
     
                         
    failed = 0
     
                       
    for char in word:
         
                               
        if char in guesses:
            print(char)
             
        else:
           
              failed += 1
             
 
    if failed == 0:
        print("आप जीतते हैं")
         
        
        print("शब्द है: ", word)
        break
     
   
    guess = input("पात्रों का अनुमान लगाएं:")
     
   
    guesses += guess
     
   
    if guess not in word:
         
        turns -= 1
         
       
        print("गलत")
         
       
        print("आपके पास", + turns, 'अधिक अनुमान')
         
         
        if turns == 0:
            print("आप हारे")
