newList = (3, 5, 7)
newTuple = (3, 5, 7)

print(type(newTuple), newTuple)

newTuple = list(newTuple)
newTuple[0] = 4
newTuple = tuple(newTuple)

print(type(newTuple), newTuple)
