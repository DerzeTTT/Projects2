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

Custom_Input.Production = False;

Custom_Input.add_input('''5 3
10
100 3.54
101 4.28
102 5.0
103 1.51
104 3.33
105 1.78
106 4.91
107 4.22
108 4.17
109 4.17
5
200 4.00
201 3.97
202 2.12
203 1.87
204 1.56
2
300 1.98
301 5.23''')

import queue
import math

def bucketSort(rawList):

    min_range = 1.00
    max_range = 6.00
    n_buckets = 5
    size = max_range - min_range
    bucket_size = int((max_range - min_range) / n_buckets)

    arr = rawList.copy()
    buckets_list = [[] for _ in range(n_buckets)]

    for i in range(len(arr)):

        j = int((arr[i].grade - min_range) // bucket_size)
        buckets_list[j].append(arr[i])

    for z in range(n_buckets):

        buckets_list[z].sort(key=lambda x: x.grade)
            
    finalOutput = []

    for x in range(n_buckets):

        finalOutput = finalOutput + buckets_list[x]

    return finalOutput

line1 = Custom_Input.read().split(" ")

maxQueue, amountOfDays = int(line1[0]), int(line1[1])

class Student():

    def __init__(self, rawStr):

        splitted = rawStr.split(" ")

        self.id = int(splitted[0])
        self.grade = float(splitted[1])

days = []

def parseThroughDay():

    n = int(Custom_Input.read())
    students = []

    for i in range(n):

        students.append(Student(Custom_Input.read()))

    days.append(students)

for i in range(amountOfDays):

    parseThroughDay()

def processDay(students):
 
    sortedByGrade = bucketSort(students)

    print([s.grade for s in sortedByGrade])
    
    return sortedByGrade

for day in days:

    sortedStudents = processDay(day)