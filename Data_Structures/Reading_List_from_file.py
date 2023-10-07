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
        sub_list.append(char)
    
    