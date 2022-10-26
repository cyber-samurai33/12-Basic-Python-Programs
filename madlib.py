
import sys
import os
import time
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
os.system('clear||cls')



def disable_key():
   while True:
      if title == 1:
         import madscript_sam
         break
      elif title == 2:
         import madscript_highschool
         break
      elif title > 2:
         import madlib
disable_key()          





 










   



