kmh = [40, 50, 60, 70, 56, 73, 85, 99, 42, 68, 100, 120]

# 2: mph = list(map(lambda element : element / 1.61, kmh))

# 1: for element in kph:
# 1:     mph.append(element / 1.61)

mph = [element / 1.61 for element in kmh]

character = [element for element in "I'm a guy"]

print(mph)
print(character)
