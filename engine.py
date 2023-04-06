import random

# Constants
EMPTY_SPACE = " "
WALL = "▄"
DOOR = "░"
COIN = "$"
WEAPON = "#"
MONSTER = "M"
HEAL = "H"
PLAYER_ICON = "@"
PLAYER_MONEY = 0
PLAYER_HP = 50
ATTACK = 20
MAP_WIDTH = 10
MAP_HEIGHT = 10
NUM_MAPS = 3
EMPTY = ' '

# Game state variables
current_map = 0
player_pos = [0, 0]
maps = []


def move(board, player, dx, dy):
    x, y = player
    new_x = x + dx
    new_y = y + dy
    if new_x < 0 or new_y < 0 or new_x >= len(board[0]) or new_y >= len(board):
        return player
    elif board[new_y][new_x] == "#":
        return player
    else:
        return (new_x, new_y)


def move_offsets(direction):
    """Return the x, y offsets corresponding to the given direction."""
    if direction == "w":
        return (0, -1)
    elif direction == "a":
        return (-1, 0)
    elif direction == "s":
        return (0, 1)
    elif direction == "d":
        return (1, 0)
    else:
        return (0, 0)
    

# Helper functions
def clear_screen():
    """Clear the console screen."""
    print("\033c", end="")

def create_board(width, height):
    """Create a new game board with walls around the edges."""
    board = [[WALL]*(width+2)]
    for i in range(height):
        board.append([WALL]+[EMPTY_SPACE]*width+[WALL])
    board.append([WALL]*(width+2))
    return board

def add_items(board, item, num_items):
    """Add a specified number of a given item to a game board at random positions."""
    for i in range(num_items):
        x = random.randint(1, len(board)-2)
        y = random.randint(1, len(board[0])-2)
        while board[x][y] != EMPTY_SPACE:
            x = random.randint(1, len(board)-2)
            y = random.randint(1, len(board[0])-2)
        board[x][y] = item

class Player:
    def __init__(self, icon, x, y, hp, attack_power, defense_power, money):
        self.icon = icon
        self.x = x
        self.y = y
        self.hp = hp
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.money = money

def add_monsters(board, num_monsters):
    """Add a specified number of monsters to a game board at random positions."""
    add_items(board, MONSTER, num_monsters)

def add_coins(board, num_coins):
    """Add a specified number of coins to a game board at random positions."""
    add_items(board, COIN, num_coins)

def add_weapons(board, num_weapons):
    """Add a specified number of weapons to a game board at random positions."""
    add_items(board, WEAPON, num_weapons)

def add_health_potions(board, num_potions):
    """Add a specified number of health potions to a game board at random positions."""
    add_items(board, HEAL, num_potions)

def get_input():
    """Get user input and return the corresponding action."""
    while True:
        action = input("Action: ")
        if action in ["w", "a", "s", "d", "q"]:
            return action
        elif action == "h":
            print("Move up: w\nMove left: a\nMove down: s\nMove right: d\nQuit: q\n")
        else:
            print("Invalid input. Type 'h' for help.")

def get_new_position(player_pos, action):
    """Get the new position of the player based on the action."""
    x, y = player_pos
    if action == "w":
        return [x, y-1]
    elif action == "a":
        return [x-1, y]
    elif action == "s":
        return [x, y+1]
    elif action == "d":
        return [x+1, y]
    else:
        return player_pos

def handle_collision(board, player_pos):
    """Obsługuje kolizje między graczem a innymi obiektami na planszy."""
    x, y = player_pos
    item = board[x][y]
    if item == COIN:
        player.money += 1
        print('Zebrano monetę!')
    elif item == WEAPON:
        player.attack_power += 5
        print('Znaleziono broń!')
    elif item == MONSTER:
        player.hp -= 10
        print('Zostałeś/aś zaatakowany/a przez potwora!')
    elif item == HEAL:
        player.hp += 10
        print('Znaleziono lecznicę!')
    elif item == DOOR:
        print('Znalazłeś/aś drzwi wyjściowe! Koniec gry.')
        return True
    return False


def put_player_on_board(board, player):
    """Umieszcza gracza na planszy."""
    board[player.x][player.y] = player.icon

