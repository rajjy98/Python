def displayScores(scoreArray):
    """Displays the current test scores"""
    print("The current test scores are:")
    for i in range(len(scoreArray) - 1):
        print(float(scoreArray[i]), end="%, ")
    print(float(scoreArray[len(scoreArray) - 1]), end="%\n")
    print()


def findMin(scoreArray):
    """ Iterates through scoreArray, returns minimum value"""
    minimum = scoreArray[0] #assings minimmum value
    for i in range(len(scoreArray)): #Loop iterating through each component in the list
        if scoreArray[i]< minimum: #if given value is less than the current minimum
            minimum = scoreArray[i] #given value becomes the minimum value
    return minimum


def findMax(scoreArray):
    """Iterates through ScoreArray, returns maximum value"""
    maximum = scoreArray[0] #assign maximum value
    for i in range(len(scoreArray)): #loop iterating through each component in the list
        if scoreArray[i] > maximum: #if given value is greater than the current maximum
            maximum = scoreArray[i] #given value becomes the maximum

    return maximum

def dropLowest(scoreArray):
    """Calls findMin function and removes the given minimum from scoreArray"""
    minimum = (findMin(scoreArray)) #calls function findMin to obtain smallest value in list
    scoreArray.remove(minimum) #removes said value
    scoreArray.sort(reverse=True) #required for 100 points (orders the list from greatest to least)
    addition = '.0%'
    tempList = [str(i) +addition for i in scoreArray] #turns each component from the list into a string and adds ".0%" to the end
    newList = str(tempList).replace('[', '').replace(']', '') #removes brackets -makes code identical to requirements
    finalList = str(newList).replace('\'', '') #removes quotation  -makes code identical to requirements

    return finalList

def getMean(scoreArray):
    """returns mean of score Array"""
    total = 0
    for i in range(len(scoreArray)):
        total += scoreArray[i]    # total = the addition of every grade in the string
    mean = total/(len(scoreArray)) # mean = total divided by the length of scoreArray

    return mean

def getMedian(scoreArray):
    """returns median of scoreArray"""
    scoreArray.sort()
    if len(scoreArray) % 2 == 0:    #if there are an even number of components in the list
        lowerDigit = int((len(scoreArray) - 1)/2) # lowerDigit = total number of components in scoreArray divided by two
        upperDigit = int(lowerDigit +1)          # upperDigit = lowerDigit + 1
        median = ((scoreArray[upperDigit] + scoreArray[lowerDigit])/2) # median = average of those numbers
    if len(scoreArray) % 2 != 0:    # if there are an odd number of components
        digit = int((len(scoreArray) / 2) - 0.5) #the length of scoreArray divided by two (would produce the middle float - 0.5 giving the exact middle integer
        median = (scoreArray[digit]) #scoreArray[middle integer]

    return median

def main():
    testScores = [90, 85, 52, 74, 95, 100, 78,]
    displayScores(testScores)
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    average = getMean(testScores)
    print('Average:', average)
    Median = getMedian(testScores)
    print('Median:', Median)

    print()
    minusLowest = dropLowest(testScores)
    print('After dropping the lowest score.')
    print('The current test scores are:')
    print(minusLowest)
    average = getMean(testScores)
    print('Average:',average)
    Median = getMedian(testScores)
    print('Median:', Median)





main()
input("\nPress enter to quit")