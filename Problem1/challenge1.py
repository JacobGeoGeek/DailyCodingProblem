def sumOfTwoNumber(listNumber, sumResult):
    for x in range(0, len(listNumber)):
        for y in range(1, len(listNumber)):
            if listNumber[x]+listNumber[y] == sumResult:
                return (listNumber[x], listNumber[y])
    return None


NumbersFromProblem = [10, 15, 3, 7]
ExpectedResult = 17

print(sumOfTwoNumber(NumbersFromProblem, ExpectedResult))
