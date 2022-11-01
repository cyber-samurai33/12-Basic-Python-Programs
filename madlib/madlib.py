
import sys
import os
import time

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
      elif title == 2:
        import madscript_highschool
        str(input("Press Enter (Esc)"))
        os.system('clear||cls')
        break
      elif title > 2:
        import madlib
        os.system("clear||cls")

except:
    print("Error")
