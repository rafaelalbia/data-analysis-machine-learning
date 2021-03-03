import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1000, 1000, 1)
y = x**2
plt.plot(x, y)
plt.show()

y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.subplot(2, 2, 4)
plt.plot(x, y3)
plt.show()

y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3

figure = plt.figure(figsize=(10, 10))

figure.add_subplot(2, 2, 1)
plt.plot(x, y1)
figure.add_subplot(1, 2, 2)
plt.plot(x, y2)
figure.add_subplot(2, 2, 3)
plt.plot(x, y3)
plt.show()

y = [y1, y2, y3, y4]
for i in range(4):
    figure.add_subplot(2, 2, i+1)
    plt.plot(x, y[i])
plt.show()
