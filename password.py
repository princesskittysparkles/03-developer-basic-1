#!/usr/bin/env python3 

#This tells the system which version of Python to use

#Program Notes
#There are some program notes.
"""
Author : [Andrea Brody]
Email   : [andreaLbrody@gmail.com]
Purpose : [This is a password generator]
Date    : [March 23, 2021]
"""


import argparse
import random


#-------------------------------------------------------------------------
#TODO: Ask the user how long they would like their new password to be
password_length = int(input("How long would you like the password to be? ") or 8 ) #default length is 8

#A list if symbols we can use in our password
symbols_list = ['!', '@', '#', '%', '&', '*']

#TODO: Create a list of numbers 0 - 9
numbers_list = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#TODO: Create a list of the 10 least used lowercase letters in the english language
lowercase_list = ['z', 'q', 'j', 'x', 'k', 'v', 'b', 'y', 'w', 'g']

#TODO: Create a list of the 10 most use used uppercase letters in the english language
uppercase_list = ['E', 'A', 'R', 'I', 'O', 'T', 'N', 'S', 'L', 'C']

#TODO: Join the 4 lists together to form a password character bank
password_character_bank = (symbols_list + numbers_list + lowercase_list + uppercase_list)

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
def Copy_password():
    pyperclip.copy(pass_str.get())

    Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
