def printAbout():
    print("LAMpy is a simple project to bring functionality of underscoe.js lib to python")
    pass


def first(array, length=0):
    try:
        tempList = []
        if(length == 0):
            return array[0]
        if(length > len(array)):
            length = len(array)
        for iterator in range(0, length):
            tempList.append(array[iterator])
        return tempList
    except Exception as details:
        print(details)


def initial(array, exclude=1):
    tempList = []
    if(len(array) == 1):
        return array[0]
    else:
        if(exclude >= len(array)):
            return None
        else:
            for iterator in range(len(array)-exclude):
                tempList.append(array[iterator])
    return tempList


def rest(array, skip=0):
    tempList = []
    if(skip >= len(array)):
        return None
    for iterator in range(skip, len(array)):
        tempList.append(array[iterator])
    return tempList


def checkIfContainsForbiddenWords(element, forbiddenWords):
    for forbiddenWord in forbiddenWords:
        if(element == forbiddenWord):
            return True
    return False


def compact(array, forbiddenWords=[" ", False, 0, None]):
    tempList = []
    for element in array:
        if(checkIfContainsForbiddenWords(element, forbiddenWords) is False):
            tempList.append(element)
    if(len(tempList) > 1):
        return tempList
    else:
        return tempList[0]


def without(*args):
    tempList = []
    passedArguments = list(args)
    forbiddenWords = []
    for element in range(1, len(passedArguments)):
        forbiddenWords.append(passedArguments[element])
    for iterator in passedArguments[0]:
        if(checkIfContainsForbiddenWords(iterator, forbiddenWords)):
            continue
        tempList.append(iterator)
    if(len(tempList) == 0):
        return None
    return tempList


def union(*args):
    tempList = []
    if(len(args)== 0):
        return None
    elif(len(args) == 1):

    return tempList
