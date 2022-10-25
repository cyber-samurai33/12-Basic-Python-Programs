import sys
import os
import time



# Welcome to Mad Lib! Banner
print('Welcome to Mad Lib!')
time.sleep(2)
os.system('cls||clear')

# Mad lib Title Selection
title = int(input(print(f"""
            [{1}] A Monkey Named Sam
            [{2}] Highschool""")))


sam = 1
highschool = 2

# [1] Sam Selection / [2] High School Selection
if title == 1:
   import madscript_sam    
elif title == 2:
   import madscript_highschool_1
else:
   print("Retry Selection..")
   








   



