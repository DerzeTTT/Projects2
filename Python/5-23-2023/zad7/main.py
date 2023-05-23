import math

def jumpSearch(sortedList, lookingFor):

    n = len(sortedList)
    found = None

    increment = math.ceil(math.sqrt(n))

    for i in range(0, n-1, increment):

        divider = int(sortedList[i])

        if divider == lookingFor: return i

        if divider < lookingFor:

            for i2 in range(divider+1, n):

                if sortedList[i2] == lookingFor:

                    return i2
                
        else:

            for i2 in range(0, divider-1):

                if sortedList[i2] == lookingFor:

                    return i2
                
    return False

print("Found number on index:", jumpSearch([2,5,8,13,32], 8))