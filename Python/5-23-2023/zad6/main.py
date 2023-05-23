def sumNumbersInFloat(floatNum):

    if not type(floatNum) is float:

        print("Number provided is not a float!")
        return
    
    stringified = str(floatNum)
    total = 0

    for v in stringified:

        try:

            total += int(v)

        except:

            continue

    return total

print(sumNumbersInFloat(4.57))