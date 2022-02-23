from tabulate import tabulate
from art import *
from rich.console import Console
import sys
import random


console = Console()
console.print(text2art("Hangman"), style="green")
data_new = []
def get_words(name, delimiter):
    global data_new
    file = open(name, "r")
    data = file.read()
    file.close
    data_new = str(data).split(delimiter)

get_words("words.txt", "\n")


hp = 0
word = data_new[random.randint(0, len(data_new))]
victimArray = ""
lettersCounter = len(word)
letters = ['_']*lettersCounter
isWin = False

#print(word) #to fast-bug-check uncomment this row


mustBeShown1 = [i for i, ltr in enumerate(word) if ltr == " "] #symbols that need to be shown and haven't to be guessed
for i in range(0, len(mustBeShown1)):
    letters[mustBeShown1[i]] = " "

mustBeShown2 = [i for i, ltr in enumerate(word) if ltr == "-"]
for i in range(0, len(mustBeShown2)):
    letters[mustBeShown2[i]] = "-"

mustBeShown2 = [i for i, ltr in enumerate(word) if ltr == "'"]
for i in range(0, len(mustBeShown2)):
    letters[mustBeShown2[i]] = "'"    

def printParameters(): #function can be called anywhere and can show current hp, hangman and guessed letters
    global victimArray

    if hp == 9:                    #hangman animation
        victimArray = "|"
    elif hp == 8:
        victimArray = "|\n|\n|"
    elif hp == 7:
        victimArray = "|\n|\n|\n|"
    elif hp == 6:
        victimArray = "|\n|\n|\n|\n|"
    elif hp == 5:
        victimArray = "|-\n|\n|\n|\n|"
    elif hp == 4:
        victimArray = "|--\n|\n|\n|\n|"
    elif hp == 3:
        victimArray = "|---\n|\n|\n|\n|"
    elif hp == 2:
        victimArray = "|---\n|  |\n|\n|\n|"
    elif hp == 1:
        victimArray = "|---\n|  | \n|    О\n|   /|\ \n|   / \ "
        
    data = [["{0}/10♥".format(hp)], [victimArray]]
    print(tabulate(data, tablefmt='fancy_grid'))
    print("")
    print(*letters)

def initGame(initHp): #you can enter hp and initializate new game
    global hp
    hp = initHp

def gameLoop():
    printParameters()
    global hp
    global letters
    global isWin

    while True:
        found = input("Guess a letter or type exit: ").lower()
        
        if word.find(found) != -1:
            guessedIndeces = [i for i, ltr in enumerate(word) if ltr == found]
            for i in range(0, len(guessedIndeces)):
                letters[guessedIndeces[i]] = found
            printParameters()
            break
            
        elif found == "exit":
             print('\033[F\033[K', end="")
             sys.exit()
        else:
             print('\033[F\033[K', end="")
             hp = hp - 1
             break


    if letters == list(word):
        isWin = True
                

initGame(10)

while True:
    gameLoop()
    if hp <= 0:
        victimArray = "|--т\n|  О \n| /|\    \n| / \ \n| "
        data = [["YOU LOSE! {0}/10♥".format(hp)], [victimArray]]
        console.print(tabulate(data, tablefmt='fancy_grid'), style="red")
        print("")
        while True:
            prompt = input("Would you like to play again? [y/n]: ").lower()
            print('\033[F\033[K', end="")
            if prompt == '' or not prompt in ['y','n']:
                victimArray = ""
                continue
            else:
                break
        if prompt == "y":
            victimArray = ""
            letters = ['_']*lettersCounter
            initGame(10)
        elif prompt == "n":
            break
    elif isWin == True:
        print("\nYou win!")
        while True:
            prompt = input("Would you like to play again? [y/n]: ").lower()
            print('\033[F\033[K', end="")
            if prompt == '' or not prompt in ['y','n']:
                victimArray = ""
                continue
            else:
                break
        if prompt == "y":
            victimArray = ""
            word = data_new[random.randint(0, len(data_new))]
            #print(word) #to fast-bug-check uncomment this row
            lettersCounter = len(word)
            letters = ['_']*lettersCounter
            mustBeShown1 = [i for i, ltr in enumerate(word) if ltr == " "] #symbols that need to be shown and haven't to be guessed
            for i in range(0, len(mustBeShown1)):
                letters[mustBeShown1[i]] = " "

            mustBeShown2 = [i for i, ltr in enumerate(word) if ltr == "-"]
            for i in range(0, len(mustBeShown2)):
                letters[mustBeShown2[i]] = "-"

            mustBeShown2 = [i for i, ltr in enumerate(word) if ltr == "'"]
            for i in range(0, len(mustBeShown2)):
                letters[mustBeShown2[i]] = "'"    
            isWin = False
            initGame(10)
        elif prompt == "n":
            break