"""Funktioner
inparameter
anropa funktion
return-sats
lokala variabler
"""


import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2

print(f(5))
x=np.licenceplate(-10,10)
y=f(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x) = x**2")
plt.grid()
plt.show()