import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('iris.csv')

print(df.head())

sns.pairplot(df, hue="variety");
#plt.show()

X = df.iloc[:, 0:4]
Y = df.iloc[:, 4]

def testState(testingState):

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33, shuffle=True, random_state=testingState)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X=X_train, y=Y_train)

    correct = 0

    for iris_X, iris_Y, in zip(X_test.values, Y_test.values):

        print(iris_X, iris_Y)

        pred = model.predict([iris_X])[0]

        if pred == iris_Y:

            correct +=1

    return correct / len(X_test)

testedStates = []

for i in range(1,100):

    testedStates.append([testState(i), i]);

largest = [0,0];

for v in testedStates:

    if v[0] > largest[0]:

        largest = vx

print(largest)