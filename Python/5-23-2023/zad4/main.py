rawNumbers = input("Enter numbers (sep: space)\n")

total = 0

for v in str(rawNumbers).split(' '):

    total += int(v)

print(total)