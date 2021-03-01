import numpy as np

numbersArray = np.array([1, 2, 3])
print(numbersArray)

numbersMatrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(numbersMatrix)

numbersZeros = np.zeros((4, 3))
print(numbersZeros)

numbersOnes = np.ones((4, 3))
print(numbersOnes)

numbersEye = np.eye(10)
print(numbersEye)
print(np.mean(numbersArray))
print(np.max(numbersArray))
print(np.min(numbersArray))
print(np.std(numbersArray))
