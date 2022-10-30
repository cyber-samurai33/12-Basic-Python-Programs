
import sys
import os
import time
# Create a while loop to force user to select or go back to title.
# Getting a traceback error when hitting enter. 


# Welcome to Mad Lib! Banner

print('\n\nWelcome to Mad Libs! Select your story!')
print('')
print('[1] Sam')
print('[2] High School')

# Mad lib Title Selection

try:
 
   title = int(input(' > '))
   while True:
      os.system("clear||cls")
      if title == 1:
         import madscript_sam
         str(input("Press Enter (Esc)"))
         os.system('clear||cls')
         break   
      os.system("clear||cls")     
      if title == 2:
         import madscript_highschool
         str(input("Press Enter (Esc)"))
         os.system('clear||cls')
         break
      if title > 2:
         import madlib
         break
except: 
    import madlib
    os.system("clear||cls")
   

      
         
      




 










   



