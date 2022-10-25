import sys
import os
import time
# When user makes wrong selection, add a function to return to title - 
# screen.


# Welcome to Mad Lib! Banner
print('Welcome to Mad Libs! Select your story!')
time.sleep(2)
print('')
print(''' [1] Sam
 [2] High School''')

# Mad lib Title Selection

title = int(input())

sam = 1
highschool = 2

# [1] Sam Selection / [2] High School Selection
if title == 1:
   import madscript_sam    
elif title == 2:
   import madscript_highschool_1
else:
   print("Retry Selection..")
   








   



