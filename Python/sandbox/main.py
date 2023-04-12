fileName = input()
commandStrings = open(fileName, "r").read().split("\n")

maxSize = int(commandStrings[0])
newStack = []

class Commands():

    def get(self, splitted):

        if not newStack:

            print("empty")

            return
        
        print(newStack.pop())

    def put(self, splitted):

        if len(newStack) >= maxSize:

            print("full")
            return
        
        tName = splitted[1]
        newStack.append(tName)

    def count(self, splitted):

        print(len(newStack))

newCommands = Commands()
commandList = dir(newCommands)

failed = []

def parseCommand(raw):

    splitted = raw.split(" ")
    pCommand = splitted[0]

    if not pCommand in commandList: return

    try:

        getattr(newCommands, pCommand)(splitted)

    except:

        failed.append(raw)

for v in commandStrings[1:]:

    parseCommand(v)

if failed:

    print("unfinished commands:")

    for v in failed:

        print(v)
