import sys
import os
import time
from keyboard import press
# Create a while loop to force user to select or go back to title.
# Getting a traceback error when hitting enter. 


# Welcome to Mad Lib! Banner
print('Welcome to Mad Libs! Select your story!')
print('')
print(''' [1] Sam
 [2] High School
  ''')

# Mad lib Title Selection

title = int(input("> "))

while title == press:
   pass
   if title == 1:
      import madscript_sam
   elif title == 2:
      import madscript_highschool

if title == 1: 
   import madscript_sam
elif title == 2:
   import madscript_highschool
else: 
   import madlib








   



