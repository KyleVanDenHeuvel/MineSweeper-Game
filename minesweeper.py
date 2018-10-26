# Size of the map
size = 10

# Creates a matrix of size "size" to store the map
game_map = []
# Creates a matrix of size "size" to store where mines are located
game_mines = []

# Initializes the matrix for game_map
for i in range(size):
    game_map.append(["[]"] * 10)

# Initializes the matrix for game_mines
for i in range(size):
    game_mines.append(["[]"] * 10)

'''
Prints out the matrix which holds the game map.  Can be used to
display both the game map and the mine map.
'''
def print_map(map1):
    for row in map1:
        print(" ".join(row))


print(str(size))
print_map(game_map)
