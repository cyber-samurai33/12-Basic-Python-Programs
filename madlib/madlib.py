
import sys
import os
import time
# Create a while loop to force user to select or go back to title.
# Getting a traceback error when hitting enter. 


# Welcome to Mad Lib! Banner

print('Welcome to Mad Libs! Select your story!')
print('')
print('[1] Sam')
print('[2] High School')

# Mad lib Title Selection

title = int(input(' > '))
os.system('clear||cls')

def menu_script():
   while True:
      try:
         if title == 1:
            import madscript_sam
            str(input("Any key to Esc"))
            os.system('clear||cls')
            break          
         if title == 2:
            import madscript_highschool
            str(input("Any key to Esc"))
            os.system('clear||cls')
            break
         elif title > 2: 
            import madlib
      except: 
         print("Error")
   
menu_script()  
      
         
      




 










   



