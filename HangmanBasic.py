
import random

def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        return x

wordBank = ['Dog','Frog','Toss','Food','Toad','Road']
correctguesses = []
guesses = []
wordPick = random.randint(0,len(wordBank)-1)
wordPick = wordBank[wordPick]
wordPick = wordPick.lower()
wordPickset = set(wordPick)
wordLength = int(len(wordPick))
print(wordPick)
for i in range(wordLength):
    correctguesses.append(" _ ")


for i in range(10):
    print('-------------------------------------------------------')
    userGuess = input("What Is Your Guess?")
    userGuessUsable = userGuess
    userGuessUsable = userGuessUsable.lower()
    guesses.append(userGuessUsable)
    userGuess = set(userGuess)

    common = ''.join(sorted(wordPickset.intersection(userGuess)))
    for x in range(wordLength):
        if wordPick[x] == common:
            correctguesses[x] = common
        #elif wordPick[x] != common:
            #wrongguesses.append(userGuessUsable)
    print(*correctguesses, sep=' ')
    print("Guesses", *guesses, sep=' - ')
    print('-------------------------------------------------------')
    if userGuessUsable == wordPick:
        print('---------------------THANK YOU-------------------------')
        print("Good Job You Got It Right!")
        quit()
