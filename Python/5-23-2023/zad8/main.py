# Takes file1.txt, file2.txt
# list a string and check if index value is equal on both strings

file1, file2 = open('file1.txt', 'r').read(), open('file2.txt', 'r').read()

def getDifference(str1, str2):

    larger, smaller = None, None;

    if len(str1) >= len(str2):

        larger = str1
        smaller = str2
    
    else:

        larger = str2
        smaller = str1

    listed1, listed2 = list(larger), list(smaller)
    totalChars = len(larger)

    correct = 0

    for i in range(0, len(listed2)):

        if listed2[i] == listed1[i]:

            correct += 1

    percentage = (correct / totalChars) * 100

    return percentage

if file1 == file2:

    print('No difference in content')

else:

    print("Difference in between file content (%):", getDifference(file1, file2), sep="\n")