def sumOfTwoNumber(listNumber, sumResult):
    listNumber = sorted(listNumber)
    rightIndex = 0
    leftIndex = len(listNumber) - 1

    while(rightIndex < leftIndex):
        if sumResult == listNumber[rightIndex] + listNumber[leftIndex]:
            return (listNumber[rightIndex], listNumber[leftIndex])

        if (sumResult > listNumber[rightIndex] + listNumber[leftIndex]):
            rightIndex += 1

        if (sumResult < listNumber[rightIndex] + listNumber[leftIndex]):
            leftIndex -= 1

    return None


NumbersFromProblem = [10, 15, 3, 7]
ExpectedResult = 17

print(sumOfTwoNumber(NumbersFromProblem, ExpectedResult))
