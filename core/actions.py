def BAY_WINDOW_F(game):
    """Bay window action handler"""
    if game.IS_VERB("LOOK-INSIDE"):
        if game.HERE == "WEST-OF-DOOR":
            game.TELL("You see the living room through the window.")
        elif game.IS_IN("GARDENER", "SOUTH-LAWN"):
            game.TELL("Through the bay windows the gardener, Mr. McNabb, can be seen ")
            game.TELL(game.PICK_ONE("LAWN-ACTIVITIES"))
            game.TELL(" on the south lawn.")
        else:
            game.TELL("You can see the south lawn.")
    
    elif game.IS_VERB("OPEN") and not game.IS_FSET("FOYER", "TOUCHBIT"):
        game.TELL("The window seems to be latched from the inside.")

def ROSE_F(game):
    """Rose action handler"""
    if game.IS_VERB("SMELL"):
        game.TELL("They smell nice.")
    elif game.IS_VERB("EXAMINE"):
        game.TELL("There are rows of yellow, red, pink, and white roses here.")
    elif game.IS_VERB("TAKE"):
        game.TELL(
            "Taking a rose would be most ungracious, and possibly dangerous if Mr. McNabb "
            "found out."
        )