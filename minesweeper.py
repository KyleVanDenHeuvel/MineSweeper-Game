from random import randint

# Size of the map (10 by default)
size = 10
# Creates a matrix to store the map
game_map = []
# Creates a matrix to store where mines are located
game_mines = []
# Determines whether the game is over ("True" if the game is over)
game_over = False

#FIXME
'''
Allows the user to change the size of the map by accepting an
integer value and setting "size" equal to it.
'''
def set_size(int_size):
    size = int_size


'''
Instantiates game_map and mine_map to the size "size"
'''
def create_maps(int_size):
    # Initializes the matrix for game_map to size "int_size"
    for i in range(int_size):
        game_map.append(["O"] * int_size)

    # Initializes the matrix for game_mines to size "int_size"
    for i in range(int_size):
        game_mines.append(["O"] * int_size)


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
        rand_x = randint(0, len(map1) - 1)
        rand_y = randint(0, len(map1) - 1)
        if (map1[rand_y][rand_x] == "O"):
            map1[rand_y][rand_x] = "X"


'''
Allows the user to choose a position to step on the map by accepting
an x and y coordinate and placing it on the map.  If the player steps
on a mine, then the mine "explodes" and all of the other mines are
revealed--making the game now over.  If the player doesn't step on
a mine, they can proceed to make another step.
'''
def make_step(int_x, int_y):
    if(game_mines[int_y][int_x] == "X"):
        game_over = True
        print("\n\n")
        print_map(game_mines)
        print("\nGAME OVER")
    else:
        game_map[int_y][int_x] = "+"
        print("\n\n")
        print_map(game_map)
            

'''
Runs the game processes until the game is over (game_over == True).
Instantiates the maps, deploys mines, and utilizes the function
make_step to allow the player to take steps on the map.
'''
def game_run():
    create_maps(size)
    deploy_mines(game_mines)
    print_map(game_map)
    while(game_over != True):
        step_x = int(input("Step X: ")) - 1
        step_y = int(input("step Y: ")) - 1
        make_step(step_x, step_y)
        # DEBUGGING
        print("\n")
        print_map(game_mines)


# Testing - Full
game_run()


'''
# Testing

# Set map size to 8
    set_size(8)
# Print size of map
print(str(size))
print("\n")

# Instantiate the maps to size "size"
create_maps(size)

# Generate mines
deploy_mines(game_mines)

# Print game map
print("Game Map")
print_map(game_map)
print("\n")

# Print mine map
print("Mine map")
print_map(game_mines)
'''
