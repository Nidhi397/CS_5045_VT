# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:47:58 2023

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:02:10 2023

@author: User
"""

#Initialize list
words_list=[]

#Read file and store in file descriptor

file = open("words.txt","r")

for f in file:
    words_list.append(f.strip())
    
#Create nested list with 26 sublists

alpha_list=[]

for i in range(26):
    alpha_list.append([])

#Add upto five words in each sublist of alpha list

#Loop through words_list as we check every word here
#Index every letter ord 

for char in words_list:
    #We check first letter of char
    first_char=char[0]
    first_char_num=ord(first_char.upper())-65
    if first_char_num<0:
        print("Looks like a negative number, something went wrong")
    if first_char_num>25:
        print("Number out of bounds")
    
    #Sub list is equivalent to the [] in the alpha_list, first_char_num gives the index to ensure correct organization
    sub_list=alpha_list[first_char_num]   
    #Only words with first letter associated to the char num will be appended to this list

    if len(sub_list)<5:
        if len(char)>1 or char in ['a','i']: 
            sub_list.append(char)
            
#Create a dictionary to get a count of the number of times each word started with the character
#Initialize dictionary
first_char_dict={}
#Loop through word_list
for word in words_list:
    first_character=word.lower()[0]       
    if first_character in first_char_dict:
        first_char_dict[first_character]+=1
    else:
        first_char_dict[first_character]=1

total_char_count={}
#Looping through to get the frequency of each letter 
for word in words_list:
    for char in word:
        if char in total_char_count:
            total_char_count[char]+=1
        else:
           total_char_count[char]=1

#Read new file moby.txt
#Initialize list to save words
book_list=[]
#Create list of punctuations to be replaced
punctuations=[",",".","'",'"',":",";","(" ,")","-"]
with open("moby.txt","r") as file:
    count=0
    for f in file:
        if count>=311:
            #Remove white spaces
            f=f.strip()
            #Replace punctuations in every line with empty space
            for i in punctuations:
                f.replace(i,"")
            #Separate words based on spaces    
            f_list=f.split(" ")    
            book_list+=f_list 
                
        count+=1
m_char_dict={}
#Loop through book_list
for word in book_list:
    if len(word)>0:
        first_character=word.lower()[0]       
        if first_character in m_char_dict:
            m_char_dict[first_character]+=1
        else:
            m_char_dict[first_character]=1

m_total_char_count={}
#Looping through to get the frequency of each letter 
for word in book_list:
    for char in word:
        if char in m_total_char_count:
            m_total_char_count[char]+=1
        else:
           m_total_char_count[char]=1        
#Print Key with key values
for key in first_char_dict.keys():
    print(key,":",first_char_dict[key],"\t",total_char_count[key],"\t",m_char_dict[key],"\t",m_total_char_count[key])
    
    