class Artificial_Input:

    def __init__(self):

        self.Holding = [];
        self.Reading = 0;

        self.Production = False;

    def add_input(self, new_input, split_lines=True):

        Appending = None;

        if type(new_input) is str and split_lines:

            Appending = new_input.split("\n");

        elif type(new_input) is list:

            Appending = new_input;

        else:

            raise Exception("Given value is not a string or list!")

        self.Holding += Appending;

    def read(self):

        if not self.Production:

            Returning = self.Holding[self.Reading];
            self.Reading += 1;

            return Returning;
        
        else:

            return input();

Custom_Input = Artificial_Input();

Custom_Input.Production = True;

Custom_Input.add_input('''10
count
put Marek
put Janek
put Monika
count
get
get
put Darek
count
get''')

import queue

storeQueue = queue.Queue()

n = int(Custom_Input.read())

def runOperation(opName, pName):

    if opName == 'put':

        storeQueue.put(pName)

    elif opName == 'get':

        print(storeQueue.get(pName))
    
    elif opName == 'count':

        print(storeQueue.qsize())

for _ in range(n):

    rawCommand = str(Custom_Input.read())
    parts = rawCommand.split(' ')

    pName = None;

    if len(parts) > 1:

        pName = parts[1]

    runOperation(parts[0], pName)