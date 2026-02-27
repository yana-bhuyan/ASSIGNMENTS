n = int(input("Enter number of persons: "))
data = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    data[name] = city

print("Names:", list(data.keys()))
print("Cities:", list(data.values()))

for name, city in data.items():
    print(name, "->", city)

city_count = {}
for city in data.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Students in each city:", city_count)