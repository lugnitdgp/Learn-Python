# PowerSet.py
# Description: given an array of numbers, generates
# a power set

def findPowerSet(originalSet, index, currentSet, powerSet):
    if (index >= len(originalSet)):
        # add list to power set(convert list to tuple)
        powerSet.append(currentSet)
        return 

    # set where element was not added
    notAddedSet = currentSet[:]

    # append both sets
    currentSet.append(originalSet[index])

    # recursive call to other elements in originalSet
    findPowerSet(originalSet, index + 1, currentSet, powerSet)
    findPowerSet(originalSet, index + 1, notAddedSet, powerSet)


if __name__ == "__main__":
    print("in main file")
    testSet = [1, 2, 3]
    powerSet = []

    findPowerSet(testSet, 0, [], powerSet)

    print("Final Set = " + str(powerSet))
