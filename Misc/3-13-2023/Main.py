import matplotlib.pyplot as plt
import numpy as np

def getVelocity(s,t):

    if t==0: return

    return s/t

t = np.arange(0, 5, 1/12)
s = []

v = []

km = 0;

for i in t:

    km += 20

    s.append(km)
    v.append(getVelocity(km, i))

plt.plot(t, v)

plt.title("Wykres v(t)")

plt.xlabel("t")
plt.ylabel("v")

plt.show()