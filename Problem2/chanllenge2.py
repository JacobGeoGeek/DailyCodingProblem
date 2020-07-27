def productArray(Numbers):
    result = []
    Product = 1
    for x in range(len(Numbers)):
        for y in range(len(Numbers)):
            if x != y:
                Product = Product * Numbers[y]
        result.append(Product)
        Product = 1
    return result


NumbersFromProblemv1 = [1, 2, 3, 4, 5]
NumbersFromProblemv2 = [3, 2, 1]


print(productArray(NumbersFromProblemv1))
print(productArray(NumbersFromProblemv2))
