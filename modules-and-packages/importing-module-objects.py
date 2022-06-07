#importing module objects to the current namespace
from draw import draw_game

def play_game():
    ...

def main():
    result = play_game()
    #You may have noticed that in this example, the name of the module 
    # does not precede draw_game, because we've specified the module
    # name using the import command.
    draw_game(result)

