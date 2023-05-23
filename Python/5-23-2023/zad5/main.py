def countLetters(tStr):

    counts = {}

    for v in list(tStr):

        if not counts.get(v): counts[v] = 0

        counts[v] += 1

    return counts

def checkForRepeating(str1, str2):

    letters1, letters2 = countLetters(str1), countLetters(str2)

    return letters1 == letters2

print(checkForRepeating("ko", "ok"))
print(checkForRepeating("halo", "hallo"))