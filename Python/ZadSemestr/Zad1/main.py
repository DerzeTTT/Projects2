import random as ran
import time

import matplotlib.pyplot as plt
import numpy as np

lists = []
listSizes = [1000, 10_000, 15_000, 20_000, 30_000]

# Rozmiary sa mniejsze niz w przykladzie bo te wczesniejsze by za dlugo zajely dla przetestowania
# Moze pan je zamienic w zmiennej "listSizes"

for v in listSizes:

    newList = []

    for i in range(v):

        newList.append(ran.random()*100)

    lists.append(newList)

def bubbleSort(rawList):

    arr = rawList.copy()
    
    for i in range(len(arr)):
       
        for j in range(0, len(arr) - i - 1):
        
            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

def insertSort(rawList):

    arr = rawList.copy()

    if (n := len(arr)) <= 1:
      
      return
    
    for i in range(1, n):
         
        key = arr[i]
        j = i-1

        while j >=0 and key < arr[j] :
                
                arr[j+1] = arr[j]
                j -= 1

        arr[j+1] = key

    return arr

def bucketSort(rawList):

    arr = rawList.copy()

    maxValue = max(arr)
    size = maxValue/len(arr)

    buckets_list= []

    for x in range(len(arr)):

        buckets_list.append([]) 

    for i in range(len(arr)):

        j = int(arr[i] / size)

        if j != len(arr):

            buckets_list[j].append(arr[i])

        else:

            buckets_list[len(arr) - 1].append(arr[i])

    for z in range(len(arr)):

        insertSort(buckets_list[z])
            
    finalOutput = []

    for x in range(len(arr)):

        finalOutput = finalOutput + buckets_list[x]

    return finalOutput

v = lists[0]

def testSort(func, tList):

    oldTick = time.time()

    func(tList)

    timeDur = time.time()-oldTick

    print(f"{len(tList)} sample size took: {timeDur}")

    return timeDur

timed = {

    'bubble':[],
    'insert':[],
    'bucket':[]

}

def addToTimed(sortName, count, dur):

    timed.get(sortName).append({

        'tries':count,
        'duration':dur

    })

for v in lists:

    t1, t2, t3 = testSort(bubbleSort, v), testSort(insertSort, v), testSort(bucketSort, v)

    listLen = len(v)

    addToTimed('bubble', listLen, t1)
    addToTimed('insert', listLen, t2)
    addToTimed('bucket', listLen, t3)

fig, ax = plt.subplots()

ax.set(ylabel='Time(ms)', xlabel='Samples', title='Sorting algorithms sorting times')
ax.grid()

for sortName in ['bubble', 'insert', 'bucket']:

    data = timed.get(sortName)

    triesList = [t['tries'] for t in data]
    durList = [t['duration'] for t in data]

    ax.plot(triesList, durList, label=sortName)

ax.legend()

plt.show()