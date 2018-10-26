# Size of the map
size = 10

# Creates a matrix of size "size" to store the map
game_map = []

for i in range(size):
    game_map.append(["0"] * 10)

def print_map(map1):
    for row in map1:
        print(" ".join(row))


print(str(size))
print_map(game_map)
