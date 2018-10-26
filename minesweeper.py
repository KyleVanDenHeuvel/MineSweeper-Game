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


'''
Determines the number of mines that will be generated (15-20 mines)
and sets the locations of the mines in the mine map.
'''
def deploy_mines(map1):
    num_mines = randint(15, 21)
    mine_loc = []
    for i in range(num_mines):
        rand_x = randint(0, len(map1))
        rand_y = rantint(0, len(map1))
            

# Testing
print(str(size))
print("")
print("Game Map")
print_map(game_map)
print("\n")
print("Mine map")
print_map(game_mines)
