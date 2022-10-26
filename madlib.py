
import sys
import os
import time
import keyboard
# Create a while loop to force user to select or go back to title.
# Getting a traceback error when hitting enter. 


# Welcome to Mad Lib! Banner
print('Welcome to Mad Libs! Select your story!')
print('')
print(''' [1] Sam
 [2] High School
  ''')

# Mad lib Title Selection

title = int(input(' > '))

# Disable Enter key so program does not give ValueError: invalid literal for in()

def disable_key():
   while True:
      if title == 1:
         import madscript_sam
      elif title == 2:
         import madscript_highschool
      elif title > 2:
         import madlib
      else:
         break
   
disable_key()
      
   










   



