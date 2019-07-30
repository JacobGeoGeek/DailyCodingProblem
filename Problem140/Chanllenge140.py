def countSort(arrayInt):
    minValue = min(arrayInt)
    maxValue = max(arrayInt)
    frequencyNumbers = [0]*((maxValue-minValue)+1)
    RangeNumbers = []
    output = []
    for i in range(minValue, maxValue+1):
        RangeNumbers.append(i)
    for i in range(len(arrayInt)):
        frequencyNumbers[arrayInt[i] -minValue] = frequencyNumbers[arrayInt[i]-minValue] + 1
    for i in range(len(frequencyNumbers)):
        if frequencyNumbers[i] == 1:
            output.append(RangeNumbers[i])
    return output


print(countSort([2, 4, 6, 8, 10, 2, 6, 10]))
