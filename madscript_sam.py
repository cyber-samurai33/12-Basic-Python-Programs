import os


class Sam:
    
    noun = str(input("Noun: "))
    verb = str(input("Verb: "))
    adjective = str(input("Adjective: "))
    adverb = str(input("Adverb: "))
    os.system("clear||cls")
    print('\t\t\t\t\tSam the Monkey\n')
    print(f'''\tThis is a story about a monkey name Sam. Sam was curious about many things,\n 
    \tsuch as {noun} Sam would {verb} all day and night when there were loud noise's.\n
    \tSam would often think of {adjective} when he was sitting on a branch.\n 
    \tSometimes Sam would have to {adverb} a tree to avoid getting eaten by other predators.\n
    \tSam was mostly interested in bananas and throwing poop, this was a daily activity for Sam.\n 
    ''' )

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + Sam + color.END)
