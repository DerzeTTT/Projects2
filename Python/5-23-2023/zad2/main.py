def sumDivisibleByThree(tList):

    total = 0

    for v in tList:

        if v%3 == 0:

            total += v

    return total

print(sumDivisibleByThree([2,5,6,3,8,9]))