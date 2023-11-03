# import string

# a= input("Enter number:")
# a= list(a)
# print(a)
# for i in a:
#     if i not in string.hexdigits:
#         continue
#     else:
#         print("Not a hexadeximal")
#         break

# Define a function to check if a string is hexadecimal
# def is_hexadecimal(s):
#   # Try to convert the string to an integer with base 16
#   try:
#     int(s, 16)
#     return True # The conversion was successful, so the string is hexadecimal
#   except ValueError:
#     return False # The conversion failed, so the string is not hexadecimal

# # Read the input value from the user
# value = input("Enter a value: ")

# # Check if the value is hexadecimal or not
# if is_hexadecimal(value):
#   print("The value is hexadecimal.")
# else:
#   print("The value is not hexadecimal.")

# import tkinter as tk 

# # Top level window 
# frame = tk.Tk() 
# frame.title("TextBox Input") 
# frame.geometry('400x200') 
# Function for getting Input 
# from textbox and printing it 
# at label widget 

# def printInput(): 
# 	inp = inputtxt.get(1.0, "end-0c") 
# 	lbl.config(text = "Provided Input: "+inp) 

# # TextBox Creation 
# inputtxt = tk.Text(frame, height = 5, width = 20) 

# inputtxt.pack() 

# # Button Creation 
# printButton = tk.Button(frame, text = "Print", command = printInput) 
# printButton.pack() 

# # Label Creation 
# lbl = tk.Label(frame, text = "") 
# lbl.pack() 
# frame.mainloop() 

import re

regex = r'^[A-Za-z]$|^([A-Za-z]).*\1$'

st = input("Enter String: ")
if(re.search(regex, st)): 
    print("Valid") 
else: 
    print("Invalid")

