#Custom import name
#Modules may be loaded under any name you want. This is useful when importing 
# a module conditionally to use the same name in the rest of the code.
#For example, if you have two draw modules with slighty different names, you 
# may do the following:

visual_mode = True

if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)