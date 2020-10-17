from typing import List


def findMissingPositiveNumber(listNumber: List[int]) -> int:

    for i in range(len(listNumber)):
        if listNumber[i] < 0:
            listNumber[i] = 0

    maxValue = max(listNumber)
    minValue = min(listNumber)

    for index in range(len(listNumber)):
        if listNumber[index] == maxValue:
            currentLastValue = listNumber[len(listNumber)-1]
            currentValue = listNumber[index]
            listNumber[len(listNumber)-1] = currentValue
            listNumber[index] = currentLastValue

        if listNumber[index] == minValue:
            currentLastValue = listNumber[0]
            currentValue = listNumber[index]
            listNumber[0] = currentValue
            listNumber[index] = currentLastValue

    return listNumber


if __name__ == "__main__":
    print(findMissingPositiveNumber([3, 4, -1, 1]))
    print(findMissingPositiveNumber([1, 2, 0]))
