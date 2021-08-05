# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:03:32 2020

@author: camer
"""

encrypt_synonyms=["encrypt","Encrypt","E","e"]
decrypt_synonyms=["decrypt","Decrypt","D","d"]
while True:
    print("Welcome to caesar crypting program, please enter mode (encrypt/decrypt)")
    mode_input=input()
    if mode_input in encrypt_synonyms:
        mode=("encrypt")
        break
    elif mode_input in decrypt_synonyms:
        mode=("decrypt")
        break
    else:
        print("invalid input")


manual_synonyms=["Manual","manual","m","M"]
import_synonyms=["Import","import","i","I"]
print("Would you like to enter message manually or import from file? Please enter: Manual/Import")
message_source_input=input("")
while True:
    if message_source_input in manual_synonyms:
        print("please enter message to "+mode)
        message=input()
        break
    if message_source_input in import_synonyms:
        print("Please enter directory path in format C:\\Users\\ ...\\...")
        file_location_read=input()
        print("Please enter file name")
        file_name_read=input()
        message=("")
        try:
            file = open(file_location_read+"\\"+file_name_read+".txt","r")
            for line in file:
                message+=line
            file.close
            print("File found")
            break
        except FileNotFoundError:
            print("file not found")
    else:
        print("invalid, please specify manual or import")
        message_source_input=input()

import random
while True:
    print("please specify rotation of "+mode+"ion, or specify random. If auto-decrypting, specify automatic")
    rotation_input=input()
    if rotation_input==("random"):
        rotation=random.randint(1,26)
        break
    if rotation_input==("automatic"):
        rotation=("automatic")
        break
    try:
        int(rotation_input)
        if int(rotation_input) in range(26):
            rotation=int(rotation_input)
            break
        else:
            print("rotation out of range, please re-enter integer (1<=N=<25), or type: random")
            rotation_input=input()
    except ValueError:
        print("invalid rotation")

import string
def rotated_message_function(rotation,message):
    global rotated_message
    rotated_message=("")
    def non_letter(element,element_type):
        if element in element_type:  #non-letter function bascially leaves any non-letter elements in the message unchanged
            global rotated_message
            rotated_message+=(element)  
    def rotated_letter(element,letters):
        if element in letters:                      #rotated-letter function rotates letters using the letter and the rotation
            original_position=letters.index(element)
            new_position=(original_position+rotation)
            if new_position<=0:
                new_position+=25
            if new_position>=25:
                new_position-=25
            global rotated_message
            rotated_message+=(string.ascii_lowercase[new_position])
    for element in message:
        non_letter(element,string.digits)
        non_letter(element,string.whitespace)
        non_letter(element,string.punctuation)
        rotated_letter(element,string.ascii_lowercase)
        rotated_letter(element,string.ascii_uppercase)

def raw_message_function(message_to_raw):  
    global raw_message 
    raw_message=("")
    for a in message_to_raw: 
        if a in string.ascii_letters:
            raw_message+=a
        if a in string.whitespace:
            raw_message+=a

def word_frequency_count_function(raw_message):
    global word_frequency_count
    word_frequency_count={}
    raw_words=raw_message.split(" ")
    for i in raw_words:
        if i in word_frequency_count:
            word_frequency_count[i]+=1
        if i not in word_frequency_count:
            word_frequency_count[i]=1    
 
if rotation !=("automatic"):
    if mode==("decrypt"):
        rotation *= -1
    rotated_message_function(rotation,message)
    print(mode+"ed message:"+rotated_message.upper()) 
    if mode==("decrypt"):
        raw_message_function(rotated_message)   
        word_frequency_count_function(raw_message) 
    if mode==("encrypt"):
        rotated_message_function(0,message)
        raw_message_function(rotated_message)
        word_frequency_count_function(raw_message)    

matching_words_count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
if rotation==("automatic"):
    for possible_rotations in range(1,25):
        rotated_message_function(possible_rotations,message)
        raw_message_function(rotated_message) 
        word_frequency_count_function(raw_message)
        words=list(word_frequency_count.keys()) 
        frequencies=list(word_frequency_count.values()) 
        file=open("words.txt","r") 
        common_words=("")  
        for a in file:
            common_words+=a   
        for a in common_words.split("\n"): 
            if a in words:
                matching_words_count[possible_rotations]+=frequencies[words.index(a)] 
        file.close
    ordered_matching_words=sorted(matching_words_count,reverse=True) 
    rotation=(matching_words_count.index(ordered_matching_words[0])) 
    rotated_message_function(rotation,message)
    print("Decrypted message: "+rotated_message)          
    print("\n")
    raw_message_function(rotated_message)
    word_frequency_count_function(raw_message)  
    
def message_analysis():
    print("Un-encrypted/Decrypted message analysis;")
    total_words=("Total number of words:"+str(len(raw_message.split(" "))))
    print(total_words)
    frequency_count_items=word_frequency_count.items()
    total_unique_words=("Total number of unique words:"+str(len(frequency_count_items)))
    descending_words=sorted(word_frequency_count.items(), key=lambda x:x[1],reverse=True)
    print("The most common words (up to the tenth) in descending order: ")
    n=0
    for i in descending_words:
        if n>=10 or n>=len(frequency_count_items):
            break
        print(descending_words[n][0],", occurances: "+str(descending_words[n][1]))
        n+=1
    
    word_length_count={}
    for i in raw_message.split(" "):
        if i not in word_length_count:
            word_length_count[i]=len(i)
    descending_word_lengths=sorted(word_length_count.items(),key=lambda x:x[1],reverse=True)
    longest_word=("Longest word: "+str(descending_word_lengths[0][0])+", length:"+str(descending_word_lengths[0][1]))
    print(longest_word)
    shortest_word=("Shortest word: "+str(descending_word_lengths[len(descending_word_lengths)-1][0])+", length:"+str(descending_word_lengths[len(descending_word_lengths)-1][1]))
    print(shortest_word)

    letter_count={}
    for a in raw_message.split(" "):
        for b in a:
            if b in letter_count:
                letter_count[b]+=1
            if b not in letter_count:
                letter_count[b]=1
    descending_letters=sorted(letter_count.items(),key=lambda x:x[1],reverse=True)
    print("Most common letter: "+str(descending_letters[0][0]))

    print("Please enter filename to save message stats:")
    file_name_write=input()
    with open(file_name_write+".txt","w") as file:
        file.write(total_words+"\n"+total_unique_words+"\n"+longest_word+"\n"+shortest_word)
message_analysis()
