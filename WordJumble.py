##Word Jumble

#imports
import random

#Global Variables
WORDS = ("PYTHON", "JUMBLE", "EASY", "DIFFICULT", "ANSWER", "XYLOPHONE")


def jumbleWord(word):
    Letters = list(word) #makes the word into a list of letters
    random.shuffle(Letters) #shuffles them
    shuffledList = ''.join(Letters) #puts the list back together as another string variable
    if shuffledList != word: #making sure the shuffled list does not equal the orignial word
        return shuffledList
    else:
        return jumbleWord(word)

def takeGuess(correct):
    userGuess = ''
    Attempt = 1
    while userGuess!=correct:
        if Attempt >= 2:
            askForHint(Attempt, correct)
        userGuess = input('What is the word?: ')
        if userGuess.lower() == correct.lower():
            print('Great guess, The word is correct')
            print('It took you', Attempt, 'attempts')
            return
        else:
            print('The guess is incorrect, try again')
            Attempt += 1
            continue

def askForHint (Attempt,correct):
    print("This would be attempt number:", Attempt)
    response = ''
    while response not in ["yes", "no"]:
        response = input('Would you like a hint \"yes\" or \"no\"? ').lower()
    if response == 'yes':
        getHint(correct)
    elif response == "no":
        pass

def getHint(correct):
    change = ["- " for i in range(len(correct))]
    new = random.randint(0,len(correct)-1)
    change[new] = correct[new] + " "
    hint = ''.join(change)
    print('Your hint is:', hint)


def welcome():
    print('''
            Welcome to Word Jumble!
    Unscramble the letters to make a word.
  (Press the enter key at the prompt to quit.)
    ''')



def main():
    word = random.choice(WORDS)
    correct = word
    jumbled = jumbleWord(word)
    welcome()
    print("The jumble is: ", jumbled)
    takeGuess(correct)
    print("That's it!!!")
    input("Press enter to quit")

main()