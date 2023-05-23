# Takes file1.txt, file2.txt
# list a string and check if index value is equal on both strings

file1, file2 = open('file1.txt', 'r').read(), open('file2.txt', 'r').read()

def getDifference(str1, str2):

    larger, smaller = None, None

    if len(str1) >= len(str2):

        larger = str1
        smaller = str2
    
    else:

        larger = str2
        smaller = str1

    totalChars = len(larger)

    listed1, listed2 = list(larger), list(smaller)

    correct = 0
    difIndexes = {}

    count = 0

    for i in range(0, totalChars):

        try:

            if listed2[i] == listed1[i]:

                correct += 1

            else:

                difIndexes[i] = True

        except:

            difIndexes[i] = True

    difStr = ''

    for i in range(len(larger)):

        appending = ((difIndexes.get(i) and f'({listed1[i]})') or listed1[i])

        difStr += appending

    percentage = (correct / totalChars) * 100

    return (percentage, difStr)

if file1 == file2:

    print('No difference in content')

else:

    diff = getDifference(file1, file2)

    print("Difference in between file content (%):", diff[0], "Difference in text:", diff[1], sep="\n")