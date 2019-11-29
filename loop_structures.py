import random

def sumOdds(input_value):
    initial = 1    #The first odd number is one
    total = 0       #The total of the odd numbers equals 0
    while initial <= input_value:   #the loop starts at 1 because 0 has no odd numbers in, but one does
        total += initial        #inital gets added to total
        initial += 2            #initial begins as an odd number, thus inital plus 2 will remain odd

    print('The sum of the odds is:', total)

def characterCount(text):
    total = 0       #represents total characters in variable text
    for i in text:
        total += 1  #The loop iterates over every character adding one to "total" each time
    print('The number of total characters is:', total)

def multiplicationPractice():
    right = 0       #number of correct answers
    while right !=3:    #The loop will stop iterating once there are 3 correct answers
        num1 = random.randint(1, 10)    #Makes sure that a random number is chosen between 1 and 10, each time the loop iterates
        num2 = random.randint(1, 10)
        print("The problem is:", num1,"x",num2)
        answer = int(input("your answer is: "))
        if answer == (num1 * num2):  #if the answer inputed by the user is equal to the numbers multiplied...
            print("The answer is correct")
            right += 1      #... 1 is added to the variable "right" (as labeled above)
        else:
            print("sorry the answer is incorrect, try another") #else the answer is incorrect, and user is prompted to try again
    print("Congratulations you answered 3 questions correctly")

def testOrder():
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    value3 = int(input("Enter the third number: "))

    for i in range(2):  #mathematically takes two checks to place numbers in order
        temporaryVariable = ''  #temperary variable initiated
        if value1 > value2:
            temporaryVariable = value1  #the temporary variable is replaced with value 1 (the greater value)
            value1 = value2     #value1, is set to be the smallest value, therefore value 2 is placed in its variable location
            value2 = temporaryVariable  #value two now equals value 1 (the greater value)
        if value2 > value3:
            temporaryVariable = value2 #the largest value is placed in the temporary variable spot
            value2 = value3 #The second largest value is placed in the value 2 spot
            value3 = temporaryVariable  #the greatest value, previously placed as a temporary variable, is now value 3
    print('The values in order are:',value1,',',value2,',',value3) #prints (smallest value, middle value, largest value) as per the code

def displayTriangle(numRows):
    numStars = str('*')  #numStars is set to equal '*"
    i = 1                 #because numStars begins with one star (*), i =1
    while i <= numRows: #the loop iterates including the last row value
        print(numStars)
        numStars += str('*') #for each new row another (*) is added to the string
        i += 1              #variable i increases to prevent infinite looping

def displayCheckerBoard(value):
    for Yvar in range(value):       #iterates through each column, and row
        for Xvar in range(value):
            if Xvar < value - 1:    #alternates rows and columns
                if (Xvar + Yvar) % 2 == 0:  #checking for even or odd (rows)
                    print('X ', end= '')    #prints X ending with space
                else:
                    print('O ', end= '')    #prints Y ending with space
        else:
            if(Xvar + Yvar) % 2 ==0:    #repeat code for columns
                print('X')
            else:
                print('O')


def findGrade(finalScore):

    if finalScore < 59.5:               #asks for grade percentage, and outputs grade based on given percent rounding up when necessary.
            print('your grade is an: F')
    elif 59.5 <= finalScore < 69.5:
            print('your grade is a: D')
    elif 69.5 <= finalScore <79.5:
            print('your grade is a: C')    #highly self explanatory
    elif 79.5 <= finalScore <89.5:
            print('your grade is a: B')
    elif 89.5 <= finalScore <=100:
            print('your grade is an: A')
    else:
            print('Error, try again')   #if a grade outside the domain (1-100) is given, the program outputs an error code


def findGrades():
    finalScore = float(input('Enter a grade (1-100), or press \'000\' to terminate: ')) #flag placed in input code
    while finalScore != 000:    #runs program until flag is inputed
        findGrade(finalScore)   #runs previously created final score module to identify the grade
        finalScore = float(input('Enter a grade (1-100), or press \'000\' to terminate: ')) #prompts the user to enter another score
    print('Thank you for using letter grade finder')

def findSum(value):
    newValue = str(value)   #turns the given integer value into a string
    total = 0           #sets total variable equal to 0
    for i in newValue:  #iterates over each character in the newly created string
        total += int(i) #changes each character back into an integer and adds it to variable "total"
    print(total)

def isPalindrome(string):
    temporaryVariable = ''  #sets temporary variable equal to zero
    for i in string:    #iterates over every character in the string
        temporaryVariable = i + temporaryVariable   #sets temporary variable as the reverse of the original string
        if string == temporaryVariable: #if the reverse of the string equals the original string
            print(string,'is a palindrome') #prints palindrome

    if string != temporaryVariable:
        print(string,'is not a palindrome') #else prints not...















#Write all your methods above this comment


def main():
    #sumOdds(int(input("Enter a value to sum odds too: "))) #good
    #characterCount(input("Enter a phrase to count the characters: ")) #good
    #multiplicationPractice()
    #testOrder()
    #displayTriangle(int(input("Enter the number of rows: ")))
    #displayCheckerBoard(int(input("Enter the size: ")))
    #findGrade(float(input("Enter a score to be assigned a grade: ")))
    #findGrades()
    #findSum(int(input("Enter a number to sum the digits of: ")))
    #isPalindrome(str(input("Enter a word to check if it's a palindrome: ")))
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()