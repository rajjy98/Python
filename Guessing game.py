import random

def guessingGame():


    print("Welcome to the guessing game!")
    print()
    print(input("press Enter for the directions"))
    print()
    print("Think of a random number 1-100 and I'll try to guess it")    #description of game/opening statements
    print()
    print(("If I get the number right tell me I'm \"correct\", otherwise tell me the whether the number is \"too high\" or \"too low\"."))
    print(("Make sure you type your response exactly as it is written above!"))      #Game directions, as exact and straight forward as possible... my mom barely reads english and she got them.
    print()
    print(input("Ready for me to start guessing? Press Enter!"))
    largestNum = int(101)   #the largest number is 101 non inclusive.
    smallestNum = int(0)    #the lowest number is set to 0 non inclusive.       #Used '101', and '0' because '100' and '1' can still be answer choices and the program always rounds up.
    guess = random.randint(1,100)
    print("My guess is:", guess)        #first guess is random

    feedback = str(input("So, how was my guess: "))     #Player response (too high, too low, or correct)

    while feedback != str("correct"):   #loop runs UNITL the use enters "correct".
        if feedback == str("too high"):
            largestNum = guess             #changes global variable larestNum to the guess. Narrows the range of possible numbers by getting rid of all numbers larger than the guess. Iterates making the range smaller until the number is "correct"

        elif feedback == str("too low"):
            smallestNum = guess             #changes global variable smallestNum to the guess. Narrows the range by getting rid of all numbers smaller than the guess. Iterates making the range smaller and smaller until the number is "correct".

        guess = ((largestNum+smallestNum)//2)   #Next guess is always the average of the smallest number and largest number. Constantly guesses the center of the range of possibilities, systematically discarding the most possibilites at a time.
        print("My guess is:", guess)
        feedback = str(input("So, how was my guess: ")) #allows for the uses to keep adding input until the user deems the number "correct"


    print("Finally I guessed the right number, thanks for playing!")     #"First game created, gotta say thank you"

    print(input("Press Enter to quit: "))     #basic necessities.











guessingGame()


