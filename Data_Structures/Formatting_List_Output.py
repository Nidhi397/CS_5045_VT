
    
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:25:47 2023

@author: User
"""

#Task is to read file and put it to a list
#Then create a nested list with 26 sub lists, representing 26 alphabet lists
#Finally add upto five words from that list starting with each alphabet in the respective sub lists

#read file and add it to a list

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
    
#Now we will format this list to look more organized:
# A : a,aa,...
#We want to include only relevant words, hence any single letter except a and i will not be a part of the sub list, make that change in code from line 49 
#Iterate through alphalist, take first character of first word of each sublist
# Append rest of the list ahead of that

for subword_list in alpha_list:
    first_subword_char=subword_list[0][0]
    print(first_subword_char.upper()+": ",end="")
    
    #Print words associated to each list
    # for word in subword_list:
    #     print(word+",",end="")
    # print("")
    
    #Using enuerate to remove commas at the end
    for (ind,word) in enumerate(subword_list):
        if ind<4:
            print(word+", ",end="")
        else:
            print(word)    