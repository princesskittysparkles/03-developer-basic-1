#!/usr/bin/env python3 

#This tells the system which version of Python to use

#Program Notes
#TODO Fill out the program notes
"""
Aurthor : [Your name here]
Email   : [Your email address here]
Purpose : [What does this program do?]
Date.   : [Date of completion]
"""


import argparse
import random


#-------------------------------------------------------------------------
#TODO: Ask the user how long they would like their new password to be
password_length = int(input("<prompt user for password length>") or 8 ) #default length is 8

#A list if symbols we can use in our password
symbols_list = ['!', '@', '#', '%', '&', '*']

#TODO: Create a list of numbers 0 - 9
numbers_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#TODO: Create a list of the 10 least used lowercase letters in the english language
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#TODO: Create a list of the 10 most use used uppercase letters in the english language
uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

#TODO: Join the 4 lists together to form a password character bank
password_character_bank = " " 

#We are going to loop over the password character bank and choose a character at random
#That character will be added to our password
password = []

#TODO: Loop over password character bank and choose a character at random
for x in range(password_length):
    password.append(random.choice(password_character_bank))

#print the password out to the user
print(''.join(password))

#Bonus
#TODO: Copy the generated password to the users clip board