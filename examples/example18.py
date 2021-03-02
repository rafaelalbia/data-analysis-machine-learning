import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array = np.arange(0, 1000, 1)

# graphic = plt.scatter(x, y)
# graphic = plt.show()

plt.plot(array, -array**3+4)
plt.show()
