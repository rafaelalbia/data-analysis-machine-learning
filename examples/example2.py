import random

cities = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
cities.append('Salvador')
choice = random.choice(cities)
print(choice)

for city in cities:
    print(city)
