##############################################################################################################################
## Global variables
##############################################################################################################################
##  XXX This probably needs to be run on the __init__ routine to ensure these are loaded into the games global variable disctionary
def init_globals(game):
    """Initialize global variables"""
    game.SETG("WELCOMED", False)
    game.SETG("AT-READING", False)
    game.SETG("LOBLO-FLAG", False)
    game.SETG("GARDENER-NO-REPLY", False)
    game.SETG("GARDENER-ANGRY", False)
    game.SETG("G-I-G", False)
    game.SETG("PRESENT-TIME", 480)  # 9AM
    game.SETG("WILL-TIME", 0)
    game.SETG("HC-ROBNER", False)
    game.SETG("CORPSE-SEEN", False)
    game.SETG("DUNBAR-DEAD", False)
    game.SETG("TUNE-ON", None)  # Currently playing tune

    # Lists for random activities
    game.SETG("LAWN-ACTIVITIES", [
        "picking weeds",
        "mowing the grass",
        "wiping his brow",
        "examining his work"
    ])
    
    game.SETG("GARDEN-ACTIVITIES", [
        "planting seeds",
        "cutting fresh flowers",
        "pruning stems"
    ])

    game.SETG("HOLE-SHOWN", False)
    game.SETG("HOLE-TELL", False)
    game.SETG("RST", 0)
    game.SETG("FRAGMENT-FLAG", False)
    game.SETG("FRAGMENT-CLEANED", False)
    game.SETG("FRAGMENT-FELT", False)
    game.SETG("FRAGMENT-FOUND", False)
    game.SETG("GARDENER-SHOW", False)
    game.SETG("ROSE-DIGS", [
        "You are making quite a mess, but you do run across some tiny pieces of a hard, shiny substance, which drop from your fingers and back onto the ground.",
        "Although everything is coming up roses, you haven't found anything unusual except for a few pieces of a hard substance which fall back to the ground."
    ])

    game.SETG("GARDEN-MUMBLES", [
        "rose garden",
        "fruit trees",
        "weather",
        "snootiness of city slickers",
        "intricacies of weeding"
    ])
    
    game.SETG("WHY-ME", [
        "\"You can do that yourself.\"",
        "\"Do it yourself!\"",
        "\"Why not do it yourself?\""
    ])
    
    game.SETG("PEN-SEEN", False)

    game.SETG("BAXTER-ANNOYED", [
        "show me useless items",
        "pick up every item in the house and show it to me"
    ])

    game.SETG("HO-HUMS", [
        " is standing here."
    ])
    
    game.SETG("NOTE-READ", False)
    game.SETG("B-NOTE", False)
    game.SETG("B-FOCUS", False)
    game.SETG("G-CALENDAR", False)
    game.SETG("WILL-READING", 720)  # Constant value for will reading time
    game.SETG("LADDER-FLAG", False)
    game.SETG("WILL-READY", False)
    
    game.SETG("YUKS", [
        "Don't be ridiculous.",
        "Surely you jest.",
        "You can't be serious!"
    ])
    
    game.SETG("G-LETTER", False)
    game.SETG("CALENDAR-PAGE", 7)
    game.SETG("P-ADVERB", False)
    game.SETG("NEWSPAPER-READ", False)
    game.SETG("ROURKE-MAIL", False)

    game.SETG("WILL-WAIT", 0)
    game.SETG("WILL-HOLD", False)
    game.SETG("POST-WILL", False)
    game.SETG("GEORGE-SEQUENCE", False)
    game.SETG("GEORGE-WAIT", False)
    game.SETG("GEORGE-READY", False)
    game.SETG("GEORGE-SCREAM", False)
    game.SETG("GEORGE-FOLLOW", False)

    game.SETG("GEORGE-SEARCH", 0)
    game.SETG("GEORGE-RUN", 0)
    game.SETG("BOOKS-MOVED", False)

    game.SETG("SAFE-SEEN", False)
    game.SETG("NEW-WILL-SEEN", False)
    game.SETG("CALL-RING", False)
    game.SETG("GEORGE-MOVES-BOOKS", False)

    game.SETG("CALL-IN-PROGRESS", False)
    game.SETG("CALL-WAITING", False)
    game.SETG("CALL-MOVE", False)
    game.SETG("CALL-OVERHEARD", False)
    game.SETG("ROBNER-OLD-LOC", False)
    game.SETG("ENVELOPE-OPENED", False)

    game.SETG("MR-ENVELOPE", False)
    game.SETG("BUTTON-REVEALED", False)
    game.SETG("CHINA-EXAMINED", False)
    
    # Corridor tables
    game.SETG("COR-1", [
        "P?WEST", "P?EAST",
        "CORRIDOR-4", "CORRIDOR-3", "CORRIDOR-2", "CORRIDOR-1", "STAIR-TOP", 0
    ])
    game.SETG("COR-2", [
        "P?NORTH", "P?SOUTH",
        "STAIR-TOP", "SHALL-11", 0
    ])
    game.SETG("COR-4", [
        "P?WEST", "P?EAST",
        "SHALL-11", "SHALL-12", 0
    ])
    game.SETG("COR-8", [
        "P?SOUTH", "P?NORTH",
        "FOYER", "NFOYER", "CORNER", 0
    ])
    game.SETG("COR-16", [
        "P?NORTH", "P?SOUTH",
        "STAIR-BOTTOM", "SHALL-1", 0
    ])
    game.SETG("COR-32", [
        "P?WEST", "P?EAST",
        "WEST-LAWN", "WEST-OF-DOOR", "FRONT-PATH", "EAST-OF-DOOR", "EAST-LAWN", 0
    ])
    game.SETG("COR-64", [
        "P?NORTH", "P?SOUTH",
        "EAST-SIDE", "EAST-OF-DOOR", "SOUTH-LAWN", 0
    ])
    game.SETG("COR-128", [
        "P?NW", "P?SE",
        "NORTH-LAWN", "ORCHARD", "EAST-LAWN", 0
    ])
    game.SETG("COR-256", [
        "P?WEST", "P?EAST",
        "NFOYER", "STAIR-BOTTOM", "STAIRS", 0
    ])
    game.SETG("COR-512", [
        "P?WEST", "P?EAST",
        "GUEST-ROOM", "EAST-LAWN", 0
    ])
    game.SETG("COR-1024", [
        "P?NORTH", "P?SOUTH",
        "UPSTAIRS-CLOSET", "CORRIDOR-2", 0
    ])
    game.SETG("COR-2048", [
        "P?WEST", "P?EAST",
        "ROSE-GARDEN", "ORCHARD", 0
    ])

    game.SETG("LADDER-POSITIONED", False)
    game.SETG("ANALYSIS-GOAL", False)
    game.SETG("ANALYSIS-OBJ", False)

    game.SETG("STUB-D", False)
    game.SETG("STUB-B", False)
    game.SETG("STUB-DX", False)
    game.SETG("STUB-BX", False)

    game.SETG("D-S-BAXTER-LOC", False)
    game.SETG("DUNBAR-ACCUSED", False)
    game.SETG("DUNBAR-BAXTER-MEET", False)
    game.SETG("STUB-DROPPED", False)
    game.SETG("SECRET-MEETING", 0)
    game.SETG("MEETING-INTERRUPTED", False)

    game.SETG("BAXTER-SEQ-LOC", False)
    game.SETG("LADDER-FLAG-2", False)
    game.SETG("DUNBAR-DEAD", False)
    game.SETG("SHOT-FIRED", False)
    game.SETG("BAXTER-SEEN", False)
    game.SETG("SHOT-COUNT", 0)
    game.SETG("SHOW-WAIT", 0)
    game.SETG("NO-SHOW", False)

    game.SETG("CONTRADICTION", False)
    
    game.SETG("DRUNK-FLAG", False)
    game.SETG("STEREO-ON", False)
    game.SETG("TUNE-ON", False)

    game.SETG("RECORD-TABLE", [
        "Hungarian Rhapsody",
        "march by Sir Edward Elgar",
        "chorus of African tribal music",
        "Hebrew prayer service",
        "Pretenders concert",
        "cacophonous electronic jumble",
        "bluegrass tune"
    ])
    
    game.SETG("TAPE-TABLE", [
        "Wagnerian opera",
        "New Orleans jazz band",
        "Bulgarian shepherdess song",
        "Navajo night chant",
        "simulated rain shower",
        "risque Russian drinking song"
    ])
    
    game.SETG("MURDER-TABLE", [
        0,
        0,
        "\"Murder? My dear inspector, I believe you are reading too many bad detective "
        "stories. It's clear that he committed suicide.\"",
        "Ms. Dunbar turns toward you, looking quite confused. \"Murder? But...but how "
        "do you know it was murder? I'm sure...\" She stops short, looking frightened.",
        "\"My father killed himself, as everyone knows. Please leave me alone.\"",
        "\"That's odd that you should say murder. Surely you don't suspect foul play, "
        "Inspector. My husband was devoted to his business, and its decline led him to "
        "take his life. The whole affair is tragic enough without your melodramatic "
        "insinuations.\"",
        "\"Was it a murder, then?\" She bounces with excitement. \"In the book I've "
        "been reading, the jealous wife did it, but I don't know about this. A whole "
        "batch of suspects, this group here. What do you know? A murder. Here!\" Her "
        "enjoyment is barely concealed.",
        0
    ])



##############################################################################################################################
## Door Action Functions
##############################################################################################################################
def DDESC(game, STR1, DOOR, STR2):
    """Describe with door state - prints text with door open/closed status"""
    game.TELL(STR1)
    if game.IS_FSET(DOOR, "OPENBIT"):
        game.TELL("open")
    else:
        game.TELL("closed")
    game.TELL(STR2)


def BALCONY_DOOR_F(game):
    """Balcony door action handler"""
    if game.IS_VERB("HIDE-BEHIND"):
        if not game.IS_SET(game.PRSO, "OPENBIT"):
            game.TELL("You open the balcony door carefully.")
            game.FSET(game.PRSO, "OPENBIT")
        
        if game.HERE == "LIBRARY":
            game.GOTO("LIBRARY-BALCONY")
        elif game.HERE == "LIBRARY-BALCONY":
            game.GOTO("LIBRARY")
        elif game.HERE == "MASTER-BEDROOM":
            game.GOTO("BEDROOM-BALCONY")
        else:
            game.GOTO("MASTER-BEDROOM")
        return True
        
    if game.VERB("LOOK-INSIDE"):
        if game.HERE in ["MASTER-BEDROOM", "LIBRARY"]:
            game.TELL("You can see the balcony, but not much beyond.")
        elif game.HERE == "LIBRARY-BALCONY":
            game.TELL("You can see into the library from here.")
        else:
            game.TELL("You can see the bedroom from here.")

def MASTER_BEDROOM_DOOR_F(game):
    """Master bedroom door action handler"""
    if game.VERB("LISTEN") and game.VAR("CALL-IN-PROGRESS"):
        game.TELL("You can hear the muffled voice of Mrs. Robner through the door.")
        return True
    
    if game.VERB("KNOCK"):
        if game.GETG("CALL-IN-PROGRESS"):
            game.TELL("Mrs. Robner calls out. 'Wait just one minute!'")
            return True
        else:
            return game.DOOR_F()

def DOOR_F(game):
   if game.VERB("LISTEN"):
      game.TELL("You can't hear anything through the door.")
      return True

   if game.VERB("KNOCK"):    
       if game.PRSO == "FRONT-DOOR" and not game.GETG("WELCOMED") and game.PRESENT_TIME < 700 and game.HERE == "FRONT-PATH":
           game.TELL("You hear footsteps inside the house. Mrs. Robner, dressed in black, opens the door and greets you.")
           game.WELCOME()
       elif game.IS_INHABITED(DOOR_ROOM()):
           game.TELL("A muffled voice says, \"Come in!\"")
       else:
           game.TELL("There is no answer at the door.")
       return True

   return False

def DOOR_ROOM(game):
    """Get room associated with door"""
    if game.PRSO == "MASTER-BEDROOM-DOOR":
        return "MASTER-BEDROOM"
    elif game.PRSO == "GEORGE-DOOR":
        return "GEORGE-ROOM"
    elif game.PRSO == "DUNBAR-DOOR":
        return "DUNBAR-ROOM"
    elif game.PRSO == "ROURKE-DOOR":
        return "ROURKE-ROOM"
    
def WELCOME(game):
    """Welcome routine when Mrs. Robner greets the player"""
    game.TELL(
        "\"Hello,\" she says, \"I'm Mrs. Robner. Please come in. I'm afraid I really "
        "can't help you much. This is surely a terrible waste of time, not to mention "
        "upsetting, having all these police marching around the house. This has been a "
        "trying time, as I suppose you can understand. As I told Mr. Coates and the "
        "other detective, you may look around but you must be out by 8 o'clock at the "
        "latest. Oh, I almost forgot...Mr. Coates will be reading my husband's will at "
        "noon in the living room. You may attend if you wish.\""
    )
    game.SETG("WELCOMED", True)
    game.REMOVE("MRS-ROBNER")
    
    if game.HERE == "FRONT-PATH":
        game.TELL("\nMrs. Robner leads you into the house and closes the door behind you.\n")
        game.GOTO("FOYER")
    
    game.MOVE("MRS-ROBNER", "FOYER")
    game.TELL(
        "\"I'm going to make myself some breakfast now. I'll be around all day if you "
        "need anything. I'll do what I can to help. Good day!\""
    )
    game.FCLEAR("FRONT-DOOR", "OPENBIT")
    game.ESTABLISH_GOAL("MRS-ROBNER", "KITCHEN")


def IS_INHABITED(game, RM):
    """Check if room is inhabited by a person"""
    # Get the first object contained in the room
    F = game.GET_FIRST_IN(RM)
    if not F:
        return False
    
    while True:
        if game.IS_FSET(F, "PERSON"):
            return True
        # Get the next object also in the same container (room)
        F = game.GET_NEXT_IN(F)
        if not F:
            return False
        

def WEST_DOOR_F(game, RARG=None):
    """West door action handler"""
    if (RARG == "M-BEG" and 
        game.IS_VERB("WALK") and 
        game.PRSO in ["P?NE", "P?NORTH"] and 
        game.IS_IN("LADDER", "PLAYER")):
        game.TELL(NO_LADDERS)


##############################################################################################################################
## Room Action Functions
##############################################################################################################################

# Global constant
NO_LADDERS = "You've got to be crazy, carrying that ladder inside the house!"

def FRONT_PATH_F(game, RARG=None):
    """Front path action handler"""
    if (RARG == "M-BEG" and 
        game.IS_VERB("WALK") and 
        game.PRSO == "P?NORTH" and 
        game.IS_IN("LADDER", "PLAYER")):
        game.TELL(NO_LADDERS)
    
    elif RARG == "M-LOOK":
        DDESC(game, "You are at the Robners' front door, which is ", "FRONT-DOOR", ".")
        game.TELL(
            "You can walk around the house from here to the east or west. To the south a "
            "rolling lawn leads to the entrance of the estate."
        )


def ROSE_GARDEN_F(game, RARG=None):
    """Rose garden action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "You are at the edge of a large rose garden, meticulously maintained by the "
            "gardener, Mr. McNabb. He is said to be exceedingly proud of this particular "
            "garden, which is the envy of the neighbors. Rows of roses are neatly arranged "
            "and the sweet fragrance of the flowers is worth a trip here in itself. An "
            "orchard to the east contains many varieties of fruit trees and wide lawns lie "
            "to the west and north. The roses themselves are to the south, filling the area "
            "between you and the back of the house."
        )


def IN_ROSES_F(game, RARG=None):
    """In roses action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "You are among rows of roses. The ground is soft, and your footsteps leave "
            "a rather bad impression as many poor seedlings are trampled underfoot. A "
            "safer place to admire the flowers lies to the north. A window to the south "
            "allows a view into the house."
        )
        
        if not game.GETG("LADDER-FLAG"):
            game.TELL("There is no way into the house from here.")
        else:
            game.TELL(
                "A ladder is leaning against the house, its upper end against a balcony "
                "above."
            )
        
        if not game.IS_FSET("HOLE", "INVISIBLE"):
            game.TELL("There are holes in the soft dirt near your feet.")
        
        return True
    
    elif (RARG == "M-ENTER" and 
          not game.GETG("GARDENER-ANGRY") and 
          not game.GETG("GARDENER-SHOW") and 
          game.LOC("GARDENER") in ["ROSE-GARDEN", "NORTH-LAWN", "WEST-LAWN"]):
        
        game.TELL(
            "In the distance you hear \"Hey! WHAT? You, there!\" and other choice words "
            "muffled by a strong Scottish burr and a stiff breeze. Now, standing at the "
            "edge of the garden, can be seen the person of Mr. Angus McNabb, the gardener. "
            "He advances, looking crazed and gesticulating wildly. With each carefully "
            "chosen step in your direction, a barely visible wince of pain comes to his "
            "deeply-lined face. He regards you as you would regard the man whose car "
            "just ran over your little puppy dog."
        )
        
        if game.GETG("G-I-G"):
            game.TELL(
                "\"I canna believe it! I've already spent an hour fixing up the ground "
                "here where some fool was walkin' aboot--and now you! I canna believe it!\""
            )
        
        game.SETG("GARDENER-ANGRY", True)
        game.SETG("GARDENER-NO-REPLY", True)
        game.ENABLE(game.QUEUE("I-GARDENER-CALM", 90))
        game.MOVE("GARDENER", game.HERE)

def IN_ORCHARD_F(game, RARG=None):
    """In orchard action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "You are amidst lovely trees bearing apples, pears, peaches, and other fruits. "
            "A grape arbor and several berry bushes may also be seen. The kitchen window "
            "and east side of the house are just to your south, and a path skirts the "
            "orchard to your north."
        )
        
        if game.GETG("LADDER-FLAG-2"):
            game.TELL("A ladder is leaning against the balcony above.")
        else:
            game.TELL("There is no way into the house from here.")

def I_GARDENER_CALM(game):
    """Gardener calming routine"""
    game.SETG("GARDENER-NO-REPLY", False)


def FOYER_F(game, RARG=None):
    """Foyer action handler"""
    if RARG == "M-ENTER":
        if not game.GETG("WELCOMED") and game.GETG("PRESENT-TIME") < 700:
            game.TELL("Mrs. Robner appears, walking down a hallway from the north.")
            WELCOME(game)
    
    elif RARG == "M-LOOK":
        DDESC(
            game,
            "This is the foyer of the Robner house, beautifully appointed with a fine "
            "crystal chandelier, marble floors, and a large marble-topped table. The front "
            "door, to the south, is ",
            "FRONT-DOOR",
            ". The foyer continues north."
        )

def SHALL_1_F(game, RARG=None):
    """South hallway 1 action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "You are in an east-west hallway south of the staircase. A door to the south "
            "is ",
            "ROURKE-DOOR",
            "."
        )


def SHALL_2_F(game, RARG=None):
    """South hallway 2 action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "This is the end of the east-west hallway. To the south a small door "
            "is ",
            "SOUTH-CLOSET-DOOR",
            "."
        )
        DDESC(
            game,
            "Another door, to the east, is ",
            "ROURKE-BATH-DOOR",
            "."
        )


def ROURKE_ROOM_F(game, RARG=None):
    """Rourke's room action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "This is the bedroom of the housekeeper, Mrs. Rourke, and is very simply "
            "furnished. A single bed, flanked by bare wooden end tables, sits below a "
            "closed window on the south end of the room. The floor is hardwood, with no "
            "rug. The only exit is a door to the north, which is ",
            "ROURKE-DOOR",
            "."
        )


def ROURKE_BATH_F(game, RARG=None):
    """Rourke's bathroom action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "This is Mrs. Rourke's bathroom. Aside from the usual bathroom fixtures "
            "are two shelves affixed to the wall. The door at the west side of the "
            "room is ",
            "ROURKE-BATH-DOOR",
            "."
        )


def LIVING_ROOM_F(game, RARG=None):
    """Living room action handler"""
    if RARG == "M-LOOK":
        game.SETG("WELCOMED", True)
        DDESC(
            game,
            "This is a large and impressive room, whose furnishings bespeak the great "
            "personal wealth of the Robners. The south side of the room is a large bay "
            "window, now ",
            "BAY-WINDOW",
            ", which looks out onto the front yard."
        )
        game.TELL(
            "A wood pile sits beside a huge fieldstone fireplace. A double doorway leading "
            "to the main hall is the only exit. Pictures of Mrs. Robner's colonial ancestors "
            "line one wall. The room contains formal seating for at least fifteen people, "
            "in several groups of chairs and couches. Tables and cabinets, all of the "
            "finest mahogany and walnut, complete the furnishings. On one of the tables is "
            "a telephone."
        )

def CORRIDOR_1_F(game, RARG=None):
    """Corridor 1 action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "You are just west of the staircase. There are doors on both sides (north and "
            "south) of the hallway, which continues west. "
        )
        
        if game.IS_FSET("DUNBAR-DOOR", "OPENBIT"):
            if game.IS_FSET("MASTER-BEDROOM-DOOR", "OPENBIT"):
                game.TELL("Both doors are open.")
            else:
                game.TELL("The door to the south is open.")
        elif game.IS_FSET("MASTER-BEDROOM-DOOR", "OPENBIT"):
            game.TELL("The door to the north is open.")
        else:
            game.TELL("Both doors are closed.")


def CORRIDOR_3_F(game, RARG=None):
    """Corridor 3 action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "This section of hallway is near the west end. Through the window at the end "
            "of the hall you can see some trees and the lake beyond. The hallway continues "
            "east and west, and a door to the south is ",
            "GEORGE-DOOR",
            "."
        )

def CORRIDOR_4_F(game, RARG=None):
    """Corridor 4 action handler"""
    if RARG == "M-ENTER" and game.GETG("PRESENT-TIME") == game.GETG("GEORGE-RUN") + 1:
        game.TELL(
            "As you enter the hallway, you catch a glimpse of George "
            "running down the stairs."
        )
        return False
    
    elif RARG == "M-LOOK":
        game.TELL(
            "This is the west end of the upstairs hall. To the north is the library, "
            "where Mr. Robner was found. Its solid oak door has been knocked down and "
            "is lying just inside the entrance to the library. A window which cannot "
            "be opened is at the end of the hallway."
        )


def LIBRARY_F(game, RARG=None):
    """Library action handler"""
    game.SETG("WELCOMED", True)
    
    if RARG == "M-LOOK":
        game.TELL(
            "This is the library where Mr. Robner's body was found. It is decorated in a "
            "simple but comfortable style. Mr. Robner obviously spent a great deal of time "
            "here. A wide executive desk sits before tall balcony windows which lie at the "
            "north of the room. A telephone is sitting on the desk. The east side of the "
            "room is composed of three large bookshelf units containing numerous volumes "
            "on many topics. The floor is carpeted from wall to wall. The massive oak door "
            "which blocked the entrance has been forcibly knocked off its hinges and is "
            "lying by the doorway."
        )
        
        if game.IS_FSET("LIBRARY-BALCONY-DOOR", "OPENBIT"):
            game.TELL("The window to the balcony has been opened.")
        
        if game.IS_FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.TELL(
                "The bookshelf unit on the far left has been swung open, "
                "revealing a room behind it!"
            )
        
        return True

def LIBRARY_BALCONY_F(game, RARG=None):
    """Library balcony action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "The balcony is bare of furniture, though it has a beautiful view of the rose "
            "garden, the north lawn and the lake. A metal railing around the balcony "
            "prevents an accidental drop to the thorny roses below. The window between the "
            "balcony and the library is ",
            "LIBRARY-BALCONY-DOOR",
            "."
        )
        
        if game.GETG("LADDER-FLAG"):
            game.TELL("The top of a ladder is resting on the metal railing.")
        
        if game.IS_IN("GARDENER", "ROSE-GARDEN"):
            game.TELL("Mr. McNabb is tending to the roses.")
        elif game.IS_IN("GARDENER", "NORTH-LAWN"):
            game.TELL(
                "Away to the north, Mr. McNabb can be seen " +
                game.PICK_ONE("LAWN-ACTIVITIES") + "."
            )
        
        return True
    

def HIDDEN_CLOSET_F(game, RARG=None):
    """Hidden closet action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "This is a secret room situated between the library and the master bedroom. "
            "The room is bare and somewhat dusty, as if it were not often used. An "
            "unmarked switchplate surrounds two buttons, one blue and one red. A formidable "
            "safe is embedded in the south wall."
        )
        
        if game.IS_FSET("SAFE", "OPENBIT"):
            game.TELL(" The heavy safe door is wide open.")
        
        game.CRLF()
        
        if game.IS_FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.TELL("The library can be seen through a door to the west.")
        elif game.IS_FSET("HIDDEN-DOOR-B", "OPENBIT"):
            game.TELL("The master bedroom can be seen through a door to the east.")
        
        return True

def RED_BUTTON_F(game):
    """Red button action handler"""
    if game.IS_VERB("PUSH"):
        if game.IS_FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.FCLEAR("HIDDEN-DOOR-L", "OPENBIT")
            game.TELL("The wall to the west silently closes.")
        else:
            game.FSET("HIDDEN-DOOR-L", "OPENBIT")
            game.TELL(
                "The wall to the west swings open, revealing the library on the other "
                "side."
            )


def BLUE_BUTTON_F(game):
    """Blue button action handler"""
    if game.IS_VERB("PUSH"):
        if game.IS_FSET("HIDDEN-DOOR-B", "OPENBIT"):
            game.FCLEAR("HIDDEN-DOOR-B", "OPENBIT")
            game.TELL("The wall to the east swings closed.")
        else:
            game.FSET("HIDDEN-DOOR-B", "OPENBIT")
            game.TELL(
                "The wall to the east swings open, revealing the master bedroom on the "
                "other side."
            )
            
            if not game.GETG("HC-ROBNER") and game.IS_IN("MRS-ROBNER", "MASTER-BEDROOM"):
                game.TELL(
                    "Mrs. Robner, sitting on her bed, appears stunned. She walks over and peeks "
                    "in, speaks of her complete surprise at the presence of such a place, and "
                    "returns to her bed, somewhat shaken."
                )
                game.SETG("HC-ROBNER", True)
            
            return True
        
def MASTER_BEDROOM_F(game, RARG=None):
    """Master bedroom action handler"""
    if RARG == "M-ENTER" and game.GETG("BAXTER-SEQ-LOC") == "MASTER-BEDROOM":
        game.TELL(
            "As you walk through the door, there is an explosion from in front of you! "
            "The impact of the bullet knocks you to the ground, stunned. You struggle, "
            "trying to look up. Another explosion! You fall back, into a long silence."
        )
        game.QUIT()
    
    elif RARG == "M-LOOK":
        DDESC(
            game,
            "This is the Robners' master bedroom, decorated in the Queen Anne style. A "
            "large four-poster bed with paired end tables fills the south end of the room. "
            "On one of the end tables is a telephone. Dressers, a small chair, and a lounge "
            "are against the walls. The north wall contains a balcony window, which is ",
            "BEDROOM-BALCONY-DOOR",
            ". An open doorway leads east to the bathroom. A large mirror with a gilt frame "
            "hangs on the west wall."
        )
        
        if game.IS_FSET("HIDDEN-DOOR-B", "OPENBIT"):
            game.TELL(
                "Part of the west wall has been swung away, revealing a hidden closet."
            )
        
        return True
    


def BEDROOM_BALCONY_F(game, RARG=None):
    """Bedroom balcony action handler"""
    if RARG == "M-ENTER" and game.GETG("BAXTER-SEQ-LOC") == "BEDROOM-BALCONY":
        game.TELL(
            "As you enter the balcony, there is an explosion and a burst of flame from "
            "your left. The pain freezes you for a moment as everything becomes black. "
            "While you await a choir of angels, a short chuckle and the sound of running "
            "feet are the last you hear."
        )
        game.QUIT()
    
    elif RARG == "M-LOOK":
        DDESC(
            game,
            "This balcony is atop the orchard, with the tallest of the fruit trees rising "
            "to about the level of the balcony. A metal railing surrounds the balcony, "
            "preventing a precipitous descent. A glass door leading to the master bedroom "
            "is ",
            "BEDROOM-BALCONY-DOOR",
            "."
        )
        
        if game.GETG("LADDER-FLAG-2"):
            game.TELL("The top of a ladder is visible here, leaning on the railing.")
        
        return True

def SHALL_11_F(game, RARG=None):
    """South hallway 11 action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "The hallway turns a corner here and continues east. To the north is the "
            "head of the stairs. A door to the south is ",
            "DUNBAR-BATH-DOOR",
            "."
        )

def DUNBAR_BATH_F(game, RARG=None):
    """Dunbar bathroom action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "This bathroom contains the usual sink, toilet, and bath. A medicine "
            "cabinet, "
        )
        
        if game.IS_FSET("DUNBAR-CABINET", "OPENBIT"):
            game.TELL("lying partially open")
        else:
            game.TELL("closed")
        
        DDESC(
            game,
            ", is above the sink. A door to the north is ",
            "DUNBAR-BATH-DOOR",
            "."
        )


def DUNBAR_ROOM_F(game, RARG=None):
    """Dunbar's room action handler"""
    if RARG == "M-ENTER" and game.GETG("DUNBAR-DEAD"):
        game.SETG("CORPSE-SEEN", True)
    
    elif RARG == "M-LOOK":
        DDESC(
            game,
            "This is Ms. Dunbar's room. It is furnished in the usual style, with a few "
            "additions indicative of Ms. Dunbar's taste. The bedroom door is ",
            "DUNBAR-DOOR",
            "."
        )

def GEORGE_BATH_F(game, RARG=None):
    """George's bathroom action handler"""
    if RARG == "M-LOOK":
        DDESC(
            game,
            "This is George's bathroom, with all the appropriate fixtures. Shaving gear "
            "sits near the sink. The door, to the west, is ",
            "GEORGE-BATH-DOOR",
            "."
        )

def GEORGE_ROOM_F(game, RARG=None):
    """George's room action handler"""
    if RARG == "M-LOOK":
        game.TELL(
            "This is George's bedroom. In addition to the normal furnishings, there "
            "is a small liquor cabinet, and a stereo with records and tapes. The door, "
            "leading to the hallway to the north, is "
        )
        
        if game.IS_FSET("GEORGE-DOOR", "OPENBIT"):
            game.TELL("open")
        else:
            game.TELL("closed")
        
        DDESC(
            game,
            ". Another door, to the east, is ",
            "GEORGE-BATH-DOOR",
            "."
        )
        
        if game.GETG("TUNE-ON"):
            game.TELL("Playing on the stereo is a " + game.GETG("TUNE-ON") + ".")
        
        return True
        



##############################################################################################################################
## Local Global Functions
##############################################################################################################################

def LAWN_F(game):
    """Lawn action handler"""
    if game.IS_VERB("EXAMINE"):
        game.TELL("The lawn is well manicured.")

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

def HOUSE_F(game):
    """House action handler"""
    if game.IS_VERB("FIND"):
        game.TELL("It's right here. Some inspector you are.")
    
    elif game.IS_VERB("THROUGH"):
        if game.HERE == "FRONT-PATH" and game.IS_FSET("FRONT-DOOR", "OPENBIT"):
            game.GOTO("FOYER")
        elif game.HERE == "EAST-OF-DOOR" and game.IS_FSET("BAY-WINDOW", "OPENBIT"):
            game.GOTO("LIVING-ROOM")
        else:
            game.TELL("You might try the front door.")
    
    elif game.IS_VERB("EXAMINE"):
        game.TELL(
            "The house is a magnificent New England colonial, like many other houses "
            "around the lake. It is painted slate gray with white trim."
        )

def GROUND_F(game):
    """Ground action handler"""
    if (game.IS_VERB("BRUSH") and 
        game.IS_IN("FRAGMENT", "PLAYER") and 
        not game.GETG("FRAGMENT-CLEANED")):
        game.PERFORM("V?BRUSH", "FRAGMENT")
        return True
    
    elif game.IS_VERB("EXAMINE", "SEARCH", "SEARCH-AROUND"):
        if game.HERE == "ROURKE-ROOM":
            game.TELL("The floor is hardwood.")
        elif game.HERE == "FOYER":
            game.TELL("The floor is marble.")
        elif game.HERE == "IN-ROSES":
            if not game.IS_FSET("HOLE", "INVISIBLE"):
                game.PERFORM("V?SEARCH-AROUND", "HOLE")
                return True
            elif game.IS_VERB("SEARCH-GROUND-UNDER") and game.PRSI == "BALCONY":
                game.TELL(
                    "The balcony above is very large. Searching the entire area beneath it "
                    "would take a great deal of time."
                )
            else:
                game.TELL(
                    "There are rows upon rows of roses here. It would take you the best part of "
                    "a day to search the ground in great detail."
                )
        else:
            game.TELL("You don't find anything new there.")

def AIR_F(game):
    """Air action handler"""
    if game.IS_VERB("SMELL"):
        if game.HERE in ["ROSE-GARDEN", "IN-ROSES"]:
            game.TELL("The smell of roses permeates everything.")
        elif game.HERE in ["NORTH-LAWN", "EAST-LAWN", "WEST-LAWN"]:
            game.TELL("A breeze carries the faint smell of roses through the air.")
        elif game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C":
            game.TELL("The air is clear and fresh here.")
        elif FRESH_AIR(game, game.HERE):
            return True
        else:
            game.TELL("The air is rather musty here.")

def FRESH_AIR(game, RM):
    """Check for fresh air from open doors/windows"""
    P = 0
    while True:
        P = game.NEXTP(game.HERE, P)
        if P == 0:
            return False
        if P >= game.LOW_DIRECTION:
            TX = game.GETPT(game.HERE, P)
            L = game.PTSIZE(TX)
            if L == game.DEXIT:
                O = game.GETB(TX, game.DEXITOBJ)
                if game.IS_FSET(O, "OPENBIT"):
                    game.TELL("There is a pleasant breeze coming through the ")
                    game.TELL_D(O)
                    game.TELL(".")
                    return True
                

def LAKE_F(game):
    """Lake action handler"""
    if game.IS_VERB("SWIM", "LEAP", "THROUGH"):
        game.TELL(
            "You're not on vacation, but with ideas like that you will probably be given "
            "a rather long one."
        )
    
    elif game.IS_VERB("LOOK-INSIDE", "EXAMINE"):
        if game.HERE == "NORTH-LAWN" and game.IS_IN("SOGGY-WILL", "LAKE"):
            game.TELL(
                "A crumpled piece of paper is floating on the water a few feet from shore. "
                "With an uncommonly agile motion, you retrieve the drenched paper."
            )
            game.MOVE("SOGGY-WILL", game.WINNER)
        else:
            game.TELL("Surely you don't suspect the fish also?")

def SHED_F(game):
    """Shed action handler"""
    if game.IS_VERB("THROUGH"):
        if game.HERE in ["EAST-LAWN", "BEHIND-SHED"]:
            game.GOTO("SHED-ROOM")
            return True
        else:
            game.TELL("Senility strikes!")
    
    elif game.IS_VERB("LISTEN"):
        if game.GETG("SECRET-MEETING") != 0:
            game.TELL("You hear two muffled voices inside the shed.")
    
    elif game.IS_VERB("HIDE-BEHIND"):
        if game.HERE == "EAST-LAWN":
            game.TELL(
                "You carefully sneak behind the shed. It seems that no one saw you."
            )
        else:
            game.TELL(
                "You leave the shed and quietly slip behind it. Nobody appears to have seen "
                "you."
            )
        game.GOTO("BEHIND-SHED")
        return True
    


##############################################################################################################################
##  People Functions
##############################################################################################################################

def PLAYER_F(game):
    """Player action handler"""
    pass  # Empty function







def SHOW_HOLE(game):
    """Show hole location routine"""
    game.TELL(
        "McNabb grabs your arm and leads you to a spot deep within the garden and "
        "near the house. You might never have found this place alone. He points at "
        "the ground, where you see two holes in the soft earth."
    )
    game.FCLEAR("HOLE", "INVISIBLE")
    game.SETG("HOLE-SHOWN", True)

def HOLE_F(game):
    """Hole action handler"""
    if not game.GETG("HOLE-TELL"):
        game.TELL("What hole?")
    elif game.IS_VERB("ASK-ABOUT"):
        return False
    elif game.IS_VERB("FIND"):
        if game.HERE != "IN-ROSES":
            game.TELL("They're among the roses, or have you forgotten?")
        elif not game.IS_FSET("HOLE", "INVISIBLE"):
            game.TELL("They're right here!")
        elif not game.GETG("HOLE-SHOWN") and game.PROB(80):
            game.TELL(
                "The rose garden is vast and full of thorny roses. You might look "
                "for the rest of the day before you find them."
            )
        else:
            game.TELL(
                "The garden is rather big, even just the area you are searching now, and the "
                "holes were small. They're not here, but are probably nearby."
            )
    elif game.HOLE in [game.PRSI, game.PRSO]:
        if game.IS_VERB("EXAMINE", "LOOK-INSIDE"):
            game.TELL(
                "There are two holes here, each about two inches by four inches. They are at "
                "least three inches deep and the soil is compacted around them."
            )
        elif ((game.IS_VERB("SEARCH-GROUND-AROUND") and game.PRSO == "GROUND") or 
              game.IS_VERB("SEARCH-AROUND")):
            if game.LOC("GARDENER") == game.HERE:
                game.TELL("Mr. McNabb watches you with ill-concealed irritation.")
            
            if game.GETG("FRAGMENT-FOUND"):
                game.TELL(
                    "Aside from dirt, organic fertilizer, and small crawly creatures, you turn "
                    "up nothing but roses."
                )
            else:
                RST = game.GETG("RST") + 1
                game.SETG("RST", RST)
                if RST > 2 or game.PROB(30):
                    game.TELL(
                        "Ouch! You cut your finger on a sharp edge as you dig. You search carefully "
                        "in the dirt, now that you are sure something is there, and pull up a piece "
                        "of porcelain, covered with dirt and dried mud."
                    )
                    game.THIS_IS_IT("FRAGMENT")
                    game.MOVE("FRAGMENT", game.WINNER)
                    game.FCLEAR("FRAGMENT", "INVISIBLE")
                    game.SETG("FRAGMENT-FOUND", True)
                    game.SETG("FRAGMENT-FELT", True)
                else:
                    game.TELL(game.GETG("ROSE-DIGS")[RST - 1]) ## XXX This is a bit of a problem - use different APi?
    else:
        game.TELL("There is no hole here.")

def FRAGMENT_F(game):
    """Fragment action handler"""
    if game.IS_VERB("EXAMINE"):
        if game.GETG("FRAGMENT-CLEANED"):
            game.TELL("The fragment is beautifully hand-painted")
            game.SETG("FRAGMENT-FLAG", True)
            if game.GETG("CHINA-EXAMINED"):
                game.TELL(", exactly like those you saw in the kitchen")
            game.TELL(".")
        else:
            game.TELL(
                "The piece of porcelain is filthy, coated with dried mud. You can barely "
                "make out some design underneath the dirt."
            )
    
    elif game.IS_VERB("FINGERPRINT"):
        game.TELL(
            "It's covered with dirt and mud. You realize that there would be no good "
            "fingerprints on it."
        )
    
    elif game.IS_VERB("ANALYZE"):
        game.DO_ANALYZE()
    
    elif game.IS_VERB("BRUSH"):
        game.SETG("FRAGMENT-CLEANED", True)
        game.TELL(
            "As you wipe off the piece of porcelain, you notice that it is a fragment of "
            "some very beautiful piece, handsomely painted."
        )
        if game.GETG("CHINA-EXAMINED"):
            game.TELL("  The markings are identical to those you saw on the china in the kitchen.")
        game.CRLF()


def GARDENER_F(game, RARG=None):
    """Gardener action handler"""
    if RARG == "M-OBJDESC":
        if game.IN_MOTION("GARDENER"):
            return True
        elif game.LOC("GARDENER") == "ORCHARD":
            game.TELL("Mr. McNabb is here, pruning the trees.")
        elif game.LOC("GARDENER") in ["NORTH-LAWN", "EAST-LAWN", "SOUTH-LAWN", "WEST-LAWN"]:
            game.TELL("Mr. McNabb is here, ")
            game.TELL(game.PICK_ONE("LAWN-ACTIVITIES"))
            game.TELL(".")
        elif game.IS_IN("GARDENER", "ROSE-GARDEN"):
            game.TELL("Mr. McNabb is here, ")
            game.TELL(game.PICK_ONE("GARDEN-ACTIVITIES"))
            game.TELL(".")
        else:
            game.TELL("Mr. McNabb is here.")
        
        if game.GETG("G-I-G"):
            game.TELL(" He seems quite worked up and is talking aloud to himself.")
        elif game.GETG("GARDENER-ANGRY"):
            game.TELL(" He seems pretty angry about something.")
        
        game.CRLF()
        game.CARRY_CHECK("GARDENER")
    
    elif game.IS_VERB("HELLO", "GOODBYE"):
        if game.GETG("GARDENER-ANGRY"):
            game.TELL("McNabb grunts briefly in your direction.")
        elif game.GETG("G-I-G"):
            game.TELL("He answers absently and starts to mumble quietly about the roses.")
        else:
            game.TELL("He replies with a brief nod, and then starts mumbling to himself about the ")
            game.TELL(game.PICK_ONE("GARDEN-MUMBLES"))
            game.TELL(".")
    
    elif game.WINNER == "GARDENER":
        if game.IS_VERB("SHOW", "SSHOW") and game.PRSI in ["GLOBAL-HOLE", "HOLE", "GLOBAL-ROSES", "ROSE"]:
            if not game.GETG("HOLE-TELL") and not game.GETG("G-I-G"):
                game.TELL("\"I don't know what you're-a talkin' aboot.\"")
            elif game.GETG("NO-SHOW"):
                game.TELL(
                    "\"I don't think I remember where it was. Now go away,\" he says. He looks a "
                    "bit annoyed at you, probably for asking him before and then running off."
                )
            elif game.GETG("HOLE-SHOWN"):
                game.TELL("\"I've already shown you plenty. Now, git!\"")
            elif game.HERE == "IN-ROSES":
                game.SETG("GARDENER-SHOW", True)
                game.SETG("HOLE-TELL", True)
                SHOW_HOLE(game)
            else:
                game.ESTABLISH_GOAL("GARDENER", "IN-ROSES", True)
                game.SETG("GARDENER-SHOW", True)
                game.SETG("HOLE-TELL", True)
                game.TELL("\"Follow me!\" he says, and starts walking toward the roses.")
        elif game.IS_VERB("FIND"):
            return False
        elif game.COM_CHECK("GARDENER"):
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
    
    elif game.IS_VERB("LISTEN"):
        if game.GETG("G-I-G"):
            game.TELL(
                "You can't make out everything, but he seems to be complaining about weeks "
                "of work on the roses ruined by someone stomping around in the garden. There "
                "are references to elephants and holes. When he's worked up, as now, he "
                "doesn't always make much sense."
            )
            game.SETG("HOLE-TELL", True)
        else:
            game.TELL("He seems to be mumbling about the ")
            game.TELL(game.PICK_ONE("GARDEN-MUMBLES"))
            game.TELL(".")
    
    elif game.IS_VERB("ASK-ABOUT") and game.PRSO == "GARDENER":
        if game.GETG("GARDENER-NO-REPLY") and not game.GETG("GARDENER-SHOW"):
            game.TELL(
                "\"I dinna give a hoot about you or your questions! Now, begone! Steppin' all "
                "o'er me roses. A crime, it is! I'll call the police is what!\" He seems pretty "
                "angry."
            )
        elif game.PRSI == "GLOBAL-HOLE" and game.GETG("HOLE-TELL"):
            game.TELL("\"I've already told you. There's holes in my garden!\"")
        elif game.PRSI == "GLOBAL-WEATHER" and not game.GETG("G-I-G"):
            game.TELL(
                "\"Beautiful! What a fine day. Except for the rain Wednesday night, I ha'ent "
                "had such a fine week in a long spell. Not that I'm complainin'. You see, with "
                "my roses...\" He goes on and on about his roses."
            )
        elif game.PRSI in ["GLOBAL-LADDER", "LADDER"]:
            game.TELL("\"What aboot it? I use it for cleanin' the gutters 'n prunin' the trees.\"")
        elif game.PRSI in ["GLOBAL-ROSES", "ROSE", "GLOBAL-WEATHER"]:
            if game.GETG("G-I-G"):
                game.TELL(
                    "He tells you his story. He was tending to the roses this morning when he "
                    "noticed two deep holes in the garden, with a few roses crushed nearby. He "
                    "doesn't know when he'll be able to repair the damage."
                )
                game.SETG("HOLE-TELL", True)
            else:
                game.TELL(
                    "McNabb goes on for some time about the exquisite nature of the garden in "
                    "general and mentions, for your benefit, some of the finer points of his "
                    "gardening technique."
                )
        elif game.PRSI == "LAWN":
            game.TELL(
                "McNabb tells a long tale of woe and hardship, of days and nights "
                "sweating with the lawn mower, roller, and weed puller."
            )
        elif game.PRSI in ["GEORGE", "GLOBAL-GEORGE", "BAXTER", "GLOBAL-BAXTER", 
                           "DUNBAR", "GLOBAL-DUNBAR", "MRS-ROBNER", "GLOBAL-MRS-ROBNER", 
                           "ROURKE", "GLOBAL-ROURKE"]:
            game.TELL(
                "\"I don't care much aboot any of them from in the house. I barely even know "
                "which is which.\" He shakes his head and continues with his work."
            )
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "\"Too bad aboot Mr. Robner. He was a good man, liked to talk aboot the "
                "garden. He told me 'McNabb', he says, 'this here's the finest garden I've "
                "seen.' We'd talk for hours about planting and gardening. None of the others "
                "knows between a rose and a sunflower.\" He shakes his head sadly and "
                "continues his work."
            )
        else:
            game.TELL("\"I dinna know nothin' aboot that.\"")


def BAXTER_F(game, RARG=None):
    """Baxter action handler"""
    if RARG == "M-OBJDESC":
        if game.IN_MOTION("BAXTER"):
            return True
        elif game.IS_IN("BAXTER", "SHED") and game.GETG("SECRET-MEETING") != 0:
            game.TELL(
                "Mr. Baxter and Ms. Dunbar are here talking rapidly with each other. They "
                "haven't noticed you yet."
            )
        elif game.GETG("DUNBAR-BAXTER-MEET"):
            game.SETG("DUNBAR-BAXTER-MEET", False)
            game.TELL(
                "Mr. Baxter is in one corner, talking to Ms. Dunbar. He notices you and "
                "motions Dunbar to stop talking."
            )
        elif game.IS_IN("BAXTER", "LIVING-ROOM"):
            if game.GETG("POST-WILL"):
                game.TELL("Mr. Baxter is offering his sympathies to Mrs. Robner.")
            elif game.IS_IN("RECURSIVE-BOOK", "BAXTER"):
                game.FSET("RECURSIVE-BOOK", "NDESCBIT")
                game.TELL("Mr. Baxter is sitting here reading a book.")
            else:
                game.TELL("Mr. Baxter is sitting quietly here.")
        else:
            game.TELL("Mr. Baxter is here.")
        game.CRLF()
        game.CARRY_CHECK("BAXTER")
    
    elif game.IS_VERB("EXAMINE"):
        if game.GETG("SHOT-FIRED"):
            if game.IS_IN("BAXTER", "DUNBAR-ROOM"):
                game.TELL(
                    "Baxter seems out of breath. His hair is disheveled and his hands are "
                    "somewhat soiled."
                )
            else:
                game.TELL(
                    "Mr. Baxter has recovered his composure and looks calm. His hair is a bit "
                    "disheveled and his hands are dirty."
                )
    
    elif game.IS_VERB("HELLO"):
        game.TELL("Mr. Baxter returns your salutation.")
    
    elif game.IS_VERB("GOODBYE"):
        game.TELL("Mr. Baxter nods.")
    
    elif game.WINNER == "BAXTER":
        if game.IS_VERB("FIND"):
            return False
        elif game.COM_CHECK("BAXTER"):
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
    
    elif game.IS_VERB("SEARCH", "SEARCH-OBJECT-FOR"):
        game.TELL(
            "Mr. Baxter pushes you away abruptly. \"I don't know what game you're playing, "
            "Inspector, and frankly I'm not interested. You have been invited here to "
            "investigate, not molest innocent persons.\""
        )
    
    elif game.IS_VERB("ACCUSE") and game.PRSI == "GLOBAL-MURDER":
        if game.GETG("PEN-SEEN"):
            game.TELL(
                "Mr. Baxter turns to run away, but notices Sergeant Duffy by the door. He "
                "stops abruptly and faces you."
            )
    
    elif game.IS_VERB("ARREST"):
        if game.GETG("PEN-SEEN") or game.GETG("BAXTER-SEEN"):
            if game.IS_IN("BAXTER", game.HERE):
                game.TELL(
                    "Sergeant Duffy enters the room solemnly. He places a pair of handcuffs "
                    "on Mr. Baxter, who is stiff and unspeaking.  \"Let's not have any "
                    "trouble, now.\" Duffy remarks to Baxter."
                )
            else:
                game.TELL(
                    "A few moments pass and Sergeant Duffy appears, escorting a handcuffed "
                    "Mr. Baxter."
                )
            game.TELL(" With that, he leads him from your view and into a police car waiting near the south lawn.\n\n")
            game.END_HEADER("August 10")
            game.TELL("Congratulations on your work in the Robner case. As I'm sure you are aware, Mr. Baxter was found guilty ")
            if game.IS_FSET("BAXTER-PAPERS", "TOUCHBIT") and game.GETG("NOTE-READ"):
                game.TELL(
                    "of two counts of first-degree murder and has been sentenced to two "
                    "consecutive terms of life imprisonment.  My only regret is that Dunbar "
                    "couldn't stand trial with him. We may never know the complete story behind "
                    "the Robner murder. But once again, thanks.\n\n"
                )
            else:
                game.TELL(
                    "of first-degree murder in the death of Ms. Dunbar. Unfortunately, Baxter "
                    "remained tight-lipped throughout the proceedings, and except for the "
                    "revelation that Baxter and Dunbar were lovers, there was no motive established "
                    "for her murder. The jury acquitted Mr. Baxter in the murder of Mr. Robner, "
                    "as a motive had not been established. I am indeed sorry that a proper "
                    "conclusion to the case could not have been made.\n\n"
                )
            game.CASE_OVER()
        elif game.IS_IN("CORPSE", "DUNBAR-ROOM"):
            game.TELL("Trusty Sergeant Duffy enters and places Mr. Baxter under arrest. They leave, Baxter remaining calm.\n\n")
            game.END_HEADER("August 13")
            game.TELL("I heard today that the jury in the Robner case has voted to acquit Mr. Baxter of both murders at the Robner house.")
            if game.IS_FSET("BAXTER-PAPERS", "TOUCHBIT"):
                game.TELL(
                    "While it was clear that Baxter had committed numerous crimes in the Focus "
                    "case, the jury was unconvinced of the relation between that and the murders. "
                    "They felt that Ms. Dunbar had committed the first murder, although I can't "
                    "imagine any scenario in which that would be possible, and had committed "
                    "suicide in desperation. These explanations leave much to be desired, but "
                    "what's done is done. I can't help feeling that there is more to this case than "
                    "has been discovered. Thank you for your work.\n\n"
                )
                game.CASE_OVER()
            else:
                game.TELL(
                    "The jury believed the more probable story: that Ms. Dunbar committed the "
                    "first murder and then committed suicide when her guilt became clear to you. "
                    "I don't really believe this any more than you do, but the evidence is vague, "
                    "you must agree. Thanks again for handling the case.\n\n"
                )
                game.CASE_OVER()
        elif game.IS_FSET("BAXTER-PAPERS", "TOUCHBIT"):
            if game.IS_FSET("LAB-REPORT", "TOUCHBIT"):
                game.TELL("Trusty Sergeant Duffy enters and places Mr. Baxter under arrest. They leave, Baxter remaining calm.\n\n")
                game.END_HEADER("August 11")
                game.TELL(
                    "I am sorry to report that Mr. Baxter was acquitted yesterday of the murder "
                    "of Mr. Robner. In speaking to the District Attorney, I gathered that the jury "
                    "was almost convinced of Baxter's guilt, given that he had both motive and a "
                    "means to enter the house using the ladder. However, the theory had a number of "
                    "serious flaws, including the means by which Baxter could have administered the "
                    "drug either without Robner's knowledge or without a struggle. I must confess "
                    "that I too am baffled. I am convinced that Baxter is guilty, but I fear we "
                    "will never know for certain.\n\n"
                )
                game.CASE_OVER()
            else:
                game.MURDER_NOT_PROVEN("BAXTER", True)
        elif game.IS_FSET("LAB-REPORT", "TOUCHBIT"):
            game.TELL("Duffy enters and places Mr. Baxter under arrest, then leads him away without fuss.\n\n")
            game.END_HEADER("August 11")
            game.TELL(
                "I am indeed sorry that Mr. Baxter was acquitted yesterday of the murder of "
                "Mr. Robner. From the District Attorney, I gather that the jury was completely "
                "unconvinced by the our case. They found neither sufficient motive nor any "
                "plausible means of introducing the fatal medicine into Mr. Robner's drink. I "
                "must confess to being baffled by this case. Perhaps we shall never know the "
                "true story of Mr. Robner's murder.\n\n"
            )
            game.CASE_OVER()
        else:
            game.MURDER_NOT_PROVEN("BAXTER", False)
    
    elif game.IS_VERB("ASK-FOR") and game.IS_IN("CORPSE", "DUNBAR-ROOM") and game.PRSI == "GLOBAL-PEN":
        game.TELL(
            "Baxter reaches instinctively into his jacket and starts to pull out a pen. "
            "He hesitates suddenly, pen in hand."
        )
        game.MOVE("PEN", "BAXTER")
        game.SETG("PEN-SEEN", True)
    
    elif game.IS_VERB("ASK-ABOUT") and game.PRSO == "BAXTER":
        if not game.GRAB_ATTENTION("BAXTER"):
            return True
        
        if game.PRSI == "RECURSIVE-BOOK":
            game.TELL(
                "\"A fascinating story, Inspector. A man is found dead behind a locked door, "
                "a clear suicide. Yet the detective seems bent on proving that a murder has "
                "occured. Rather odd, wouldn't you say?\""
            )
        elif game.PRSI == "GLOBAL-CONCERT":
            game.TELL(
                "\"A marvelous concert! There were works by Beethoven, Sibelius, and Ravel. I "
                "never would've guessed you were interested in serious music, Inspector.\""
            )
        elif game.PRSI == "STUB":
            # STUB conversation logic - handles alibi contradiction tracking
            # STUB-DX: Dunbar has already explained the stub
            # STUB-B: Baxter has given his version 
            # STUB-BX: Baxter gave version while Dunbar present
            # STUB-D: Dunbar has given her version
            # CONTRADICTION: Set when stories don't match
            if game.GETG("STUB-DX"):
                game.TELL("\"My dear Inspector, it is just as Ms. Dunbar told you.\"")
            else:
                game.SETG("STUB-B", True)  # Mark that Baxter has told his version
                if game.IS_IN("DUNBAR", game.HERE):
                    game.SETG("STUB-BX", True)  # Baxter told it with Dunbar present
                if game.GETG("STUB-D"):
                    game.SETG("CONTRADICTION", True)  # Stories contradict
                game.TELL(
                    "\"Ah, that must be Ms. Dunbar's ticket stub. I should have told you earlier. "
                    "Ms. Dunbar was with me at the concert on the night that Marshall killed "
                    "himself. She became ill at intermission and hired a car to take her back home. "
                    "You see, Inspector, I know that Ms. Dunbar appreciates classical music, so I "
                    "occasionally ask her along to my subscription series. I really should "
                    "have told the other detective, but I didn't think it mattered.\""
                )
        elif game.PRSI == "GLOBAL-LADDER":
            game.TELL("\"What ladder? You know, Inspector, your questions are becoming quite tiresome.\"")
        elif game.PRSI in ["GLOBAL-MERGER", "GLOBAL-OMNIDYNE"]:
            game.TELL(
                "\"I didn't realize you had an interest in finance. Before Marshall died, we "
                "agreed that the only reasonable way to protect our interests was to be bought "
                "out by a larger company which could then provide us with capital for "
                "expansion. I had been talking to people at Omnidyne and we agreed in "
                "principle on the terms for such an agreement last week. I'm hopeful that we "
                "can close the deal quickly.\""
            )
        elif game.PRSI == "GLOBAL-NEW-WILL":
            if game.GETG("WILL-TIME") > 0:
                game.TELL(
                    "\"It's fortunate for George that Marshall died when he did. It must be quite "
                    "a relief to know that he'll have plenty of money.\" He chuckles softly."
                )
                if game.GETG("AT-READING"):
                    game.TELL(" \"I guess that explains his reaction at the reading.\"")
                game.CRLF()
            else:
                game.TELL(
                    "\"I don't know much about the family's affairs. Marshall threatened "
                    "to make a new will, but it certainly appears that he never did.\""
                )
        elif game.PRSI == "GLOBAL-FOCUS":
            if game.GETG("B-FOCUS"):
                game.TELL(
                    "\"I told you already. There was no legal wrongdoing, only "
                    "some reporters trying to stir up a fuss.\" He appears quite nervous."
                )
            elif game.GETG("B-NOTE"):
                game.TELL("\"I understand the note no more than you do.\" He turns away.")
            else:
                game.TELL(
                    "There is a flicker of surprise on Baxter's face. \"I'm not sure "
                    "what you mean. Focus Corporation has been a subsidiary of Robner "
                    "Corp. for some years. I fail to see its import.\""
                )
        elif game.PRSI in ["GEORGE", "GLOBAL-GEORGE"]:
            game.DISCRETION("BAXTER", "GEORGE")
            game.TELL(
                "\"I've known the boy for some time, and believe me, he's no good. He's "
                "wasted more money this year than you've probably earned. His father "
                "reprimanded him frequently, as you know. George even threatened his father "
                "from time to time.\""
            )
        elif game.PRSI in ["CORPSE", "DUNBAR", "GLOBAL-DUNBAR"]:
            game.TELL(
                "\"Ms. Dunbar is an efficient and tireless worker. She has been of tremendous "
                "help to Marshall and has been working quite hard for him lately. She had a "
                "great deal of respect for him, that's clear. She has a keen mind and is an "
                "exceptional strategic planner for the corporation.\""
            )
        elif game.PRSI in ["MRS-ROBNER", "GLOBAL-MRS-ROBNER"]:
            game.TELL(
                "\"Leslie is a fine woman from a distinguished family. She was much more "
                "outgoing than Marshall, but she seems to have become accustomed to the quiet "
                "life here. I am quite grieved for her.\""
            )
        elif game.PRSI in ["ROURKE", "GLOBAL-ROURKE", "GARDENER", "GLOBAL-GARDENER"]:
            game.TELL("\"I don't know much about ")
            game.TELL_D(game.PRSI)
            game.TELL(".\"")
        elif game.PRSI == "GLOBAL-OLD-WILL":
            game.TELL("\"I really don't know anything about the old will.\"")
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "\"Marshall was a truly great man...a brilliant manager; he started the "
                "corporation single-handedly about 25 years ago and is mostly responsible for "
                "its reputation. I owe him a great deal. He was also a great philanthropist "
                "and got the corporation involved in many charitable works. I am not given to "
                "shows of emotion, Inspector, but I will miss him greatly.\""
            )
        else:
            game.TELL("\"I can't help you there.\"")
    
    elif game.IS_VERB("CONFRONT", "SHOW"):
        if not game.GRAB_ATTENTION("BAXTER"):
            return True
        
        if game.PRSI == "LAB-REPORT":
            game.TELL(
                "Baxter studies the report carefully. \"This is quite peculiar. It appears "
                "that Marshall was murdered. I wonder...I would have a word with George if I "
                "were you, Inspector.\""
            )
        elif game.PRSI == "STUB":
            game.PERFORM("V?ASK-ABOUT", "BAXTER", "STUB")
            return True
        elif game.PRSI == "NOTE-PAPER" and game.GETG("NOTE-READ") and not game.GETG("B-NOTE"):
            game.SETG("B-NOTE", True)
            game.TELL(
                "He reads it carefully against the light, then speaks: \"I really don't know "
                "what to make of this. Marshall seems to be insisting that I do something. I'm "
                "afraid we will never know, since I never got the note.\""
            )
        elif game.PRSI == "BAXTER-PAPERS" and not game.GETG("B-FOCUS"):
            game.SETG("B-FOCUS", True)
            game.TELL(
                "He reads slowly and leafs through the pages. \"I'm afraid I haven't been "
                "entirely candid with you. There was some trouble a few years ago with Focus "
                "Corp. because of some, let us say, irresponsible dealings on my part. Marshall "
                "agreed to cover up my involvement to save the company any bad publicity.\""
            )
            if game.GETG("B-NOTE"):
                game.TELL(
                    "\"I can't understand why he would be insisting that I do this or that, "
                    "though, as it says on that note you showed me. He must have changed his "
                    "mind, since I never received the note.\""
                )
            return True
        elif game.PRSI == "LETTER":
            game.TELL(
                "\"Very interesting, Inspector, but I assure you that this fellow is quite "
                "off base about the business. Marshall and I were in complete agreement when "
                "it came to those matters. I can't imagine where he got that idea.\""
            )
        else:
            game.TELL("\"I can't understand why you are showing this to me. Have you nothing better to do than ")
            game.TELL(game.PICK_ONE("BAXTER-ANNOYED"))
            game.TELL("?\"")


def MURDER_NOT_PROVEN(game, PERSON, ARG=True):
    """Murder not proven ending routine"""
    game.TELL("Sergeant Duffy dutifully appears and escorts ")
    game.TELL_D(PERSON)
    game.TELL(" from the grounds.\n\n")
    game.END_HEADER("July 26")
    game.TELL(
        "I am sorry to inform you that the District Attorney's office has declined "
        "to seek an indictment against "
    )
    game.TELL_D(PERSON)
    game.TELL(
        " in the case of the death of Mr. Robner, against your recommendation. It is still not clear that Mr. Robner "
        "was murdered, although, as you point out, there are a number of suspicious "
        "characters in the Robner household."
    )
    if not ARG:
        game.TELL(
            "  Additionally, Mr. Baxter seems to have "
            "had no clear motive for killing Mr. Robner."
        )
    game.CRLF()
    if PERSON == "BAXTER":
        game.TELL(
            "Mr. Baxter has threatened to sue the department for malicious "
            "arrest, but we feel that he will prefer to avoid the publicity."
        )
    game.TELL("     Please be more careful in the future!\n\n")
    game.CASE_OVER()



def GLOBAL_PERSON(game):
    """Global person handler for references to people not present"""
    if ((game.IS_VERB("ASK-ABOUT") and 
         game.IS_FSET(game.PRSO, "PERSON") and 
         not game.IS_IN(game.PRSO, "GLOBAL-OBJECTS")) or
        game.IS_VERB("WHAT", "FIND", "WAIT-FOR", "FOLLOW", "CALL", "CALL-LOSE")):
        return False
    
    elif game.IS_VERB("TELL"):
        game.TELL("It's not clear to whom you are referring.")
        game.SETG("P-CONT", False)
        return True
    
    else:
        if game.IS_FSET(game.PRSO, "PERSON"):
            game.TELL_D(game.PRSO)
        else:
            game.TELL_D(game.PRSI)
        
        if (game.IS_VERB("ASK-ABOUT", "TELL") and
            game.BAND(
                game.GETP(
                    game.LOC(
                        game.GET(
                            "CHARACTER-TABLE",
                            game.GETP(game.PRSO, "P?CHARACTER")
                        )
                    ),
                    "P?CORRIDOR"
                ),
                game.GETP(game.HERE, "P?CORRIDOR")
            ) != 0):
            game.TELL(" can't hear you.")
        elif (game.PRSO == "GLOBAL-MRS-ROBNER" and
              game.HERE == "MASTER-BATH" and
              game.IS_IN("MRS-ROBNER", "MASTER-BEDROOM")):
            game.TELL(" can't hear you.")
        else:
            game.TELL(" isn't here!")
        
        game.SETG("P-CONT", False)
        return True
    

def GEORGE_F(game, RARG=None):
    """George action handler"""
    if RARG == "M-OBJDESC":
        if game.IN_MOTION("GEORGE"):
            return True
        elif game.IS_IN("GEORGE", "KITCHEN"):
            game.TELL("George is here, preparing a snack.")
        elif game.IS_IN("GEORGE", "DINING-ROOM"):
            game.TELL("George is sitting at the table, eating some red herrings.")
        elif game.IS_IN("GEORGE", "LIVING-ROOM"):
            if game.GETG("POST-WILL"):
                game.TELL("George is staring contentedly out the bay window.")
            else:
                game.TELL("George is here, pacing around the room.")
        elif game.IS_IN("GEORGE", "NORTH-LAWN"):
            game.TELL("George is here, staring out over the lake.")
        elif game.IS_IN("GEORGE", "GEORGE-ROOM") and not game.GETG("GEORGE-WAIT"):
            if game.GETG("TUNE-ON"):
                game.TELL("George is lying on his bed, listening intently to a " + game.GETG("TUNE-ON") + ".")
            else:
                game.TELL("George is sitting on his bed, deep in thought.")
        else:
            game.TELL("George is here.")
        game.CRLF()
        game.CARRY_CHECK("GEORGE")
    
    elif game.IS_VERB("HELLO", "GOODBYE"):
        game.TELL("George looks up and grunts disinterestedly.")
    
    elif game.WINNER == "GEORGE":
        if game.IS_VERB("FIND"):
            return False
        elif game.COM_CHECK("GEORGE"):
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
    
    elif game.IS_VERB("CALL") and game.GETG("GEORGE-RUN") > 0:
        game.TELL("\"Don't bother me!\" he shouts, and continues on.")
    
    elif game.IS_VERB("SEARCH", "SEARCH-OBJECT-FOR"):
        if game.GET(game.GET("GOAL-TABLES", "GEORGE-C"), "GOAL-S") == "NORTH-LAWN":
            game.TELL(
                "George points accusingly at you. \"Don't come near me! I'm getting sick and "
                "tired of your accusing tone. Get lost!\""
            )
        else:
            game.TELL("\"Buzz off! Don't come back until you get a search warrant!\" He chuckles in contempt.")
    
    elif game.IS_VERB("ACCUSE"):
        game.TELL("George sneers at you. \"What an ass! Go on, try to prove it!\"")
    
    elif game.IS_VERB("ARREST"):
        if game.GETG("NEW-WILL-SEEN") or game.GETG("GEORGE-RUN"):
            game.TELL(
                "Faithful Sergeant Duffy enters and handcuffs George, who spits at you. \"You "
                "filthy, stinking...\" is all you hear as George is carted off struggling.\n\n"
            )
            game.END_HEADER("August 4")
            game.TELL(
                "I am sorry to inform you that George Robner was acquitted in the death of "
                "his father today. It seems the evidence, consisting mainly of a new will "
                "which George admitted under pressure that he was trying to destroy, was "
                "insufficient for the jury to return a guilty verdict. Although I suspect that "
                "George may have committed the crime, his arrest was a bit premature.\n\n"
            )
            game.CASE_OVER()
        else:
            return False
    
    elif game.IS_VERB("CONFRONT", "SHOW"):
        if not game.GRAB_ATTENTION("GEORGE"):
            return True
        
        if game.PRSI == "LAB-REPORT":
            game.TELL(
                "George scans the report. \"Killed, eh? I wonder who might have wanted...\" He "
                "cocks his head in thought. \"I'm sorry, Inspector, I really should act a bit "
                "better with you. I thought you were just snooping about, digging up dirt about "
                "the family. I'm not sure...I can't believe Mom would have anything to do with "
                "it, although...Baxter, now there's a worm for you. He'd do anything, maybe "
                "even murder, to get ahead. I just don't know.\""
            )
        elif game.PRSI == "LETTER":
            game.TELL(
                "George reads the letter quickly. \"Pompous ass! What does he know about "
                "it?\" He pauses. \"I thought Mom was having an affair. How nice for the "
                "lovebirds that Dad is dead! They can finish their honeymoon plans without "
                "worrying. It's perfect!\" With a bitter laugh, he throws the letter to the "
                "ground."
            )
            game.SETG("G-LETTER", True)
            game.MOVE("LETTER", game.HERE)
        elif game.PRSI == "DESK-CALENDAR" and game.GETG("CALENDAR-PAGE") == 8 and not game.GETG("GEORGE-SEQUENCE"):
            game.SETG("G-CALENDAR", True)
            if game.GETG("WILL-TIME") > 0:
                game.TELL(
                    "\"I...uh...I don't really know what to say. I guess that Dad...but there is "
                    "no other...I can't help you...sorry.\" George seems to be quite agitated."
                )
                game.GEORGE_HACK()
            else:
                game.TELL(
                    "George tilts his head in thought (or perhaps surprise) but recovers quickly. "
                    "\"All I know is that Coates is my father's personal attorney.\""
                )
        elif game.PRSI == "NEWSPAPER" and game.GETG("NEWSPAPER-READ"):
            game.DISCRETION("GEORGE", "BAXTER")
            game.TELL(
                "\"So Baxter's arranged the merger. I'll be damned. That's strange, since "
                "Dad was opposed to the whole thing. He's worried about losing control of "
                "the company ever since he had to sell off most of his interest. I bet he "
                "doesn't even own enough shares to prevent the deal.\" "
                "He shakes his head in disbelief."
            )
    
    elif game.IS_VERB("ASK-ABOUT") and game.PRSO == "GEORGE":
        if not game.GRAB_ATTENTION("GEORGE"):
            return True
        
        if game.PRSI == "GLOBAL-HIDDEN-CLOSET":
            if game.GETG("SAFE-SEEN") or game.GETG("NEW-WILL-SEEN"):
                game.TELL(
                    "\"What of it? Dad's safe is there. I don't think anyone knows about it "
                    "except Dad and me.\""
                )
            else:
                game.TELL(
                    "\"Hidden closet, you say? Hmm. I think I'd know if there was one, but there "
                    "isn't!\""
                )
        elif game.PRSI == "GLOBAL-MERGER":
            game.TELL(
                "\"I've heard talk of a merger between Dad's company and another one, "
                "but I don't think it's happened yet. Dad would be furious if it did, "
                "though. I can tell you that!\""
            )
        elif game.PRSI == "GLOBAL-STEVEN":
            if game.GETG("G-LETTER"):
                game.TELL(
                    "\"He's a little worm who's been coming by lately. He's one of those fancy "
                    "ski-instructor types, if you know what I mean. From what I've seen, it "
                    "wouldn't surprise me if he and Mom are having an affair.\""
                )
            else:
                game.DISCRETION("GEORGE", "MRS-ROBNER")
                game.TELL(
                    "\"Steven? Oh, you must mean the guy who comes around for Mom now and "
                    "then. I don't know much about him. Dresses a bit above himself, I'll say "
                    "that much.\""
                )
        elif game.PRSI in ["BAXTER", "GLOBAL-BAXTER"]:
            game.TELL(
                "\"I don't know much about him, really. With Baxter, it's always business, "
                "and he's not here much except to discuss business with Dad. You might ask Ms. "
                "Dunbar about him, though. She handled lots of Dad's business matters herself, "
                "so they work together a lot. They probably know each other pretty well.\""
            )
        elif game.PRSI in ["CORPSE", "DUNBAR", "GLOBAL-DUNBAR"]:
            game.TELL(
                "\"She's been here for about ten years, I guess. She knows a lot about Dad's "
                "business, and he lets her take care of a lot of stuff by herself. Other than "
                "that, I can't say. We don't get in each other's way. I think she's heard Dad "
                "lecture me too often.\""
            )
        elif game.PRSI in ["MRS-ROBNER", "GLOBAL-MRS-ROBNER"]:
            game.TELL(
                "\"She's OK. Not as stuck up as Dad about money. We've always gotten "
                "along pretty well. I think she understands me better than Dad ever "
                "did.\""
            )
        elif game.PRSI == "GLOBAL-SAFE":
            if game.GETG("NEW-WILL-SEEN"):
                game.TELL(
                    "\"Let's not go into it, ok? You caught me looking for the will. Well, what of "
                    "it? I didn't kill Dad, if that's what you're thinking. Leave me alone!\""
                )
            elif game.GETG("SAFE-SEEN"):
                game.TELL(
                    "\"You mean my father's safe? Yeah, if he brings important papers home he puts "
                    "them in there. He keeps most important stuff at the office at the bank. You "
                    "really startled me in there. I thought I might be able to get it open. Dad "
                    "always acted like it was a big secret, something out of a spy story. Anyway, "
                    "it turns out I don't remember the combination. It was a long time ago.\""
                )
            elif game.GETG("GEORGE-SEQUENCE"):
                game.TELL(
                    "George turns toward you with rage in his eyes. \"I don't know anything about "
                    "any damn safe! Now leave me alone or I'll have you kicked out of here!\" He "
                    "turns away."
                )
            else:
                game.TELL(
                    "George looks briefly toward the ceiling, as if recalling something. \"Oh, I'm "
                    "sorry. A safe? No, I don't know about any safe...except at the office, that "
                    "is. I think there's one there.\""
                )
        elif game.PRSI in ["GARDENER", "GLOBAL-GARDENER"]:
            game.TELL(
                "\"McNabb, that old bore? Always talking about the damn roses and weeds. Don't "
                "ask him about them, unless you have all day.\""
            )
        elif game.PRSI in ["ROURKE", "GLOBAL-ROURKE"]:
            game.DISCRETION("GEORGE", "ROURKE")
            game.TELL(
                "\"She's nice but awfully nosy. She acts like she knows everything that goes "
                "on around here, but she doesn't know the half of it.\""
            )
        elif game.PRSI == "GLOBAL-OLD-WILL":
            game.TELL("\"I know what you know.\"")
        elif game.PRSI in ["NEW-WILL", "GLOBAL-NEW-WILL"]:
            if game.GETG("PRESENT-TIME") > game.GETG("WILL-TIME"):
                if game.IS_FSET("NEW-WILL", "TOUCHBIT"):
                    game.TELL("\"You should know what it says.\"")
                elif game.GETG("NEW-WILL-SEEN"):
                    game.TELL(
                        "\"I don't know what you're talking about. There's no new will. Dad never "
                        "wrote one! He would just threaten me when I asked for spending money.\""
                    )
                elif game.GETG("GEORGE-SEQUENCE"):
                    game.TELL(
                        "\"Look. I know the same as you. There's no new will. I'm sure of it. Dad "
                        "would have rubbed my nose in it: you can be sure of that!\""
                    )
                elif game.GETG("AT-READING"):
                    game.TELL("\"You were there when I was. Coates says there's no new will.\"")
                elif game.GETG("WILL-TIME") == 0:
                    game.TELL(
                        "\"Dad always threatened to write a new will, but I guess he ran out "
                        "of time.\" He chuckles disturbingly."
                    )
                else:
                    game.TELL(
                        "\"Oh, yeah. You skipped out on the will reading. Anyhow, Coates says there's "
                        "no new will, and he should know, right?\""
                    )
            elif game.GETG("G-CALENDAR"):
                game.TELL(
                    "\"I know what you're getting at...the desk calendar. Look, I've heard nothing "
                    "about a new will. Maybe the old man just wanted to change something.\""
                )
            else:
                game.TELL("\"I don't know anything about any new will.\"")
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "\"Like I told your detective friend yesterday, we didn't get along too well. "
                "He was always riding me, giving me a hard time.\" George gets worked up "
                "talking about it.\"Look, man. I'm not going to lie and say I loved him, right? "
                "He got what...\" He stops in mid-sentence."
            )
        elif game.PRSI == "GLOBAL-FOCUS":
            game.TELL(
                "\"Focus...Focus...That name rings a bell. Something about the company, quite "
                "a while ago...what was it? I can't remember now. I don't pay much attention to "
                "business stuff: I've got better things to do.\""
            )
        else:
            game.TELL("\"I haven't a clue.\"")



##############################################################################################################################
##  Object functions
##############################################################################################################################




def DESK_CALENDAR_F(game, RARG=None):
    """Desk calendar action handler"""
    if game.IS_VERB("READ", "EXAMINE") and game.PRSI == "INTNUM":
        if game.P_NUMBER == 0 or game.P_NUMBER > 30:
            game.TELL("Why?  Is it your birthday?")
        else:
            game.TELL("You flip the pages until you find the page.")
            game.SETG("CALENDAR-PAGE", game.P_NUMBER)
    
    if game.IS_VERB("CLOSE"):
        game.TELL("It's not worth the effort.")
    elif game.IS_VERB("TURN") and not game.PRSI:
        if game.GETG("CALENDAR-PAGE") == 31:
            game.TELL("You have reached the end of the book.")
            return True
        else:
            game.SETG("CALENDAR-PAGE", game.GETG("CALENDAR-PAGE") + 1)
        game.PRSA = "V?READ"
    
    PAG = game.GETG("CALENDAR-PAGE")
    
    if RARG == "M-OBJDESC":
        game.TELL("A desk calendar is here, open to July ")
        game.TELL_N(game.GETG("CALENDAR-PAGE"))
        game.TELL(".")
        game.CRLF()
    elif game.IS_VERB("READ", "EXAMINE"):
        game.TELL("It is open to July ")
        game.TELL_N(game.GETG("CALENDAR-PAGE"))
        game.TELL(".")
        game.CRLF()
        if PAG == 8:
            game.TELL(
                "There is only one notation here, in the 9AM spot:\n"
                "\"Call Coates: Will completed\"."
            )
        elif PAG == 7:
            game.TELL(
                "The only listing here is an appointment with Baxter at 2PM\n"
                "at the Robner Corp. office."
            )
        else:
            game.TELL("Nothing of interest is scheduled on this date.")
    elif game.IS_VERB("TURN"):
        if game.PRSI != "INTNUM":
            game.TELL("Huh?")
        elif game.P_NUMBER > 30:
            game.TELL(
                "Thirty days hath September,\n"
                "April, June, and November,\n"
                "All the rest have "
            )
            game.TELL_N(game.P_NUMBER)
            game.TELL("???")
        elif game.P_NUMBER == 0:
            game.TELL("Do you suppose that would be June 30?")
        else:
            game.SETG("CALENDAR-PAGE", game.P_NUMBER)
            game.TELL("The calendar is now open to July ")
            game.TELL_N(game.P_NUMBER)
            game.TELL(".")

def NOTE_PAPER_F(game):
    """Note paper action handler"""
    if game.IS_VERB("READ", "EXAMINE"):
        if game.GETG("NOTE-READ"):
            game.PAD_READ("Examination of the paper")
        elif game.P_ADVERB == "W?CAREFULLY":
            game.TELL(
                "There are some indentations on the paper. Something may have been "
                "written on the previous sheet."
            )
        else:
            game.TELL("There doesn't seem to be anything written on the pad.")
    
    elif game.IS_VERB("RUB"):
        if not game.PRSI:
            game.TELL("You should try rubbing or shading the pad with something.")
        elif game.PRSI == "PENCIL":
            game.PAD_READ("Shading the paper with the pencil")
    
    elif game.IS_VERB("RUN-OVER") and game.PRSO == "PENCIL":
        game.PAD_READ("Running the pencil over the paper")
    
    elif game.IS_VERB("HOLD-UP") and game.PRSI == "GLOBAL-LIGHT":
        game.PAD_READ("Looking at the pad against the light")


def PAD_READ(game, STR):
    """Reveal writing impressions on the note pad"""
    game.SETG("NOTE-READ", True)
    game.TELL(STR)
    game.TELL(
        " reveals impressions left by writing on the previous sheet. The writer must "
        "have borne down heavily, but only a few words come out clearly:\n"
        "\n"
        "  Baxter,\n"
        "\n"
        "                  st time\n"
        " nsist             op       merg\n"
        "       mnidy               Oth\n"
        "          forc\n"
        "         ocumen     y poss\n"
        "  plica     y      Focus s\n"
        "          recons\n"
        "late!\n"
        "                              rsha"
    )



def READ_SECOND_SECTION(game):
    """Read the second section of the newspaper"""
    game.SETG("NEWSPAPER-READ", True)
    game.TELL(
        "In your study of the second section, a small item in the financial section "
        "catches your eye. A merger between Robner Corp. and Omnidyne is set to be "
        "concluded shortly. There is a picture of Mr. Baxter with Omnidyne president "
        "Starkwell, both smiling broadly. Baxter is quoted as saying that the deal "
        "will enable the financially ailing Robner Corp. to continue to produce the "
        "highest-quality products. The article points out that Marshall Robner, who "
        "founded Robner Corp. but is no longer its major stockholder, had been found "
        "dead yesterday morning, an apparent suicide victim. Baxter is quoted as "
        "saying that Robner was in full agreement with the terms of the merger."
    )

def NEWSPAPER_F(game):
    """Newspaper action handler"""
    if game.IS_VERB("EXAMINE", "READ", "OPEN"):
        if game.P_ADVERB in ["W?CAREFULLY", "W?SLOWLY"]:
            READ_SECOND_SECTION(game)
        else:
            game.TELL(
                "The Daily Herald is a local paper in two sections. In your cursory look at "
                "the first, you find a brief obituary for Mr. Robner. It details his career, "
                "including the formation of Robner Corp. A few years ago, Mr. Robner and the "
                "Robner Corp. were given a prestigious award for works in the community. At "
                "that time Robner said \"I am proud to accept this award for the Corporation. "
                "Robner Corp is my whole life, and I will continue to guide it for the public "
                "interest as long as I live.\" Robner himself had won great public acclaim for "
                "his charitable works."
            )

def SECOND_SECTION_F(game):
    """Second section of newspaper action handler"""
    if game.IS_VERB("TAKE"):
        if game.IS_IN("NEWSPAPER", game.WINNER):
            game.TELL("You already have the whole newspaper.")
        else:
            game.PERFORM("V?TAKE", "NEWSPAPER")
            return True
    
    elif not game.IS_IN("NEWSPAPER", game.WINNER):
        game.TELL("You don't have the newspaper.")
    
    elif game.IS_VERB("EXAMINE", "READ"):
        READ_SECOND_SECTION(game)
        return True
    
    elif game.IS_VERB("DROP"):
        game.TELL(
            "You shouldn't leave pieces of the paper lying around. At least "
            "leave the whole thing."
        )



##############################################################################################################################
##  Interupt Handlers
##############################################################################################################################


def I_MAIL(game):
    """Mail delivery interrupt routine"""
    if (game.HERE in ["FRONT-PATH"] or 
        (game.HERE == "FOYER" and game.IS_FSET("FRONT-DOOR", "OPENBIT"))):
        game.TELL(
            "A mailman walks briskly up to you, hands you an envelope, "
            "and departs."
        )
        game.MOVE("ENVELOPE", game.WINNER)
        game.FSET("ENVELOPE", "TOUCHBIT")
        return True
    
    elif game.HERE == "FOYER":
        game.TELL(
            "There is a short rap on the front door.  A moment later, a thin "
            "envelope appears under the door."
        )
        game.MOVE("ENVELOPE", "FOYER")
        game.PUTP(
            "ENVELOPE",
            "P?FDESC",
            "Partially exposed under the front door is an envelope."
        )
        game.ENABLE(game.QUEUE("I-MAIL-2", 60))
        return True
    
    else:
        game.MOVE("ENVELOPE", "FOYER-TABLE")
        game.ENABLE(game.QUEUE("I-MAIL-2", 60))
        if game.HERE in ["SOUTH-LAWN", "WEST-OF-DOOR", "EAST-OF-DOOR"]:
            game.TELL("You notice a mailman stop by the house briefly and depart.")
            return True
        else:
            return False

def I_MAIL_2(game):
    """Second mail interrupt routine"""
    if game.LOC("ENVELOPE") in ["FOYER", "FOYER-TABLE"]:
        game.ESTABLISH_GOAL("ROURKE", "FOYER", True)
        game.ENABLE(game.QUEUE("I-MAIL-3", -1))
        return False

def I_MAIL_3(game):
    """Third mail interrupt routine"""
    if game.GETG("ROURKE-MAIL"):
        if game.IS_IN("ROURKE", game.LOC("MRS-ROBNER")):
            game.QUEUE("I-MAIL-3", 0)
            game.ESTABLISH_GOAL("ROURKE", "ROURKE-ROOM", True)
            if game.IS_IN("ENVELOPE", game.WINNER) and game.IS_IN(game.WINNER, game.LOC("MRS-ROBNER")):
                game.TELL(
                    "Mrs. Rourke walks up to Mrs. Robner. \"I'm sorry, Ma'am, but this gentleman "
                    "has a letter that just arrived for you.\" Mrs. Robner grabs the letter from "
                    "you. \"That is none of your business!\""
                )
            elif not game.IS_IN("ENVELOPE", "ROURKE"):
                return True
            
            if game.HERE == game.LOC("ROURKE"):
                if game.IS_IN("ENVELOPE", "ROURKE"):
                    game.TELL("Mrs. Rourke hands an envelope to Mrs. Robner.")
                game.MOVE("ENVELOPE", "MRS-ROBNER")
                if game.GETG("ENVELOPE-OPENED"):
                    game.TELL(
                        " Mrs. Robner examines the "
                        "envelope, then turns to you. \"You did this, I suppose.\" she says. \"You had "
                        "no right! I expected better treatment than this. You would think I were "
                        "suspected of wrongdoing!\""
                    )
                else:
                    game.TELL(
                        " Mrs. Robner examines "
                        "the envelope briefly, then puts it in her pocket."
                    )
                    game.REMOVE("ENVELOPE")
                return True
            else:
                game.REMOVE("ENVELOPE")
            return False
        else:
            return False
    
    elif game.IS_IN("ROURKE", "FOYER"):
        if game.LOC("ENVELOPE") in ["FOYER-TABLE", "FOYER"]:
            game.MOVE("ENVELOPE", "ROURKE")
            game.FSET("ENVELOPE", "TOUCHBIT")
            game.ESTABLISH_GOAL("ROURKE", game.LOC("MRS-ROBNER"), True)
            game.SETG("ROURKE-MAIL", True)
            if game.HERE == "FOYER":
                game.TELL("Mrs. Rourke takes the envelope and starts to walk away.")
                return True
            else:
                return False
        else:
            game.UNPRIORITIZE("ROURKE")
            return False

def I_NEWSPAPER(game):
    """Newspaper delivery interrupt routine"""
    game.MOVE("NEWSPAPER", "FRONT-PATH")
    if game.HERE in ["SOUTH-LAWN", "FRONT-PATH"]:
        game.TELL(
            "The local paperboy, in an amazing athletic feat, throws a newspaper toward "
            "the house from a distance of at least 100 feet. It even lands beside the front "
            "door, rather than in the bushes."
        )
        return True



def I_WILL_READING(game):
    """Will reading interrupt routine"""
    if (game.GETG("PRESENT-TIME") < 760 and
        (not game.IS_IN("MRS-ROBNER", "LIVING-ROOM") or
         not game.IS_IN("DUNBAR", "LIVING-ROOM") or
         not game.IS_IN("BAXTER", "LIVING-ROOM") or
         not game.IS_IN("GEORGE", "LIVING-ROOM"))):
        game.SETG("WILL-HOLD", True)
        game.QUEUE("I-WILL-READING", -1)
        if game.HERE == "LIVING-ROOM":
            if game.PROB(70):
                return False
            elif game.PROB(50):
                game.TELL("Mr. Coates asks everyone to be patient, as not everyone is present.")
            else:
                game.TELL("Mr. Coates appears distracted, looking frequently toward the door.")
            return True
        return False
    elif game.HERE != "LIVING-ROOM":
        WILL_WAIT = game.GETG("WILL-WAIT") + 1
        game.SETG("WILL-WAIT", WILL_WAIT)
        if WILL_WAIT > 15:
            game.ENABLE(game.QUEUE("I-WILL-MISSED", -1))
            WILL_HACK(game)
            return False
        else:
            game.QUEUE("I-WILL-READING", -1)
            return False
    
    if game.HERE == "LIVING-ROOM":
        game.SETG("AT-READING", True)
        if game.GETG("PRESENT-TIME") > 720 and game.GETG("WILL-WAIT") > 3:
            game.TELL(
                "The people present turn to look at you. Mrs. Robner glares at you. \"You "
                "might at least have the courtesy to be here on time! Haven't you caused enough "
                "disruption already? We should have started without you. Mr. Coates, please "
                "proceed.\""
            )
        elif game.GETG("PRESENT-TIME") > 760:
            game.TELL("\"It's late, so let's begin!\" Coates says.")
        elif game.GETG("WILL-HOLD"):
            game.TELL("\"Ah!\" Mr. Coates says, \"Everybody's here now.\"")
        
        game.TELL(
            "Mr. Coates begins: \"This is an awkward situation. Mr. Robner told me five "
            "days ago that he wanted to execute a new will, and promised to call me when "
            "it was completed. As I never heard from him, I must assume that he either "
            "changed his mind or did not complete the new will. Therefore, the one in my "
            "possession must be considered the most recent testament.\""
        )
        
        if game.GETG("G-CALENDAR"):
            game.TELL(
                "You notice that George, who was not initially paying close attention, now "
                "perks up and begins to look about anxiously."
            )
        else:
            game.TELL(
                "From the corner of your eye, you catch George nodding his head, as "
                "if in approval, and smiling broadly."
            )
        
        game.TELL(
            "Continuing, Mr. Coates says: \"Naturally, should a more recent will exist "
            "and be found within a reasonable period, the present one will be voided. "
            "I will proceed with reading the will here in my hands, which was executed "
            "three years ago last month.\" He reads the will, simply written and direct, "
            "leaving equal parts of the estate to his son, George Arthur Robner, and "
            "his wife, Mrs. Leslie Phillips Robner."
        )
        
        game.TELL(
            "There is some discussion, understated congratulations and overstated "
            "sympathy, which Mr. Coates cuts short by clearing his throat. \"I must "
            "leave now, I'm afraid. If you have any questions, I can be contacted "
            "tomorrow.\" He picks up the phone, dials his office, and asks to be "
            "picked up at the Robner estate."
        )
        
        if game.GETG("G-CALENDAR"):
            game.TELL("George, now looking quite upset, starts for the door.")
        
        WILL_HACK(game)
        return True
    
    WILL_HACK(game)
    return False

def WILL_HACK(game):
    """Helper routine for will reading completion"""
    game.ESTABLISH_GOAL("COATES", "SOUTH-LAWN", True)
    game.SETG("WILL-TIME", game.GETG("PRESENT-TIME"))
    game.SETG("POST-WILL", True)
    game.QUEUE("I-WILL-READING", 0)
    if game.GETG("G-CALENDAR"):
        GEORGE_HACK(game)

def GEORGE_HACK(game):
    """George's reaction after will reading"""
    GL = game.LOC("GEORGE")
    if GL == game.HERE:
        if GL == "GEORGE-ROOM":
            game.TELL(
                "George paces around. \"I just remembered,\" he says, \"I've got some personal "
                "business to attend to. Would you mind?\" He shows you to the door."
            )
        elif game.GETP(GL, "P?LINE") == "TOP-OF-THE-LINE-C":
            game.TELL(
                "\"I'm...I really have some business to do in my room. I'll speak "
                "to you later,\" George says. He starts off toward his room."
            )
        else:
            game.TELL(
                "\"I've...got to be going now. I'll see you later,\" George says. "
                "He starts to leave."
            )
    
    if GL != "GEORGE-ROOM":
        game.ESTABLISH_GOAL("GEORGE", "GEORGE-ROOM", True)
    
    game.SETG("GEORGE-SEQUENCE", True)
    game.ENABLE(game.QUEUE("I-GEORGE-HACK", -1))


def I_GEORGE_HACK(game):
    """George's post-will reading behavior"""
    GL = game.LOC("GEORGE")
    GT = game.GET(game.GOAL_TABLES, game.GETP("GEORGE", "P?CHARACTER"))
    TMP = False
    
    if game.GETG("GEORGE-READY"):
        if game.HERE == GL:
            game.SETG("GEORGE-READY", False)
            game.SETG("GEORGE-SCREAM", False)
            game.SETG("GEORGE-WAIT", 1)
            game.TELL(
                "\"I don't understand you, Inspector. I asked to be alone so I can take care "
                "of some business. I...I don't see why you have to snoop around here like I was "
                "some sort of suspect.\""
            )
            if game.GETG("GEORGE-SCREAM"):
                game.TELL(
                    "\"I said to close that door and not to come in! You must be deaf as well as "
                    "stupid!\""
                )
            return True
        elif game.FSET("GEORGE-DOOR", "OPENBIT") and not game.GETG("GEORGE-SCREAM"):
            game.TELL(
                "As the door opens, you hear George say \"Close that door! I'm working!\""
            )
            game.SETG("GEORGE-SCREAM", True)
            return True
    elif game.GETG("GEORGE-WAIT"):
        if game.HERE == GL:
            game.TELL(
                "George paces around the room, awaiting your departure with ill-concealed "
                "impatience."
            )
            game.SETG("GEORGE-WAIT", game.GETG("GEORGE-WAIT") + 1)
            if game.GETG("GEORGE-WAIT") > 12:
                game.TELL(
                    "\"I can't take this. You get on my nerves. I'm leaving.\""
                )
                if game.HERE == game.GET(GT, "GOAL-QUEUED"):
                    game.PUT(GT, "GOAL-QUEUED", "LIVING-ROOM")
                game.UNPRIORITIZE("GEORGE")
                game.SETG("GEORGE-WAIT", False)
                game.QUEUE("I-GEORGE-HACK", 0)
                game.ENABLE(game.QUEUE("GEORGE-HACK", 30))
            return True
        else:
            game.SETG("GEORGE-WAIT", False)
            game.FCLEAR("GEORGE-DOOR", "OPENBIT")
            if game.HERE in ["LIBRARY", "CORRIDOR-4", "CORRIDOR-3"]:
                game.TELL("You hear George's door close.")
    elif GL == "GEORGE-ROOM":
        if game.HERE == GL:
            game.TELL(
                "\"I have business to attend to. Would you mind leaving?\""
            )
            game.SETG("GEORGE-WAIT", 1)
        else:
            game.ENABLE(game.QUEUE("I-GEORGE-HACK-2", 5))
            game.SETG("GEORGE-READY", True)
            if game.HERE in ["CORRIDOR-4", "CORRIDOR-3"] and game.FSET("GEORGE-DOOR", "OPENBIT"):
                game.FCLEAR("GEORGE-DOOR", "OPENBIT")
                TMP = True
                game.TELL("You hear George's door close.")
            game.FCLEAR("GEORGE-DOOR", "OPENBIT")
            return TMP
    elif game.HERE == GL:
        if not game.GETG("GEORGE-FOLLOW"):
            game.SETG("GEORGE-FOLLOW", True)
            return False
        elif game.PROB(50):
            game.TELL(
                "\"Please stop following me around like this. Can I have no privacy? I'm "
                "simply trying to take care of something personal.\""
            )
        else:
            game.TELL(
                "\"Stop following me. My business is private.\""
            )
    elif GL == "CORRIDOR-4":
        if (game.BAND(game.GETP(game.HERE, "P?CORRIDOR"), 1) == 1):
            game.TELL(
                "George glances in your direction, then enters his room."
            )
            game.MOVE("GEORGE", "GEORGE-ROOM")
    elif GL in ["CORRIDOR-3", "CORRIDOR-2"] and game.HERE in ["CORRIDOR-1", "STAIR-TOP"]:
        game.TELL(
            "George glances back at you briefly, then continues on his way."
        )

# At this point, George is in his room having waited for some
# time for his moment to try to enter the library secretly.
# I-GEORGE-HACK is still enabled and running every move to
# detect the chomper entering the room.

def I_GEORGE_HACK_2(game):
    """George's attempt to sneak into the library"""
    if game.GETG("GEORGE-READY"):
        if ((game.BAND(game.GETP(game.HERE, "P?CORRIDOR"), 1) == 1) or 
            game.HERE == "LIBRARY"):
            game.QUEUE("I-GEORGE-HACK-2", game.RANDOM(9))
            if game.HERE in ["CORRIDOR-2", "CORRIDOR-1", "STAIR-TOP"]:
                if game.PROB(30):
                    game.TELL(
                        "A door opens down the hall. George steps out, spots you, and looks briefly "
                        "toward the window. After a moment he steps back into his room and shuts the "
                        "door."
                    )
                else:
                    game.TELL(
                        "You faintly hear a door open and then close near the end of the hall."
                    )
            elif game.HERE in ["CORRIDOR-4", "LIBRARY"]:
                game.TELL("You hear George's door open and ", end="")
                if game.PROB(30):
                    game.TELL(
                        "you catch a brief glimpse of his "
                        "head darting back into the doorway. You watch as the door closes again."
                    )
                else:
                    game.TELL("close again immediately.")
            elif game.FSET("GEORGE-DOOR", "OPENBIT"):
                game.FCLEAR("GEORGE-DOOR", "OPENBIT")
                game.TELL(
                    "George walks up to his door and slams it in your face."
                )
            elif game.HERE == "CORRIDOR-3":
                game.TELL(
                    "George opens his door and peeks out. He is startled by your presence, "
                    "excuses himself, and closes the door sharply in your face before you can "
                    "utter a word."
                )
        else:
            game.QUEUE("I-GEORGE-HACK", 0)
            game.MOVE("GEORGE", "LIBRARY")
            game.FSET("GEORGE-DOOR", "OPENBIT")
            game.QUEUE("I-GEORGE-HACK-2", 0)
            game.ENABLE(game.QUEUE("I-GEORGE-HACK-3", -1))
            if game.HERE == "UPSTAIRS-CLOSET":
                game.TELL(
                    "You hear George's door open and you see his head poke out briefly, scanning "
                    "the hallway. He apparently didn't see you, and darts across the hall to the "
                    "library."
                )
            elif game.HERE == "LIBRARY-BALCONY":
                game.TELL(
                    "You see George through the doorway, looking down the hallway, then darting "
                    "into the library."
                )
    else:
        game.QUEUE("I-GEORGE-HACK-2", game.RANDOM(9))
        return False

def I_GEORGE_HACK_3(game):
    """George's actions in the library with the hidden closet"""
    FLG = False
    
    if game.GETG("GEORGE-SEARCH") == 0:
        if game.HERE == "LIBRARY-BALCONY":
            game.TELL(
                "George walks purposefully toward the bookshelves. He looks around, but you "
                "react before he can see you. When you peek out again, George is fiddling with "
                "the shelves. His right arm reaches into the shelf and, to your amazement, the "
                "unit of bookshelves on the left rotates away from the wall, revealing a "
                "darkened room behind. George enters it, trembling with barely controlled fear "
                "and excitement."
            )
            FLG = True
            game.SETG("BOOKS-MOVED", True)
            game.SETG("GEORGE-MOVES-BOOKS", True)
            game.MOVE("GEORGE", "HIDDEN-CLOSET")
        elif game.HERE == "LIBRARY":
            game.TELL(
                "George hears you walk through the balcony doors and recoils in horror. He "
                "runs across the hall to his own bedroom, slamming his door shut."
            )
            FLG = True
            game.SETG("GEORGE-READY", False)
            game.SETG("GEORGE-WAIT", False)
            game.FCLEAR("GEORGE-DOOR", "OPENBIT")
            game.MOVE("GEORGE", "GEORGE-ROOM")
            game.QUEUE("I-GEORGE-HACK-3", 0)
            game.QUEUE("I-GEORGE-HACK-2", 10)
        else:
            game.MOVE("GEORGE", "HIDDEN-CLOSET")
            game.SETG("BOOKS-MOVED", True)
    elif game.GETG("GEORGE-SEARCH") == 1:
        if game.HERE in ["LIBRARY", "LIBRARY-BALCONY"]:
            game.TELL(
                "A dim light in the hidden closet comes on. In the faint light, you can see "
                "George motioning with his right hand. All at once, the shelf swings shut!"
            )
            FLG = True
    elif game.GETG("GEORGE-SEARCH") < 10:
        if game.FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.TELL(
                "As the bookshelf swings open, you see George carefully dialing a combination "
                "into a large wall safe. He turns in panic and, with an exclamation, knocks you "
                "down and bolts out of the library."
            )
            FLG = True
            game.SETG("SAFE-SEEN", True)
            game.SETG("GEORGE-SEARCH", 0)
            game.QUEUE("I-GEORGE-HACK-3", 0)
            game.MOVE("GEORGE", "CORRIDOR-1")
            game.ESTABLISH_GOAL("GEORGE", "EAST-LAWN", True)
    elif game.GETG("GEORGE-SEARCH") < 16:
        if game.FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.FSET("SAFE", "OPENBIT")
            game.SETG("SAFE-SEEN", True)
            game.TELL(
                "As the shelf swings open, George spins to face you. His expression, first "
                "seemingly wild with happiness, changes to one of panic and horror. He jerks "
                "around, trying feebly to conceal a piece of paper in his hands. He jumps "
                "toward you, then recoils in fear. Finally, sobbing, he crumples to the floor, "
                "clutching the paper beneath him. A large combination safe, imbedded in a wall, "
                "is lying open. You enter the hidden closet."
            )
            FLG = True
            game.QUEUE("I-GEORGE-HACK-3", 0)
            game.MOVE("NEW-WILL", "GEORGE")
            game.GOTO("HIDDEN-CLOSET")
            game.ENABLE(game.QUEUE("I-GEORGE-LEAVE-CLOSET", 10))
            game.HERE = "HIDDEN-CLOSET"
            game.SETG("NEW-WILL-SEEN", True)
    elif game.GETG("GEORGE-SEARCH") == 16:
        game.FCLEAR("SAFE", "OPENBIT")
        if game.HERE == "LIBRARY":
            game.TELL(
                "Suddenly, the bookshelves swing out, forming an opening to a dark area "
                "behind. George starts to emerge but stops suddenly as he notices you! With "
                "jack-rabbit reflexes, he darts back inside. Before you can act, the "
                "shelves close again."
            )
            FLG = True
            game.MOVE("GEORGE", "NORTH-LAWN")
            game.MOVE("SOGGY-WILL", "LAKE")
            game.REMOVE("NEW-WILL")
            game.QUEUE("I-GEORGE-HACK-3", 0)
            game.SETG("GEORGE-RUN", game.PRESENT_TIME)
        else:
            game.MOVE("GEORGE", "LIBRARY")
            game.QUEUE("I-GEORGE-HACK-3", 0)
            game.UNPRIORITIZE("GEORGE")
            game.ESTABLISH_GOAL("GEORGE", "NORTH-LAWN", True)
            if game.HERE == "LIBRARY-BALCONY":
                game.TELL(
                    "Suddenly, the shelf swings out, and George emerges. He walks over to a "
                    "special place in the shelves and reaches behind some books. The bookshelves "
                    "silently assume their normal position."
                )
                FLG = True
    
    game.SETG("GEORGE-SEARCH", game.GETG("GEORGE-SEARCH") + 1)
    return FLG

def I_GEORGE_LEAVE_CLOSET(game):
    """George leaves the hidden closet"""
    if game.IN("GEORGE", "HIDDEN-CLOSET"):
        game.ESTABLISH_GOAL("GEORGE", "GEORGE-ROOM")
        return False

def I_CALL(game):
    """Phone call event handling"""
    MRL = game.LOC("MRS-ROBNER")
    
    if game.GETG("CALL-RING"):
        if MRL == "LIVING-ROOM":
            game.SETG("CALL-RING", False)
            if game.HERE == "LIVING-ROOM":
                game.TELL(
                    "Mrs. Robner picks up the phone. \"Oh, hi. Look, I can't talk now. I'll call "
                    "you later, okay? Bye, then.\" She hangs up the phone."
                )
                game.ROBNER_CALL_MOVE()
                return True
            game.ROBNER_CALL_MOVE()
            return False
        else:
            game.TELL("The phone rings again.")
            if game.GLOBAL_IN("TELEPHONE", game.HERE):
                game.THIS_IS_IT("TELEPHONE")
            return True
    
    if game.GETG("CALL-IN-PROGRESS"):
        game.SETG("CALL-IN-PROGRESS", game.GETG("CALL-IN-PROGRESS") + 1)
        if game.GETG("CALL-IN-PROGRESS") > 15:
            game.SETG("CALL-IN-PROGRESS", False)
            game.QUEUE("I-CALL", 0)
            game.UNPRIORITIZE("MRS-ROBNER")
            return False
        elif game.FSET("MASTER-BEDROOM-DOOR", "OPENBIT") or game.HERE == "MASTER-BEDROOM":
            game.TELL(
                "Mrs. Robner speaks quietly into the phone and hangs up."
            )
            game.SETG("CALL-IN-PROGRESS", False)
            game.QUEUE("I-CALL", 0)
            game.UNPRIORITIZE("MRS-ROBNER")
            return True
    elif game.GETG("CALL-WAITING"):
        if game.HERE in [MRL, "MASTER-BATH", "BEDROOM-BALCONY"]:
            game.SETG("CALL-WAITING", game.GETG("CALL-WAITING") + 1)
            if not game.GETG("CALL-WAITING") > 3:
                game.TELL(
                    "Mrs. Robner glares at you, holding the phone in one hand. \"Would you "
                    "mind terribly?\", she asks."
                )
            elif game.GETG("CALL-MOVE"):
                game.TELL(
                    "\"I can't understand why you won't let me use the phone. Can't I talk to "
                    "my best friend? Hummph...I suppose it can wait, since you are being "
                    "so...uh...unhelpful.\" She puts down the receiver, rises from her bed, and "
                    "starts to leave."
                )
                game.SETG("CALL-MOVE", False)
                game.SETG("CALL-WAITING", False)
                game.QUEUE("I-CALL", 0)
                game.UNPRIORITIZE("MRS-ROBNER")
            else:
                game.TELL(
                    "\"I give up. What IS your problem, anyway?,\" Mrs. Robner asks, in a "
                    "barely controllable rage. \"I'll call you back,\" she says, and slams down "
                    "the receiver."
                )
                game.SETG("CALL-MOVE", False)
                game.QUEUE("I-CALL", 0)
                game.UNPRIORITIZE("MRS-ROBNER")
        else:
            game.ESTABLISH_CALL()
            return False
    elif game.GETG("CALL-MOVE"):
        if MRL == "MASTER-BEDROOM":
            if game.HERE in ["BEDROOM-BALCONY", "MASTER-BATH", "MASTER-BEDROOM"]:
                if game.HERE != "MASTER-BEDROOM":
                    game.TELL(
                        "Mrs. Robner enters her bedroom and spots you."
                    )
                game.TELL(
                    "\"I'd like to make a private phone call, if you have no objection,\" she "
                    "says. She motions toward the door."
                )
                game.SETG("CALL-WAITING", 1)
            else:
                game.ESTABLISH_CALL()
                return False
    elif game.HERE in ["LIBRARY", "LIVING-ROOM", "MASTER-BEDROOM"]:
        game.TELL("The telephone rings.")
        game.THIS_IS_IT("TELEPHONE")
        game.ESTABLISH_GOAL("MRS-ROBNER", "LIVING-ROOM", True)
        game.SETG("CALL-RING", True)
        game.QUEUE("I-CALL", -1)
    elif game.HERE == MRL:
        game.TELL(
            "You can hear a telephone ringing in a nearby room. Mrs. Robner "
            "says \"Pardon me\" and starts for the door."
        )
        game.SETG("CALL-RING", True)
        game.QUEUE("I-CALL", -1)
        game.ESTABLISH_GOAL("MRS-ROBNER", "LIVING-ROOM", True)
    else:
        if game.GETP(game.HERE, "P?LINE") != "OUTSIDE-LINE-C":
            game.TELL(
                "You hear a phone ringing in a nearby room."
            )
            game.SETG("CALL-RING", True)
            game.QUEUE("I-CALL", -1)
            game.ESTABLISH_GOAL("MRS-ROBNER", "LIVING-ROOM", True)
        elif game.PROB(50):
            game.TELL(
                "You notice a very faint ringing sound coming from the house."
            )
            game.ROBNER_CALL_MOVE()
            return True
        

def THIS_IS_IT(game, OBJ):
    """Set the 'it' referent for parser"""
    game.SETG("P-IT-OBJECT", OBJ)
    game.SETG("P-IT-LOC", game.HERE)

def ESTABLISH_CALL(game):
    """Establish Mrs. Robner's phone call"""
    COR = None  # Local variable, though not used in the routine
    game.SETG("CALL-MOVE", False)
    game.SETG("CALL-IN-PROGRESS", 1)
    game.FCLEAR("MASTER-BEDROOM-DOOR", "OPENBIT")
    if game.HERE == "CORRIDOR-1":
        game.TELL(
            "Mrs. Robner shuts the door to the master bedroom."
        )
    elif game.HERE in ["CORRIDOR-2", "STAIR-TOP"]:
        game.TELL(
            "You hear the master bedroom door shut."
        )

def MASTER_BEDROOM_DOOR_F(game):
    """Master bedroom door handler"""
    if game.VERB("LISTEN") and game.GETG("CALL-IN-PROGRESS"):
        game.TELL(
            "You can hear the muffled voice of Mrs. Robner through the door."
        )
    elif game.VERB("KNOCK"):
        if game.GETG("CALL-IN-PROGRESS"):
            game.TELL(
                "Mrs. Robner's calls out. \"Wait just one minute!\""
            )
        else:
            game.DOOR_F()

def DOOR_F(game):
    """Generic door handler"""
    if game.VERB("LISTEN"):
        game.TELL("You can't hear anything through the door.")
    elif game.VERB("KNOCK"):
        if (game.PRSO == "FRONT-DOOR" and 
            not game.GETG("WELCOMED") and 
            game.PRESENT_TIME < 700 and 
            game.HERE == "FRONT-PATH"):
            game.TELL(
                "You hear footsteps inside the house. Mrs. Robner, dressed in black, "
                "opens the door and greets you."
            )
            game.WELCOME()
        elif game.INHABITED(game.DOOR_ROOM()):
            game.TELL("A muffled voice says, \"Come in!\"")
        else:
            game.TELL(
                "There is no answer at the door."
            )



def ROBNER_CALL_MOVE(game):
    """Move Mrs. Robner to make a call"""
    game.SETG("ROBNER-OLD-LOC", game.LOC("MRS-ROBNER"))
    game.ESTABLISH_GOAL("MRS-ROBNER", "MASTER-BEDROOM", True)
    game.SETG("CALL-MOVE", True)
    game.QUEUE("I-CALL", -1)

def TELEPHONE_F(game):
    """Telephone handler"""
    if game.HERE not in ["LIBRARY", "MASTER-BEDROOM", "LIVING-ROOM"]:
        game.TELL("There's no telephone here.")
    elif game.VERB("FIND"):
        game.TELL("You are the detective, after all.")
    elif game.VERB("TAKE", "LISTEN", "REPLY"):
        if game.GETG("CALL-RING"):
            game.TELL(
                "You take the phone and hear an unfamiliar man's voice "
                "say \"Hello?  Is Leslie there?\"  You start to reply, but Mrs. Robner", end=""
            )
            if game.HERE == "LIVING-ROOM":
                game.TELL(
                    " enters and takes the phone from you. \"Thank you, inspector,\" she says, and "
                    "then into the telephone: \"Hello? Oh, hi. I can't really talk now. I'll call "
                    "you back soon, OK? Bye.\" She hangs up and starts toward the door."
                )
            else:
                game.TELL(
                    " picks up the phone from another extension and hears you. \"I've got it, "
                    "inspector,\" she says. \"Hello? Oh, it's you. I can't talk now. I'll call "
                    "you back soon. Bye!\" You hear two clicks and the line goes dead."
                )
            game.SETG("CALL-RING", False)
            game.MOVE("MRS-ROBNER", "LIVING-ROOM")
            game.ROBNER_CALL_MOVE()
        elif game.GETG("CALL-IN-PROGRESS"):
            game.TELL(
                "You can hear Mrs. Robner and a man whose voice you don't recognize.\n"
                "Robner: \"...much too early to consider it.\"\n"
                "Man's Voice: \"But we couldn't have planned it better. You're free.\"\n"
                "Robner: \"Yes, but it will...Wait a second...I think...\"\n"
                "\"Click.\" You realize that the call has been disconnected."
            )
            game.SETG("CALL-OVERHEARD", True)
            game.SETG("CALL-IN-PROGRESS", False)
            game.QUEUE("I-CALL", 0)
            game.UNPRIORITIZE("MRS-ROBNER")
        else:
            game.TELL(
                "All you hear is a dial tone."
            )

def ENVELOPE_F(game):
    """Envelope handler"""
    if game.VERB("OPEN"):
        if game.LOC("MRS-ROBNER") == game.HERE:
            game.TELL(
                "Mrs. Robner grabs the envelope from you. \"That,\" she "
                "says, \"is none of your business!\""
            )
            game.MOVE("ENVELOPE", "MRS-ROBNER")
            return True
        game.SETG("ENVELOPE-OPENED", True)
        if not game.IN("ENVELOPE", game.WINNER) and game.ITAKE(False):
            game.TELL("(Taken)")
        return False
    elif game.VERB("CLOSE") and game.GETG("ENVELOPE-OPENED"):
        game.TELL(
            "You close the envelope carefully, but it still looks like it has been "
            "opened."
        )
        game.FCLEAR("ENVELOPE", "OPENBIT")
        return True

def IS_IN_MOTION(game, PERSON):
    """Check if a person is in motion"""
    GT = game.GET(game.GOAL_TABLES, game.GETP(PERSON, "P?CHARACTER"))
    if (game.GET(GT, "GOAL-ENABLE") and 
        game.GET(GT, "GOAL-S") and 
        game.LOC(PERSON) != game.GET(GT, "GOAL-F")):
        return True
    else:
        return False


def MRS_ROBNER_F(game, RARG=False):
    """Mrs. Robner character handler"""
    if not RARG and game.VERB("GIVE") and game.PRSO == "ENVELOPE":
        game.PERFORM("V?SHOW", "MRS-ROBNER", "ENVELOPE")
        return True
    
    if RARG == "M-OBJDESC":
        if game.IS_IN_MOTION("MRS-ROBNER"):
            if game.GETG("CALL-MOVE"):
                game.TELL("Mrs. Robner appears to be in a hurry.")
            return True
        elif game.GETG("CALL-WAITING"):
            game.TELL("Mrs. Robner is staring at you.")
        elif game.IN("MRS-ROBNER", "KITCHEN"):
            game.TELL("Mrs. Robner is preparing a meal.")
        elif game.IN("MRS-ROBNER", "DINING-ROOM"):
            game.TELL("Mrs. Robner is eating breakfast here.")
        elif game.IN("MRS-ROBNER", "LIVING-ROOM"):
            if game.GETG("POST-WILL"):
                return True
            else:
                game.TELL("Mrs. Robner is sitting here, knitting.")
        elif game.IN("MRS-ROBNER", "MASTER-BEDROOM"):
            game.TELL("Mrs. Robner is sitting on her bed.")
        else:
            game.TELL("Mrs. Robner is here.")
        game.CARRY_CHECK("MRS-ROBNER")
    elif game.VERB("HELLO", "GOODBYE"):
        game.TELL("Mrs. Robner says a curt \"", end="")
        if game.VERB("HELLO"):
            game.TELL("Hello", end="")
        else:
            game.TELL("Bye", end="")
        game.TELL("\".")
    elif game.WINNER == "MRS-ROBNER":
        if game.VERB("FIND"):
            return False
        elif game.VERB("OPEN") and game.PRSO == "ENVELOPE":
            if game.GETG("ENVELOPE-OPENED"):
                game.TELL(
                    "\"You seem to have taken care of that already.\""
                )
            else:
                game.TELL(
                    "\"I believe there are laws protecting the privacy of mail. I will not "
                    "open the envelope for you or anyone else.\""
                )
        elif game.COM_CHECK("MRS-ROBNER"):
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
    elif game.VERB("ARREST") and (game.GETG("ENVELOPE-OPENED") or game.GETG("CALL-OVERHEARD")):
        if not game.FSET("LAB-REPORT", "TOUCHBIT"):
            game.MURDER_NOT_PROVEN("MRS-ROBNER")
            return True
        game.TELL(
            "Sergeant Duffy enters and leads Mrs. Robner away.\n\n"
        )
        game.END_HEADER("August 2")
        game.TELL(
            "I am sorry to inform you that the grand jury investigating the murder charge "
            "against Mrs. Robner declined to indict her, citing a lack of evidence linking "
            "her with the execution of the crime. Please try to be more cautious when "
            "making arrests in the future.\n\n"
        )
        game.CASE_OVER()
    elif game.VERB("ASK-ABOUT") and game.PRSO == "MRS-ROBNER":
        if not game.GRAB_ATTENTION("MRS-ROBNER"):
            return True
        elif game.PRSI == "GLOBAL-HIDDEN-CLOSET":
            if game.GETG("HC-ROBNER"):
                game.TELL(
                    "\"I'm quite shocked about it. I really had no idea!\""
                )
            else:
                game.TELL(
                    "\"I don't know what you're talking about, Inspector. I know of "
                    "no such closet.\""
                )
        elif game.PRSI in ["GLOBAL-ALLERGONE", "ALLERGONE", "ALLERGONE-BOTTLE"]:
            game.TELL(
                "\"I have some allergies, Inspector. Simply dreadful in the fall and spring. "
                "That's what the Allergone is for. I don't use them much this time of year, "
                "though.\""
            )
        elif game.PRSI in ["GLOBAL-SNEEZO", "SNEEZO", "SNEEZO-BOTTLE"]:
            game.TELL(
                "\"Sneezo is a wonderful cold remedy. Whenever I get a cold, I just take "
                "a few, and I usually feel much better before long.\""
            )
        elif game.PRSI == "GLOBAL-CALL":
            if game.GETG("CALL-OVERHEARD") and game.GETG("MR-ENVELOPE"):
                game.TELL(
                    "\"I guess you know it was Steven. I admit we were lovers, and we planned to "
                    "marry if I could get a divorce from Marshall. He refused to consider it, the "
                    "divorce I mean, even though he had no time for me anymore. He was married to "
                    "the company, and he refused to see my side of things. Steven was suggesting "
                    "that now we could marry. I told him I thought the timing was poor, or at least "
                    "I would have if you hadn't eavesdropped.\""
                )
            elif game.GETG("CALL-OVERHEARD"):
                game.TELL(
                    "\"I was talking to a good friend of mine. We were discussing some plans we "
                    "made; of course they had to be changed, under the circumstances. They are none "
                    "of your business. They don't concern my husband's suicide at all, I assure "
                    "you.\""
                )
            else:
                game.TELL(
                    "\"It was just a friend of mine, offering his condolences.\""
                )
        elif game.PRSI == "GLOBAL-STEVEN":
            if not game.GETG("MR-ENVELOPE"):
                game.TELL(
                    "\"I don't know who you mean. I have no friend named Steven.\""
                )
            elif game.GETG("CALL-OVERHEARD") and game.GETG("MR-ENVELOPE"):
                game.TELL(
                    "\"I might as well tell you. Steven and I were lovers and we were going to be "
                    "married if I could divorce Marshall. I asked Marshall about it, but he became "
                    "angry and refused. I didn't know what to do. Don't look at me that way. I had "
                    "nothing to do with my husband's death. Driving him to it with talk of divorce? "
                    "You didn't know Marshall, that's for sure! I should've told the police "
                    "earlier, I suppose, but it's really none of your business.\""
                )
            elif game.GETG("MR-ENVELOPE"):
                game.TELL(
                    "\"Steven is a close personal friend. We have known each other for many "
                    "years, and I visit his home frequently. Marshall knew of our friendship "
                    "and didn't begrudge it in the slightest. My husband and I had a very "
                    "trusting relationship. You may find the idea of trust difficult to understand, "
                    "I suppose.\""
                )
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "\"I loved my husband, no matter what you may think. I am very sorry to have "
                "lost him.\" The speech is almost a set piece, and not too convincing."
            )
        elif game.PRSI in ["GEORGE", "GLOBAL-GEORGE"]:
            game.DISCRETION("MRS-ROBNER", "GEORGE")
            game.TELL(
                "\"A child. He may be a man in age, but he still hasn't really grown up. He'll "
                "find himself someday, but in the meantime he can be a trial. I guess Marshall "
                "and I were too lenient. We probably still are, but he is our son, after all. "
                "We can't throw him out on the street.\""
            )
        elif game.PRSI in ["BAXTER", "GLOBAL-BAXTER"]:
            game.TELL(
                "\"Baxter has been my husband's partner for a long time, but they're not close "
                "friends. Baxter has always had the head for making money, and Marshall had the "
                "creative spark for new products. The two of them were perfect for each other "
                "in the early days. Of course, things haven't been going well lately. I guess "
                "none of that matters much now.\""
            )
        elif game.PRSI in ["CORPSE", "DUNBAR", "GLOBAL-DUNBAR"]:
            game.DISCRETION("MRS-ROBNER", "DUNBAR")
            game.TELL(
                "\"I've always thought she was a bit too smug in her relationships around "
                "here. A bit above herself, if you see my meaning. After all, she's really "
                "just a glorified secretary. She acts as though she's part of the family, and "
                "she does get along well with almost everyone here. I swear, though, Marshall "
                "spent more time with her than me, lately. Um...not that I'm trying to imply "
                "that anything went on between them. Quite the contrary.\""
            )
        elif game.PRSI in ["ROURKE", "GLOBAL-ROURKE"]:
            game.DISCRETION("MRS-ROBNER", "ROURKE")
            game.TELL(
                "\"She's an excellent housekeeper and sometimes even helps with the cooking "
                "For all her good qualities, though, she's too much of a snoop and a gossip. "
                "She tires to keep track of everyone around here. It's unnerving sometimes. "
                "But, as servants go these days, she's quite extraordinary.\""
            )
        elif game.PRSI in ["GARDENER", "GLOBAL-GARDENER"]:
            game.TELL(
                "\"I don't pay much attention to him. He's worked out well; the grounds are "
                "in excellent condition. You must take a look at his roses while you're here. "
                "They're really spectacular.\""
            )
        elif game.PRSI == "GLOBAL-OLD-WILL":
            if game.GETG("WILL-TIME") > 0:
                game.TELL(
                    "\"It's what I expected, really.\""
                )
            else:
                game.TELL(
                    "\"Marshall takes care of that sort of thing. The will, I suppose, leaves "
                    "the estate to George and me, but I can't be sure.\""
                )
        elif game.PRSI == "NEW-WILL":
            game.TELL(
                "\"What do you know? Marshall changed the will, after all. Where did you ever "
                "find this? What? George was trying to destroy it? I'm shocked. You don't think "
                "George had anything to do...\" She stops short."
            )
        elif game.PRSI == "GLOBAL-NEW-WILL":
            game.TELL(
                "\"If there is a new will, I certainly don't know where it is.\""
            )
        elif game.PRSI == "GLOBAL-FOCUS":
            game.TELL(
                "\"Oh, you mean the \"scandal\"? Focus Corporation was a subsidiary of Robner "
                "Corp. some years ago. There was a big to-do about misuse of funds or some such "
                "thing, but Marshall kept it pretty quiet. He told me that the people "
                "responsible were forced out of the company, but that charges weren't pressed "
                "to avoid bad publicity. I didn't realize anyone remembered that.\""
            )
        elif game.PRSI == "GLOBAL-SAFE":
            game.TELL(
                "\"I don't know of a safe in the house, although it's perfectly "
                "believable that Marshall has one hidden somewhere. It would appeal "
                "to his childish side, I think.\""
            )
        else:
            game.TELL(
                "\"I don't know much about that.\""
            )
    elif game.VERB("CONFRONT", "SHOW"):
        if not game.GRAB_ATTENTION("MRS-ROBNER"):
            return True
        elif game.PRSI == "LAB-REPORT":
            game.TELL(
                "Mrs. Robner reads the report with shocked disbelief. \"I...I don't know what "
                "to say. Who would want to kill Marshall? He was so well liked and...\" She "
                "breaks down, sobbing."
            )
        elif game.PRSI == "NEW-WILL":
            game.TELL(
                "Mrs. Robner reads the will. \"That's that, then,\" she says. "
                "\"I guess Marshall was pushed too far.\""
            )
        elif game.PRSI in ["ENVELOPE", "LETTER"]:
            if not game.GETG("ENVELOPE-OPENED"):
                game.TELL(
                    "\"Thank you, Inspector. The envelope is for me.\" She takes the "
                    "envelope from you and examines it briefly."
                )
                game.MOVE("ENVELOPE", "MRS-ROBNER")
                return True
            game.SETG("MR-ENVELOPE", True)
            game.TELL(
                "\"You have certainly stooped to a new low, Inspector. Opening people's mail. "
                "I think there are laws against that sort of thing, but I guess you wouldn't "
                "know.", end=""
            )
            if game.GETG("CALL-OVERHEARD"):
                game.TELL(
                    " I suppose you also know that Steven is "
                    "my lover and that we were planning to marry. Don't look so melodramatic: I "
                    "didn't kill my husband. You think my talk of divorce may have driven him to "
                    "it? Why don't you leave me alone!\""
                )
            else:
                game.TELL(
                    " In any case, what of it? It's from a friend of mine, an old friend from "
                    "school. We get together now and then to discuss old times. I don't suppose "
                    "there is a law against that?\""
                )



def BOOKSHELVES_F(game):
    """Bookshelves handler"""
    if game.VERB("TAKE") and game.PRSI == "BOOKSHELVES":
        game.TELL(
            "That would make an ungodly pile of books on the floor and take most of "
            "the day."
        )
    elif game.VERB("TAKE"):
        game.TELL(
            "You have better things to do than taking books from the shelves."
        )
    elif game.VERB("READ"):
        game.TELL(
            "Reading, while educational, will not help you solve this case."
        )
    elif game.VERB("LOOK-BEHIND"):
        game.TELL(
            "It would take all day to look behind all of the books."
        )
    elif game.VERB("EXAMINE", "SEARCH"):
        game.TELL(
            "The shelves contain many books and manuscripts covering a wide range of "
            "subjects. They are meticulously arranged."
        )
        if (game.GETG("GEORGE-MOVES-BOOKS") or 
            (game.GETG("BOOKS-MOVED") and game.P_ADVERB == "W?CAREFULLY")):
            game.TELL(
                "One book is out of place, however, leaving a gap in one row. On closer "
                "inspection, a small black button can be seen at the back of this gap."
            )
            game.SETG("BUTTON-REVEALED", True)
            game.FCLEAR("LIBRARY-BUTTON", "INVISIBLE")
        return True

def LIBRARY_BUTTON_F(game):
    """Library button handler"""
    if game.VERB("PUSH"):
        if game.FSET("HIDDEN-DOOR-L", "OPENBIT"):
            game.TELL(
                "The bookshelf on the left quietly swings shut."
            )
            game.FCLEAR("HIDDEN-DOOR-L", "OPENBIT")
        else:
            game.TELL(
                "The leftmost shelf quietly swings out against the balcony window."
            )
            game.FSET("HIDDEN-DOOR-L", "OPENBIT")


def CSCP(game):
    """Common china/saucer/cup/plate handler"""
    if game.VERB("TAKE", "RUB", "MOVE"):
        game.TELL(
            "These items are very rare and delicate, and were used only by Mr. "
            "Robner himself. You shouldn't even be touching them."
        )
    elif game.VERB("EXAMINE"):
        game.TELL(
            "Each one is hand-painted and depicts a scene from Greek mythology."
        )
        game.SETG("CHINA-EXAMINED", True)
    elif game.VERB("MUNG"):
        if game.PROB(75):
            game.TELL(
                "As you reach for the ", end=""
            )
            game.TELL(game.D(game.PRSO), end="")
            game.TELL(
                ", you think of the pension awaiting you "
                "upon retirement. \"Is it worth it?\" you think, to be booted off the force "
                "for an impulse of anger and stupidity. Fortunately, you calm your temper."
            )
        else:
            game.TELL(
                "With a sweep of your hand, you smash all of them! "
                "Mrs. Rourke runs into the room, screaming."
            )
            game.GONE_CRAZY()

def GONE_CRAZY(game):
    """Player has gone crazy"""
    game.TELL(
        "Your mind becomes confused amidst strange screaming, yelling, and the pangs "
        "of your conscience. \"How could I have done it?\" you ask yourself, as you "
        "hear the distant sound of police sirens. Sergeant Duffy and two other officers "
        "enter and grab you rather unceremoniously. They take you to a waiting car, "
        "where, forlorn and disgusted, you begin to ponder prison life. \"Perhaps,\" "
        "you think, \"I shouldn't have done that.\""
    )
    game.CASE_OVER()

def CUPS_F(game):
    """Cups handler"""
    if game.VERB("TAKE", "RUB", "MOVE", "EXAMINE", "MUNG"):
        game.CSCP()
    elif game.VERB("COUNT"):
        game.TELL("There are six hand-painted cups.")

def SAUCERS_F(game):
    """Saucers handler"""
    if game.VERB("TAKE", "RUB", "MOVE", "EXAMINE", "MUNG"):
        game.CSCP()
    elif game.VERB("COUNT"):
        game.TELL("There are seven hand-painted saucers.")

def CHINA_F(game):
    """China handler"""
    if game.VERB("TAKE", "RUB", "MOVE", "EXAMINE", "MUNG"):
        game.CSCP()
    elif game.VERB("COUNT"):
        game.TELL(
            "There are eight large and small plates, seven saucers, and six cups."
        )

def PLATES_F(game):
    """Plates handler"""
    if game.VERB("TAKE", "RUB", "MOVE", "EXAMINE", "MUNG"):
        game.CSCP()
    elif game.VERB("COUNT"):
        game.TELL(
            "There are eight of both the large and the small plates."
        )




def LADDER_F(game):
    """Ladder handler"""
    if game.VERB("PUT") and game.PRSI == "HOLE":
        game.TELL(
            "The ladder fits perfectly in the holes! You slowly release the "
            "ladder and it rests on the railing of the balcony above."
        )
        game.SETG("LADDER-FLAG", True)
        game.MOVE("LADDER", game.HERE)
        game.SETG("LADDER-POSITIONED", True)
        game.FSET("LADDER", "NDESCBIT")
    elif game.VERB("CLIMB-UP") and not game.GETG("LADDER-FLAG") and not game.GETG("LADDER-FLAG-2"):
        game.TELL(
            "Climbing a ladder while it is horizontal is, at best, a contradiction "
            "in terms."
        )
    elif game.VERB("LEAN") and game.PRSI in ["HOUSE", "BALCONY"]:
        if game.HERE == "IN-ROSES":
            game.SETG("LADDER-FLAG", True)
            game.SETG("LADDER-FLAG-2", False)
            game.SETG("LADDER-POSITIONED", True)
            game.MOVE("LADDER", game.HERE)
            game.TELL(
                "The ladder is now leaning against the railing of a balcony above."
            )
        elif game.HERE == "IN-ORCHARD":
            game.SETG("LADDER-FLAG", False)
            game.SETG("LADDER-FLAG-2", True)
            game.MOVE("LADDER", game.HERE)
            game.TELL(
                "The ladder, firmly planted in the soil of the orchard, is now leaning "
                "against the balcony above."
            )
        else:
            game.TELL(
                "There is no good spot to lean it against here."
            )
            return True
        game.FSET("LADDER", "NDESCBIT")
    elif game.VERB("TAKE", "MOVE"):
        game.FCLEAR("LADDER", "NDESCBIT")
        game.SETG("LADDER-FLAG", False)
        game.SETG("LADDER-FLAG-2", False)
        return False
    elif game.VERB("EXAMINE"):
        game.TELL(
            "The ladder is a typical gardening ladder, about fifteen feet long and caked "
            "with dirt and dried mud."
        )

def CUP_F(game):
    """Cup handler"""
    if game.VERB("EXAMINE", "LOOK-INSIDE"):
        game.TELL(
            "The cup is painted with a scene from Greek mythology and has a brown "
            "discoloration at the bottom."
        )
    elif game.VERB("SMELL"):
        game.TELL("The cup smells faintly of tea.")
    elif game.VERB("FINGERPRINT"):
        game.TELL(
            "There don't seem to be any fingerprints on the cup."
        )
    elif game.VERB("ANALYZE") and game.PRSO == "CUP":
        game.DO_ANALYZE()

def DO_FINGERPRINT(game, AN=False):
    """Fingerprint analysis"""
    if game.GETG("FINGERPRINT-OBJ"):
        game.TELL(
            "Sergeant Duffy is already at the lab running a previous errand. "
            "You will have to wait for him to return."
        )
        return True
    
    if not AN:
        game.TELL(
            "You look at the ", end=""
        )
        game.TELL(game.D(game.PRSO), end="")
        game.TELL(
            " closely. It appears to have good "
            "fingerprints on it, so you call for Sergeant Duffy."
        )
    
    if AN and game.PRSI:
        game.SETG("ANALYSIS-GOAL", game.PRSI)
    else:
        game.SETG("ANALYSIS-GOAL", False)
    
    game.SETG("FINGERPRINT-OBJ", game.PRSO)
    game.SETG("ANALYSIS-OBJ", AN)
    
    if game.PRSO == "LADDER":
        if game.PRESENT_TIME > 720:
            game.TELL(
                "Sergeant Duffy arrives and shakes his head sadly. \"I'm sorry, sir, but "
                "the Ladder Analysis Department closes at noon.\" He leaves."
            )
            game.SETG("FINGERPRINT-OBJ", False)
            return False
        game.SETG("LADDER-FLAG", False)
        game.SETG("LADDER-FLAG-2", False)
        game.FCLEAR("LADDER", "NDESCBIT")
    
    game.ENABLE(game.QUEUE("I-FINGERPRINT", 15 + game.RANDOM(15)))
    game.REMOVE(game.PRSO)
    game.FSET(game.PRSO, "TOUCHBIT")
    game.TELL(
        "Sergeant Duffy walks up as quietly as a mouse. He takes the ", end=""
    )
    game.TELL(game.D(game.PRSO), end="")
    game.TELL(
        " from "
        "you. \"I'll return soon with the results,\" he says, and leaves as silently as "
        "he entered."
    )

def DO_ANALYZE(game):
    """Analyze handler"""
    game.DO_FINGERPRINT(True)


def I_FINGERPRINT(game):
    """Fingerprint analysis results"""
    game.TELL("Sergeant Duffy ", end="")
    if game.GETG("FINGERPRINT-OBJ") == "LADDER":
        game.TELL(
            "comes onto the scene. ", end=""
        )
    elif game.PROB(30):
        game.TELL(
            "appears before you, holding the ", end=""
        )
        game.TELL(game.D(game.GETG("FINGERPRINT-OBJ")), end="")
        game.TELL(
            " carefully in his hands. His quiet efficiency and youthful vigor impress you "
            "quite a bit. ", end=""
        )
    elif game.PROB(50):
        game.TELL(
            "seems to arrive from nowhere, holding the ", end=""
        )
        game.TELL(game.D(game.GETG("FINGERPRINT-OBJ")), end="")
        game.TELL(
            " in his hands. ", end=""
        )
    else:
        game.TELL(
            "returns with the ", end=""
        )
        game.TELL(game.D(game.GETG("FINGERPRINT-OBJ")), end="")
        game.TELL(
            ". For a moment you muse on his almost "
            "magical entrances. ", end=""
        )
    
    if not game.GETG("ANALYSIS-OBJ"):
        game.TELL(
            "\"The fingerprints,\" he begins, "
            "\"belong to ", end=""
        )
        if game.GETG("FINGERPRINT-OBJ") == "CUP":
            game.TELL("Mr. Robner", end="")
        elif game.GETG("FINGERPRINT-OBJ") in ["SAUCER", "SUGAR-BOWL"]:
            game.TELL("Mr. Robner and Ms. Dunbar", end="")
    elif game.GETG("ANALYSIS-GOAL"):
        if (game.GETG("FINGERPRINT-OBJ") == "FRAGMENT" and 
            game.GETG("ANALYSIS-GOAL") in ["LOBLO", "LOBLO-BOTTLE", "GLOBAL-LOBLO"]):
            game.TELL(
                "\"The fragment did contain LoBlo. Here is the full report.\" "
                "He hands you a slip of paper, and departs."
            )
            game.MOVE("LAB-REPORT", "PLAYER")
            game.FSET("LAB-REPORT", "TOUCHBIT")
            game.MOVE(game.GETG("FINGERPRINT-OBJ"), "PLAYER")
            game.SETG("FINGERPRINT-OBJ", False)
            return True
        else:
            game.TELL("\"The ", end="")
            game.TELL(game.D(game.GETG("FINGERPRINT-OBJ")), end="")
            game.TELL(" analysis yielded nothing useful", end="")
    elif game.GETG("FINGERPRINT-OBJ") == "FRAGMENT":
        game.TELL(
            "\"The fragment,\" he begins, "
            "\"contains traces of tea and sugar.", end=""
        )
        game.TELL(
            " In addition, there seems to be some other chemical "
            "present that is not a common medication. It could take weeks to determine "
            "exactly what it is. It is definitely not Amitraxin (Ebullion), though. There "
            "are no clear fingerprints", end=""
        )
    elif game.GETG("FINGERPRINT-OBJ") == "CUP":
        game.TELL(
            "\"The cup,\" he begins, "
            "\"contains a trace of tea. The fingerprints are those of Mr. Robner", end=""
        )
    elif game.GETG("FINGERPRINT-OBJ") == "SAUCER":
        game.TELL(
            "\"The saucer,\" he begins, "
            "\"contains traces of tea and sugar. The fingerprints are "
            "those of Mr. Robner and Ms. Dunbar", end=""
        )
    elif game.GETG("FINGERPRINT-OBJ") == "SUGAR-BOWL":
        game.TELL(
            "\"The bowl,\" he begins, "
            "\"has the fingerprints of Mr. Robner and Ms. Dunbar. The bowl "
            "contains common table sugar only.", end=""
        )
    else:
        game.TELL(
            "\"I am sorry,\" he begins, "
            " but the lab found nothing of interest.", end=""
        )
    
    if (game.GETG("FINGERPRINT-OBJ") == "LADDER" and 
        game.GETP(game.HERE, "P?LINE") != "OUTSIDE-LINE-C"):
        game.TELL(
            " In the interests of "
            "civility, I have left the ladder outside the house.\" He leaves."
        )
        game.MOVE("LADDER", "FRONT-PATH")
    else:
        game.TELL(
            "\". "
            "With that, he leaves, handing you the ", end=""
        )
        game.TELL(game.D(game.GETG("FINGERPRINT-OBJ")), end="")
        game.TELL(" as he whisks away.")
        game.MOVE(game.GETG("FINGERPRINT-OBJ"), "PLAYER")
    
    game.SETG("FINGERPRINT-OBJ", False)
    return True

def ANALYSIS_PRINT(game, OBJ):
    """Print analysis results"""
    if OBJ in ["GLOBAL-LOBLO", "LOBLO", "LOBLO-BOTTLE"]:
        game.TELL("LoBlo", end="")
    elif OBJ in ["ASPIRIN", "ASPIRIN-BOTTLE"]:
        game.TELL("aspirin", end="")
    elif OBJ in ["EBULLION", "EBULLION-BOTTLE", "GLOBAL-EBULLION"]:
        game.TELL("Ebullion", end="")
    elif OBJ in ["DUM-KOF", "DUM-KOF-BOTTLE"]:
        game.TELL("Dum-Kof", end="")
    elif OBJ in ["ALLERGONE", "ALLERGONE-BOTTLE", "GLOBAL-ALLERGONE"]:
        game.TELL("Allergone", end="")
    else:
        game.TELL(game.D(OBJ), end="")
    game.TELL("\". ")

def SAUCER_F(game):
    """Saucer handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The saucer is hand-painted with a mythological scene. It has a couple of "
            "small areas of brown discoloration."
        )
    elif game.VERB("SMELL"):
        game.TELL("There is a faint smell of tea.")
    elif game.VERB("FINGERPRINT"):
        game.DO_FINGERPRINT()
    elif game.VERB("ANALYZE"):
        game.DO_ANALYZE()

def SHOWER_F(game):
    """Shower handler"""
    if game.VERB("TAKE", "THROUGH"):
        game.TELL(
            "Being unusually grubby, even for a police detective, this is one of your "
            "better ideas so far on this case. However, your attire isn't suitable, and "
            "you probably have better things to do."
        )

def TOILET_F(game, RARG=100):
    """Toilet handler"""
    if RARG != 100:
        return False
    elif game.VERB("EXAMINE", "LOOK-INSIDE"):
        game.TELL(
            "You have stooped to a new low, snooping around toilet bowls. Wait! Something "
            "catches your eye--was it the Tidy-Bowl man? Is he the murderer? Naw..."
        )
    elif game.VERB("FLUSH"):
        game.TELL("Whhoooossshhhhh!")

def SINK_F(game):
    """Sink handler"""
    if game.VERB("LAMP-ON"):
        game.TELL(
            "You turn the handle and lo! Water starts to run. Impressed, you turn the "
            "handle again, and the water stops running! Bravo!"
        )

def RANDOM_PSEUDO(game):
    """Random pseudo object handler"""
    game.TELL("You can't do anything with that.")

def WINDOW_F(game):
    """Window handler"""
    if game.VERB("MUNG"):
        game.TELL(
            "Vandalism is not the answer! Think of your position. How would "
            "it look for a famous police inspector to be arrested?"
        )
    elif game.VERB("BRUSH"):
        game.TELL(
            "You think you're clever, don't you? The window is so dirty that "
            "it isn't easily cleaned."
        )
    elif game.VERB("LOOK-INSIDE"):
        game.TELL(
            "The window is dirty and impossible to see through clearly."
        )


def WINDOW_KNOCK(game, RM):
    """Knock on window"""
    if game.INHABITED(RM):
        game.TELL("Someone looks up at you disgustedly.")

def KITCHEN_WINDOW_F(game):
    """Kitchen window handler"""
    if game.VERB("MUNG", "BRUSH"):
        game.WINDOW_F()
    elif game.VERB("OPEN"):
        game.TELL("The window can't be opened.")
    elif game.VERB("KNOCK"):
        if game.HERE == "KITCHEN":
            game.WINDOW_KNOCK("ORCHARD")
        else:
            game.WINDOW_KNOCK("KITCHEN")
    elif game.VERB("LOOK-INSIDE"):
        if game.HERE == "KITCHEN":
            game.TELL(
                "You can barely see through the thick leaves of the grape arbor, "
                "but a lawn and lake can be seen in the distance."
            )
        else:
            game.TELL(
                "You can see the kitchen beyond the tangle of trees and branches.", end=""
            )
            game.WINDOW_SHOP("KITCHEN", "kitchen")

def POPULATION(game, RM, PR=False):
    """Count and optionally print people in room"""
    CNT = 0
    OBJ = game.FIRST(RM)
    if not OBJ:
        return CNT
    
    while True:
        if game.FSET(OBJ, "PERSON"):
            CNT = CNT + 1
            if PR:
                game.DESCRIBE_PERSON(OBJ, "there")
        OBJ = game.NEXT(OBJ)
        if not OBJ:
            return CNT

def SHED_WINDOW_F(game):
    """Shed window handler"""
    if game.VERB("MUNG", "BRUSH"):
        game.WINDOW_F()
    elif game.VERB("OPEN"):
        game.TELL("The window can't be opened.")
    elif game.VERB("LISTEN") and game.GETG("SECRET-MEETING") > 0:
        game.TELL("You can't make out any of the words.")
    elif game.VERB("LOOK-INSIDE"):
        if game.HERE == "SHED-ROOM":
            game.TELL(
                "Although the window is grimy, you can make out the lawn outside. ", end=""
            )
            game.WINDOW_SHOP("EAST-LAWN", "east lawn")
        elif game.GETG("SECRET-MEETING") == 4:
            game.TELL(
                "Mr. Baxter seems furious and about to strike Ms. Dunbar, then calms himself. "
                "Ms. Dunbar starts to cry and is embraced by Mr. Baxter."
            )
        elif game.GETG("SECRET-MEETING") > 2:
            game.TELL(
                "Mr. Baxter and Ms. Dunbar are inside. Although you can't hear them, it's "
                "clear from their gestures that a serious argument is occurring. Dunbar appears "
                "very upset and breaks into tears. Baxter remains composed, but tense and "
                "perhaps angry -- you can't be sure."
            )
        elif game.GETG("SECRET-MEETING") > 0:
            game.TELL(
                "Through the grimy window you see Mr. Baxter and Ms. Dunbar talking. Dunbar "
                "is doing most of the talking, barely restraining tears. Baxter is listening, "
                "nodding grimly, and occassionally saying a few words. Unfortunately, you can't "
                "make any of them out."
            )
        else:
            game.TELL(
                "You can vaguely make out the inside of the shed through the grime. ", end=""
            )
            game.WINDOW_SHOP("SHED-ROOM", "shed")

def DINING_ROOM_WINDOW_F(game):
    """Dining room window handler"""
    if game.VERB("MUNG"):
        game.WINDOW_F()
    elif game.VERB("OPEN"):
        game.TELL("The window can't be opened.")
    elif game.VERB("LOOK-INSIDE"):
        if game.HERE == "ROSE-GARDEN":
            game.TELL(
                "You can see the dining room through the window.", end=""
            )
            game.WINDOW_SHOP("DINING-ROOM", "dining room")
            return True
        elif game.HERE == "IN-ROSES":
            game.TELL(
                "You can see the dining room pretty clearly through the window."
            )
            game.POPULATION("DINING-ROOM", True)
            return True
        else:
            game.TELL(
                "Through the window, the rose garden can be seen, and, off to "
                "the north, a wide lawn ending on a blue lake."
            )

def WINDOW_SHOP(game, RM, STR):
    """Look through window at room"""
    P = game.POPULATION(RM)
    if P == 0:
        game.CRLF()
        return True
    else:
        game.TELL("\nYou can vaguely see ", end="")
    
    if P == 1:
        game.TELL("someone", end="")
    else:
        game.PRINTN(P)
        game.TELL(" people", end="")
    game.TELL(" inside the " + STR + ".")

def DESCRIBE_PERSON(game, PERSON, STR=False):
    """Describe a person's location"""
    game.TELL(game.D(PERSON) + " is ", end="")
    if not STR:
        game.TELL("here", end="")
    else:
        game.TELL(STR, end="")
    game.TELL(".")

def MASTER_BEDROOM_DRESSER_F(game):
    """Master bedroom dresser handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The dresser is a beautiful piece of cabinetry."
        )
    elif game.VERB("LOOK-INSIDE", "SEARCH", "OPEN"):
        game.TELL(
            "You open all of the drawers, but find only a variety of stockings, "
            "undergarments, and handkerchiefs."
        )

def BED_F(game, RARG=100):
    """Bed handler"""
    if RARG != 100:
        return False
    elif game.VERB("LOOK-UNDER"):
        game.TELL(
            "No doubt you are looking for the bogeyman, but you are out of luck."
        )

def SUGAR_BOWL_F(game):
    """Sugar bowl handler"""
    if game.VERB("TASTE"):
        game.TELL("The powder tastes like sugar.")
    elif game.VERB("SMELL"):
        game.TELL("There is no high from sniffing this powder.")
    elif game.VERB("EAT"):
        game.TELL(
            "You eat some, but it is cloyingly sweet, so you stop."
        )
    elif game.VERB("FINGERPRINT"):
        game.DO_FINGERPRINT()
    elif game.VERB("ANALYZE"):
        game.DO_ANALYZE()

def TOOLS_F(game):
    """Tools handler"""
    if game.VERB("TAKE"):
        game.TELL(
            "The tools are standard gardening tools, in excellent condition. You have no "
            "use for them, unless you are looking for a new profession."
        )


def DUNBAR_F(game, RARG=False):
    """Dunbar character handler"""
    if RARG == "M-OBJDESC":
        if game.IS_IN_MOTION("DUNBAR"):
            return True
        elif game.IN("BAXTER", "SHED") and game.GETG("SECRET-MEETING") != 0:
            return True
        elif game.GETG("DUNBAR-BAXTER-MEET"):
            return True
        elif game.IN("DUNBAR", "DUNBAR-BATH"):
            game.TELL("Ms. Dunbar is here, brushing her hair.", end="")
        elif game.IN("DUNBAR", "DUNBAR-ROOM"):
            game.TELL("Ms. Dunbar is lying on her bed.", end="")
        elif game.IN("DUNBAR", "LIVING-ROOM"):
            if game.GETG("POST-WILL"):
                game.TELL("Ms. Dunbar is standing in the corner, looking pensive.", end="")
            else:
                game.TELL("Ms. Dunbar is sitting on the sofa here.", end="")
        else:
            game.TELL("Ms. Dunbar is here.", end="")
        game.CRLF()
        game.CARRY_CHECK("DUNBAR")
        return True
    elif game.WINNER == "DUNBAR":
        if game.VERB("FIND"):
            return False
        elif game.COM_CHECK("DUNBAR"):
            return True
        elif game.VERB("HELLO", "GOODBYE"):
            game.TELL("Ms. Dunbar nods at you.")
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
            return True
    elif game.VERB("HELLO", "ASK-ABOUT", "SHOW") and not game.GRAB_ATTENTION("DUNBAR"):
        return True
    
    if game.VERB("HELLO"):
        game.TELL("Ms. Dunbar nods at you.")
    elif game.VERB("ASK-ABOUT") and game.PRSO == "DUNBAR":
        if game.PRSI == "GLOBAL-CONCERT":
            if game.GETG("STUB-D") or game.GETG("STUB-DX"):
                game.TELL(
                    "\"It was an excellent concert, Inspector, but I don't see why you're asking "
                    "about it.\""
                )
            else:
                game.TELL(
                    "\"I don't know what you are talking about. I don't go in for concerts much, "
                    "you know.\""
                )
        elif game.PRSI == "STUB":
            if game.GETG("STUB-BX"):
                game.TELL(
                    "\"Why, it's just as Mr. Baxter said.\""
                )
            else:
                game.SETG("STUB-D", True)
                if game.IN("BAXTER", game.HERE):
                    game.SETG("STUB-DX", True)
                if game.GETG("STUB-B"):
                    game.SETG("CONTRADICTION", True)
                game.TELL(
                    "\"Oh, I...well, I guess I should tell you. You see, Mr. Baxter and I, we go "
                    "together to concerts, only occasionally, you understand. We went that night, "
                    "the night Marshall died. Then he took me home and that's it. I should have "
                    "said something before, but I just didn't think it was important, and, well, "
                    "I didn't think that the others should know we were seeing each other socially. "
                    "Our...nobody knows about it, you know. Please don't say anything!\""
                )
        elif game.PRSI in ["BAXTER", "GLOBAL-BAXTER"]:
            game.TELL(
                "\"Mr. Baxter? I see him often when he comes here on business, but I don't "
                "really know him that well. We keep to business when he comes around, and I "
                "hardly ever talk with him otherwise. He is, of course, an excellent executive, "
                "and poor Mr. Robner had every confidence in him.\""
            )
        elif game.PRSI in ["LOBLO", "GLOBAL-LOBLO", "LOBLO-BOTTLE"]:
            if game.GETG("LOBLO-FLAG"):
                game.TELL(
                    "Ms. Dunbar is taken aback. \"I...I don't really know what to say. I take the "
                    "tablets for my blood pressure. I have for a few months now. I know what you're "
                    "thinking. I can't understand. Someone must have taken my pills and poisoned Mr. "
                    "Robner. That's it. It's probably George. He knew about my pills. He's always "
                    "snooping around. He used to talk about how half the money would be his "
                    "someday.\""
                )
            else:
                game.TELL(
                    "Ms. Dunbar seems a bit surprised. \"You found those in my bathroom, didn't "
                    "you? I've been taking them for months for my blood pressure. Are they "
                    "important?\" she asks."
                )
        elif game.PRSI in ["GEORGE", "GLOBAL-GEORGE"]:
            game.DISCRETION("DUNBAR", "GEORGE")
            game.TELL(
                "\"Nobody likes George much. He's always alone when he's here, and that's only "
                "when he can't get more money to waste. I think he's just been waiting for the "
                "day when his father's money would be his. I can't say I miss him when he's not "
                "here: A thoroughly obnoxious child.\""
            )
        elif game.PRSI in ["MRS-ROBNER", "GLOBAL-MRS-ROBNER"]:
            game.TELL(
                "\"She's a lovely person. She and Marshall were always an odd couple: he was "
                "so quiet and reserved, and she's so lively and sociable. She's changed a lot "
                "over the last few years. She used to enjoy her life here, but lately she's "
                "been restless and irritable, and now with Marshall's death, I'm worried about "
                "what may become of her.\""
            )
        elif game.PRSI in ["ROURKE", "GLOBAL-ROURKE"]:
            game.TELL(
                "\"Mrs. Rourke is a very good servant. Always helpful, and always "
                "nearby when needed.\""
            )
        elif game.PRSI in ["GARDENER", "GLOBAL-GARDENER"]:
            game.TELL(
                "\"He seems nice, if you can talk to him. You usually can't, really.\" She "
                "laughs briefly. \"Don't ever disturb his roses, or you'll learn the meaning "
                "of temper.\" She giggles again."
            )
        elif game.PRSI == "GLOBAL-OLD-WILL":
            game.TELL(
                "\"I really don't know too much about Marshall's personal business.\""
            )
        elif game.PRSI == "GLOBAL-NEW-WILL":
            if game.GETG("WILL-TIME") > 0:
                game.TELL(
                    "\"I don't know anything about it. I suppose Marshall could have written a new "
                    "will, but I probably would have seen signs of it around the library.\""
                )
            else:
                game.TELL(
                    "\"As far as I know, there was no new will written, although Marshall did "
                    "threaten to disinherit George. I guess he could have written one without my "
                    "knowledge. I'm not always with him, you know.\""
                )
        elif game.PRSI == "NEW-WILL":
            game.TELL(
                "Ms. Dunbar reads the will carefully, nodding slowly. \"I guess I'm not "
                "surprised that Marshall disinherited George. He's been asking for it.\""
            )
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "Ms. Dunbar looks down at the ground and sniffles softly. \"I've known him "
                "for years. He's been tremendously nervous and depressed lately about business. "
                "I don't think all was well in his personal life either. George has always been "
                "a problem for him. He even mentioned suicide once, although I never took it "
                "seriously. It shows you can never tell.\" She wipes her eyes with her "
                "hands."
            )
        elif game.PRSI == "GLOBAL-FOCUS":
            game.TELL(
                "\"Focus? There was once a subsidiary of Robner Corp. with that name. I can't "
                "recall much about it, though.\""
            )
        elif game.PRSI == "GLOBAL-SAFE":
            game.TELL(
                "\"A safe? I don't think there's one in the house, although there's one at "
                "the office.\""
            )
        else:
            game.TELL(
                "\"I'm sorry, but I can't help you with that.\""
            )
    elif game.VERB("SHOW", "CONFRONT"):
        if game.PRSI == "STUB":
            game.PERFORM("V?ASK-ABOUT", "DUNBAR", "STUB")
            return True
        elif game.PRSI == "LOBLO":
            game.TELL(
                "She glances at the pills. \"They're my pills. You must have taken them from "
                "my bathroom. Well, what am I supposed to say?\" She looks away."
            )
        elif game.PRSI == "LAB-REPORT":
            game.TELL(
                "She seems stunned but recovers quickly. \"He didn't commit suicide, then?\" "
                "she says. \"But LoBlo, that's a pill I take for my blood pressure.\" She "
                "pauses. \"I can tell what you're thinking, but I didn't, couldn't have done "
                "it. Why should I? Someone must have taken them, maybe George. He knew I used "
                "them.\""
            )
            game.ENABLE(game.QUEUE("I-DUNBAR-ACTIVATE", 5 + game.RANDOM(15)))
            game.SETG("LOBLO-FLAG", True)
    elif game.VERB("ACCUSE"):
        if game.GETG("LOBLO-FLAG"):
            game.TELL(
                "\"No! I didn't do it! I've worked for Mr. Robner for years. What possible "
                "motive could I have?\" With that, Ms. Dunbar begins to cry and move about "
                "the room quite nervously."
            )
            game.DUNBAR_SEQUENCE()
        else:
            game.TELL(
                "\"What?\" she cries. \"Murder?\" She regains her composure and asks, \"I "
                "thought he committed suicide, with his medicine.\""
            )
    elif game.VERB("ARREST"):
        if not game.FSET("LAB-REPORT", "TOUCHBIT"):
            game.MURDER_NOT_PROVEN("DUNBAR")
            return True
        game.TELL(
            "Sergeant Duffy enters the room solemnly. He places handcuffs on Ms. Dunbar "
            "and leads her off. She is sobbing hysterically.\n\n"
        )
        game.END_HEADER("August 10")
        if game.GETG("MEETING-INTERRUPTED"):
            game.TELL(
                "What a tragedy! Ms. Dunbar, released on bail during her trial for the murder "
                "of Mr. Robner, was found dead this morning, the victim of an apparent suicide. "
                "Her death is all the more distressing as the district attorney was trying to "
                "arrange some plea-bargaining deal with her in exchange for information "
                "implicating an unnamed accomplice. I am sorry to be the one to let you know. "
                "Thanks for your hard work on the Robner case.\n\n"
            )
        else:
            game.TELL(
                "I wanted to let you know the disposition of the Robner case. Ms. Dunbar was "
                "acquitted today, the jury citing a lack of motive and only circumstantial "
                "evidence. I am extremely sorry.\n\n"
            )
        game.CASE_OVER()


def I_DUNBAR_ACTIVATE(game):
    """Dunbar activation routine"""
    if not game.GETG("DUNBAR-ACCUSED"):
        game.DUNBAR_SEQUENCE()
        return False


def ROURKE_F(game, RARG=False):
    """Rourke character handler"""
    if RARG == "M-OBJDESC":
        if game.IS_IN_MOTION("ROURKE"):
            return True
        elif game.IN("ROURKE", "KITCHEN"):
            game.TELL(
                "Mrs. Rourke is here, cleaning the kitchen."
            )
        elif game.IN("ROURKE", "DINING-ROOM"):
            game.TELL("Mrs. Rourke is cleaning the table here.")
        elif game.IN("ROURKE", "LIVING-ROOM"):
            game.TELL("Mrs. Rourke is dusting the room.")
        elif game.IN("ROURKE", "ROURKE-ROOM"):
            game.TELL("Mrs. Rourke is resting here.")
        else:
            game.TELL("Mrs. Rourke is here, tidying up.")
        game.CARRY_CHECK("ROURKE")
        return True
    elif game.WINNER == "ROURKE":
        if game.VERB("FIND"):
            return False
        elif game.COM_CHECK("ROURKE"):
            return True
        elif game.VERB("HELLO", "GOODBYE"):
            game.TELL("Mrs. Rourke looks up from her work and nods.")
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
            return True
    elif game.VERB("HELLO", "ASK-ABOUT", "SHOW") and not game.GRAB_ATTENTION("ROURKE"):
        return True
    
    if game.VERB("HELLO", "GOODBYE"):
        game.TELL("Mrs. Rourke looks up from her work and nods.")
    elif game.VERB("ASK-ABOUT") and game.PRSO == "ROURKE":
        if game.PRSI == "ENVELOPE" and game.IN("ENVELOPE", "ROURKE"):
            game.TELL(
                "\"It's a letter just arrived for Mrs. Robner. I was going to bring "
                "it to her.\""
            )
        elif game.PRSI in ["BAXTER", "GLOBAL-BAXTER"]:
            game.DISCRETION("ROURKE", "BAXTER")
            game.TELL(
                "\"Baxter! Hmmmph. Stuffiest person I ever met! I don't mind telling you I've "
                "never liked him much. So serious, businesslike. Thinks he's hot stuff, I "
                "imagine. I really shouldn't be telling you this, though, I suppose. "
                "\"Rourke,\" they tell me, \"stop your gossiping.\" Not that I'm a gossip, "
                "mind you, but I do have my opinions.\""
            )
        elif game.PRSI in ["GEORGE", "GLOBAL-GEORGE"]:
            game.DISCRETION("ROURKE", "GEORGE")
            game.TELL(
                "\"George is something, I tell you. The black sheep of the family, is what I'd "
                "say. Never met nobody with less respect for money. You'd think it grew on "
                "trees; not that it don't around here. Well, there I go, shooting off my mouth "
                "again.\""
            )
        elif game.PRSI in ["CORPSE", "DUNBAR", "GLOBAL-DUNBAR"]:
            game.TELL(
                "\"Ms. Dunbar is nice; the best of the lot, I think. She's always been real "
                "friendly to me, and helps out when I have a problem. Mr. Robner, he really "
                "liked her too. I don't think Mrs. Robner did, though. He's been so busy lately "
                "with the business and Ms. Dunbar that I don't think the Mrs. hardly saw him "
                "much. Kind of jealous, maybe, of the two of them, I mean.\""
            )
        elif game.PRSI in ["MRS-ROBNER", "GLOBAL-MRS-ROBNER"]:
            game.DISCRETION("ROURKE", "MRS-ROBNER")
            game.TELL(
                "\"Now she's a strange sort. Real lively when she moved here, but I don't "
                "think she ever liked the life here. Her people are from Boston, one of those "
                "old families, and she never got used to Mr. Robner's ways. She goes out a lot, "
                "and sometimes she doesn't even come back at night. Not that I'm spying on her. "
                "But I know about these things. She has callers here, a number of men. One in "
                "particular comes more than others. A widower, I think, a real live wire. Not "
                "what it's any of my business, but I think someone with a sharp tongue could do "
                "her a lot of damage if she doesn't watch herself.\""
            )
        elif game.PRSI == "GLOBAL-STEVEN":
            game.DISCRETION("ROURKE", "MRS-ROBNER")
            game.TELL(
                "\"Ah, that's it! He's the one who's been coming around, taking Mrs. Robner "
                "out. I don't like the look of it. I mean, I think it looks kind of funny, what "
                "with she's a married woman. Mr. Robner takes no notice, of course, always "
                "busy. Oh, well. I shouldn't be telling you this. Now that Mr. Robner's dead, "
                "I don't suppose it matters, but what do you think people were saying! I tell "
                "you, gossip is fierce around here!\""
            )
        elif game.PRSI in ["GARDENER", "GLOBAL-GARDENER"]:
            game.TELL(
                "\"Oh, don't let him frighten you. Let him alone and don't bother his roses. "
                "Gets positively livid about that. Got the green thumb, that's for sure.\""
            )
        elif game.PRSI == "GLOBAL-MR-ROBNER":
            game.TELL(
                "\"A fine man, but his head was always in the clouds. Just the opposite of "
                "Mrs. Robner. Her feet were always on the ground. He's been so worried, it "
                "makes me sick. I don't understand these business things, but he said something "
                "about them taking his business away from him just two nights ago. I guess the "
                "pressure was too much. He was a fine man, full of good works, though charity "
                "does begin at home, as the saying goes. Not that I have anything to complain "
                "about. He always treated me right.\""
            )
        else:
            game.TELL(
                "\"I don't know nothing about no ", end=""
            )
            game.TELL(game.D(game.PRSI), end="")
            game.TELL("\".")
    elif game.VERB("SHOW", "CONFRONT"):
        if game.PRSI == "LAB-REPORT":
            game.TELL(
                "\"Well, if that don't beat all! A murder here, right under my nose! You've "
                "got your work cut out for you, Inspector, all right. There's some pretty "
                "strange people around here, and I wouldn't put it past hardly any of 'em to "
                "do it. What do you know!\""
            )
        else:
            game.TELL("Mrs. Rourke seems uninterested in it.")

def DISCRETION(game, P1, P2):
    """Check for discretion when talking about someone"""
    if game.IN(P2, game.HERE):
        game.TELL(game.D(P1) + " looks briefly toward " + game.D(P2) + " and then speaks "
                  "in a low whisper.")

def CARRY_CHECK(game, PERSON):
    """Check what a person is carrying"""
    if game.FIRST(PERSON):
        game.PRINT_CONT(PERSON, True, 0)
    return True

def DUM_KOF_F(game):
    """Dum-Kof cough syrup handler"""
    if game.VERB("DRINK"):
        game.TELL(
            "You drink the remaining cough syrup. Yuk! That was awful!"
        )
        game.REMOVE("DUM-KOF")
    elif game.VERB("TASTE"):
        game.TELL(
            "Yuk! It tastes like cough medicine!"
        )

def LOBLO_F(game):
    """LoBlo pills handler"""
    if game.VERB("TASTE"):
        game.TELL("The pills are virtually tasteless.")
    elif game.VERB("SMELL"):
        game.TELL("The pills are odorless.")
    elif game.VERB("EAT"):
        game.TELL(
            "Nervous? Blood Pressure high? See a doctor."
        )
    elif game.VERB("EXAMINE"):
        game.TELL("These are small, yellow pills.")

def SNEEZO_F(game):
    """Sneezo pills handler"""
    if game.VERB("TASTE"):
        game.TELL("The pills are virtually tasteless.")
    elif game.VERB("SMELL"):
        game.TELL("The pills are odorless.")
    elif game.VERB("EAT"):
        game.TELL("You must realize that you aren't sick.")
    elif game.VERB("EXAMINE"):
        game.TELL("These are small, white pills.")

def MEDICINE_BOTTLE_F(game):
    """Medicine bottle handler"""
    if game.VERB("COUNT"):
        game.TELL("It's hard to tell with the bottle closed.")

def ALLERGONE_F(game):
    """Allergone pills handler"""
    if game.VERB("TASTE"):
        game.TELL("The pills are bitter on the tongue.")
    elif game.VERB("SMELL"):
        game.TELL("The pills are odorless.")
    elif game.VERB("EAT"):
        game.TELL("The only allergy you seem to have is to work.")
    elif game.VERB("EXAMINE"):
        game.TELL("These are tiny red pills.")

def EBULLION_F(game):
    """Ebullion pills handler"""
    if game.VERB("TASTE"):
        game.TELL("The pills are quite bitter.")
    elif game.VERB("SMELL"):
        game.TELL("The pills have a faint pungent aroma.")
    elif game.VERB("EAT"):
        game.TELL(
            "Are you depressed? Given your performance on this case, that isn't "
            "surprising. In any event, you shouldn't take other people's medicine!"
        )
    elif game.VERB("EXAMINE"):
        game.TELL("These are little white pills.")


## This is the sequence which starts with accusing Dunbar of murder after having gotten the 'goods' on her, i.e. showing
## her the report about the pills.  
## Basically, she runs around looking for Baxter and talks to him briefly.  They agree to meet in the shed at a later time.  There,
## they have a long and heated argument, which can be watched from the outside."



def DUNBAR_SEQUENCE(game):
    """Start Dunbar accusation sequence"""
    BL = game.LOC("BAXTER")
    if game.GETG("DUNBAR-ACCUSED"):
        return False
    if not game.IN("DUNBAR", BL):
        game.ESTABLISH_GOAL("DUNBAR", BL, True)
    game.SETG("DUNBAR-ACCUSED", True)
    game.SETG("D-S-BAXTER-LOC", BL)
    game.ENABLE(game.QUEUE("I-DUNBAR-SEQ", -1))

def I_DUNBAR_SEQ(game):
    """Dunbar sequence interrupt"""
    BL = game.LOC("BAXTER")
    if BL != game.GETG("D-S-BAXTER-LOC"):
        game.DUNBAR_SEQUENCE()
        return False
    elif game.LOC("DUNBAR") == BL:
        game.PUT(game.GET(game.GOAL_TABLES, "BAXTER-C"), "GOAL-ENABLE", False)
        if game.HERE == BL:
            game.TELL(
                "Ms. Dunbar glances at Baxter and then at you."
            )
        else:
            game.SETG("DUNBAR-BAXTER-MEET", True)
            game.PUT(game.GET(game.GOAL_TABLES, "BAXTER-C"), "GOAL-ENABLE", True)
            game.QUEUE("I-DUNBAR-SEQ", 0)
            game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-2", 5))
            return False

def I_DUNBAR_SEQ_2(game):
    """Dunbar sequence part 2"""
    game.SETG("DUNBAR-BAXTER-MEET", False)
    game.ESTABLISH_GOAL("DUNBAR", "SHED-ROOM", True)
    game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-D", -1))
    game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-3", 10))
    return False

def I_DUNBAR_SEQ_3(game):
    """Dunbar sequence part 3"""
    game.ESTABLISH_GOAL("BAXTER", "NORTH-LAWN", True)
    game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-B", -1))
    return False

def I_DUNBAR_SEQ_D(game):
    """Dunbar sequence - Dunbar's movements"""
    GT = game.GET(game.GOAL_TABLES, "DUNBAR-C")
    if game.LOC("DUNBAR") == "SHED-ROOM":
        if game.LOC("BAXTER") == "SHED-ROOM":
            game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-4", -1))
            game.QUEUE("I-DUNBAR-SEQ-D", 0)
        elif game.HERE == "SHED-ROOM":
            if game.PROB(50):
                game.TELL(
                    "Dunbar paces around the shed nervously. If she was looking for something, "
                    "she would have found it by now."
                )
            else:
                game.TELL(
                    "Ms. Dunbar seems to be looking around for something."
                )
            return True
        return False
    elif (game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C" and 
          game.FOLLOWED("DUNBAR")):
        if game.GET(GT, "GOAL-ENABLE"):
            game.PUT(GT, "GOAL-ENABLE", False)
        elif game.PROB(28):
            game.TELL(
                "Ms. Dunbar eyes you nervously."
            )
            return True
        elif game.PROB(50):
            game.TELL(
                "Ms. Dunbar stares off toward the south."
            )
            return True
        else:
            game.TELL(
                "Ms. Dunbar seems to be deep in thought."
            )
            return True
        if (not game.GETG("STUB-DROPPED") and 
            game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C"):
            game.TELL(
                "Ms. Dunbar spots you and stops. She reaches into her pocket and pulls out a "
                "cigarette. As she does so, what appears to be a ticket stub falls out of her "
                "pocket and floats to the ground. She checks her pocket again, apparently for "
                "a match, but finds none and puts the cigarette back in her pocket."
            )
            game.MOVE("STUB", game.LOC("DUNBAR"))
            game.SETG("STUB-DROPPED", True)
        elif game.PROB(15):
            game.TELL(
                "Ms. Dunbar glances around as she walks. She takes a quick glance in your "
                "direction, but it doesn't seem like she noticed you."
            )
            game.PUT(GT, "GOAL-ENABLE", True)
        elif game.PROB(50):
            game.TELL(
                "Ms. Dunbar looks around as she walks and does a brief double-take "
                "when she looks in your direction. She slows down and stops."
            )
        else:
            game.TELL(
                "Ms. Dunbar, who has been looking from side to side as she goes, "
                "comes to a stop. She spins around, looking in all directions."
            )
    else:
        game.PUT(GT, "GOAL-ENABLE", True)
        return False

def I_DUNBAR_SEQ_B(game):
    """Dunbar sequence - Baxter's movements"""
    if (game.LOC("BAXTER") == "NORTH-LAWN" or 
        game.GETP(game.HERE, "P?LINE") == "TOP-OF-THE-LINE-C"):
        game.QUEUE("I-DUNBAR-SEQ-B", 0)
        game.ESTABLISH_GOAL("BAXTER", "SHED-ROOM", True)
        game.ENABLE(game.QUEUE("I-DUNBAR-SEQ-B-2", -1))
    return False

def I_DUNBAR_SEQ_B_2(game):
    """Dunbar sequence - Baxter's movements part 2"""
    GT = game.GET(game.GOAL_TABLES, "BAXTER-C")
    
    if game.LOC("BAXTER") == "SHED-ROOM":
        game.QUEUE("I-DUNBAR-SEQ-B-2", 0)
        return False  # <RFALSE>
    elif game.FOLLOWED("BAXTER"):
        # First nested COND
        if game.GET(GT, "GOAL-ENABLE"):
            game.PUT(GT, "GOAL-ENABLE", False)
            # No return - continues to second COND
        elif game.PROB(50):
            game.TELL("Baxter draws a deep breath and looks about contentedly.")
            return True  # <RTRUE>
        else:
            game.TELL("Baxter stares out over the lake.")
            return True  # <RTRUE>
        
        # Second nested COND - only reached if first branch of first COND was taken
        if game.PROB(50):
            game.TELL(
                "Baxter walks slowly, but with determination. He looks around often, as "
                "if he were a prospective buyer of the property. He stops now, staring "
                "up at the sky."
            )
        else:
            game.TELL("Baxter stops, bends down, and ties his shoe.", end="")
            if game.PROB(30):
                game.TELL("  As he finishes, he takes stands up, and stares at some distant trees.")
            else:
                game.TELL(" He stands up and stares off to the south.")
    else:  # T clause
        game.PUT(GT, "GOAL-ENABLE", True)
        return False  # <RFALSE>


def I_DUNBAR_SEQ_4(game):
    """Dunbar sequence - final confrontation"""
    if game.HERE == "SHED-ROOM":
        if game.GETG("SECRET-MEETING") < 2 or game.GETG("SECRET-MEETING") > 5:
            game.TELL(
                "You seem to have walked in on some sort of get-together, although from the "
                "look on Ms. Dunbar's face, you are not the guest of honor. She is aghast, and "
                "she continually looks back and forth between Mr. Baxter and yourself."
            )
        else:
            game.TELL(
                "As you enter the shed, Mr. Baxter and Ms. Dunbar, who were in the midst of a "
                "quiet but heated argument, stop at once. Ms. Dunbar is quite upset and "
                "clutches Mr. Baxter. Baxter, who has retained his composure throughout, "
                "attempts to comfort Dunbar. She pushes him away and runs out of the shed."
            )
            game.MOVE("DUNBAR", "EAST-LAWN")
            game.PUT(game.GET(game.WHERE_TABLES, "DUNBAR-C"), 0, game.PRESENT_TIME)
            game.PUT(game.GET(game.WHERE_TABLES, 0), "DUNBAR-C", game.PRESENT_TIME)
        game.HEAD_FOR_CLIMAX()
        return True
    elif game.LOC("BAXTER") == "SHED-ROOM":
        game.SETG("SECRET-MEETING", game.GETG("SECRET-MEETING") + 1)
        if game.GETG("SECRET-MEETING") > 5:
            game.HEAD_FOR_CLIMAX()
        return False

def FOLLOWED(game, PERSON):
    """Check if person is being followed"""
    L = game.LOC(PERSON)
    if L == game.HERE:
        return True
    elif game.HERE == "GUEST-ROOM":
        return False
    elif game.BAND(game.GETP(L, "P?CORRIDOR"), 
                    game.GETP(game.HERE, "P?CORRIDOR")) != 0:
        return True
    else:
        return False


## Ok, folks.  We have just caused Dunbar to run into the house toward her room.  It occurs to Baxter that she may well talk.  He
## then plans to kill her using a similar plan to his original one, this time entering the house through the master bedroom.  He
## shoots Dunbar at close range, leaves a forged suicide note, and runs outside.  He then runs to the house, 'having heard the shot'.


def HEAD_FOR_CLIMAX(game):
    """Head for climax of the story"""
    if game.HERE in ["EAST-LAWN", "EAST-SIDE", "EAST-OF-DOOR"]:
        game.TELL(
            "Baxter and Dunbar both leave the shed, heading off in "
            "different directions."
        )
    elif game.HERE == "BEHIND-SHED":
        game.TELL(
            "The voices stop and you hear sets of footsteps leaving the shed."
        )
    game.ESTABLISH_GOAL("DUNBAR", "DUNBAR-ROOM", True)
    game.ESTABLISH_GOAL("BAXTER", "NORTH-LAWN", True)
    game.ENABLE(game.QUEUE("I-BAXTER-SEQ", -1))
    game.QUEUE("I-DUNBAR-SEQ-4", 0)
    game.SETG("MEETING-INTERRUPTED", game.GETG("SECRET-MEETING"))
    game.SETG("SECRET-MEETING", 0)

def I_BAXTER_SEQ(game):
    """Baxter sequence"""
    if game.GETG("BAXTER-SEQ-LOC") == "MASTER-BEDROOM":
        if (game.BAND(game.GETP(game.HERE, "P?CORRIDOR"), 1) != 1 and
            game.HERE not in ["STAIRS", "STAIR-BOTTOM", "DUNBAR-ROOM"]):
            game.SETG("BAXTER-SEQ-LOC", "BEDROOM-BALCONY")
            game.MOVE("BAXTER", "BEDROOM-BALCONY")
            game.REMOVE("DUNBAR")
            game.SETG("DUNBAR-DEAD", True)
            game.DISABLE(game.INT("I-DUNBAR"))
            game.MOVE("PISTOL", "DUNBAR-ROOM")
            game.MOVE("SUICIDE-NOTE", "DUNBAR-ROOM")
            game.MOVE("CORPSE", "DUNBAR-ROOM")
            game.QUEUE("I-BAXTER-SEQ", 0)
            game.ENABLE(game.QUEUE("I-BAXTER-ESCAPE", -1))
            if game.GETP(game.HERE, "P?LINE") == "TOP-OF-THE-LINE-C":
                game.SETG("SHOT-FIRED", True)
                game.TELL(
                    "You hear a pistol shot close by."
                )
            elif game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C":
                game.TELL(
                    "You hear what sounds like a pistol shot from inside the house."
                )
            else:
                game.TELL(
                    "From upstairs, you hear a single explosion like a pistol shot."
                )
            game.SHOT_FIRED_F()
            return True
    elif game.GETG("BAXTER-SEQ-LOC") == "BEDROOM-BALCONY":
        if (game.HERE != "MASTER-BEDROOM" and
            game.LOC("MRS-ROBNER") != "MASTER-BEDROOM"):
            game.MOVE("BAXTER", "MASTER-BEDROOM")
            game.SETG("BAXTER-SEQ-LOC", "MASTER-BEDROOM")
        return False
    elif game.GETG("BAXTER-SEQ-LOC") == "NORTH-LAWN":
        if (game.IN("DUNBAR", "DUNBAR-ROOM") and
            game.GETP(game.HERE, "P?LINE") != "OUTSIDE-LINE-C" and
            game.HERE != "BEDROOM-BALCONY"):
            game.SETG("LADDER-FLAG-2", True)
            game.SETG("LADDER-FLAG", False)
            game.MOVE("LADDER", "ORCHARD")
            game.FCLEAR("LADDER", "NDESCBIT")
            game.FSET("LADDER", "TOUCHBIT")
            game.MOVE("BAXTER", "BEDROOM-BALCONY")
            game.SETG("BAXTER-SEQ-LOC", "BEDROOM-BALCONY")
        return False
    elif game.IN("BAXTER", "NORTH-LAWN"):
        game.SETG("BAXTER-SEQ-LOC", "NORTH-LAWN")
        return False

def I_BAXTER_ESCAPE(game):
    """Baxter escape sequence"""
    FLG = False
    if game.GETG("SHOT-FIRED"):
        game.SETG("SHOT-FIRED", False)
        if game.HERE in ["CORRIDOR-4", "CORRIDOR-3"]:
            game.TELL(
                "As you enter the hallway, you catch a glimpse of someone running across the "
                "eastern end of the hallway from south to north."
            )
            FLG = True
        elif game.HERE == "MASTER-BEDROOM":
            game.TELL(
                "As you walk into the bedroom, you see Baxter running past you to the balcony. "
                "He doesn't seem to have noticed you."
            )
            FLG = True
            game.SETG("BAXTER-SEEN", True)
        elif game.BAND(game.GETP(game.HERE, "P?CORRIDOR"), 1) == 1:
            game.TELL(
                "As you enter the hallway, you see Baxter running from Dunbar's "
                "room across the hall to the master bedroom."
            )
            FLG = True
            game.SETG("BAXTER-SEEN", True)
    game.SETG("BAXTER-SEQ-LOC", "BEDROOM-BALCONY")
    if game.HERE in ["ORCHARD", "EAST-LAWN", "NORTH-LAWN"]:
        return FLG
    else:
        game.MOVE("BAXTER", "IN-ORCHARD")
        game.SETG("LADDER-FLAG-2", False)
        game.ESTABLISH_GOAL("BAXTER", "DUNBAR-ROOM", True)
        game.QUEUE("I-BAXTER-ESCAPE", 0)
        game.SETG("BAXTER-SEQ-LOC", False)
        return FLG

def I_BAXTER_END_1(game):
    """Baxter end sequence"""
    game.UNPRIORITIZE("BAXTER")
    return False

def SHOT_FIRED_F(game):
    """Handle shot being fired"""
    game.ESTABLISH_GOAL("MRS-ROBNER", "DUNBAR-ROOM", True)
    game.ESTABLISH_GOAL("ROURKE", "CORRIDOR-1", True)
    game.ESTABLISH_GOAL("GEORGE", "DUNBAR-ROOM", True)
    game.ENABLE(game.QUEUE("I-SHOT", -1))

def I_SHOT(game):
    """Handle reactions to shot"""
    FLG = False
    if game.IN("MRS-ROBNER", "DUNBAR-ROOM"):
        if game.HERE == "DUNBAR-ROOM":
            game.TELL(
                "Mrs. Robner, standing quietly by the body, starts sobbing and "
                "leaves the room."
            )
        game.UNPRIORITIZE("MRS-ROBNER")
        game.MOVE("MRS-ROBNER", "CORRIDOR-1")
        FLG = True
    elif game.IN("GEORGE", "DUNBAR-ROOM"):
        if game.HERE == "DUNBAR-ROOM":
            game.TELL(
                "George says something like \"My God\" under his breath."
            )
        game.UNPRIORITIZE("GEORGE")
    elif game.IN("ROURKE", "CORRIDOR-1"):
        if game.HERE == "CORRIDOR-1":
            game.TELL(
                "Mrs. Rourke peeks in the door and looks sick. \"I'm leaving this "
                "house,\" she says, and pops out again."
            )
        game.MOVE("ROURKE", "STAIR-TOP")
        game.ESTABLISH_GOAL("ROURKE", "ROURKE-ROOM", True)
        FLG = True
    game.SETG("SHOT-COUNT", game.GETG("SHOT-COUNT") + 1)
    if game.GETG("SHOT-COUNT") > 20:
        game.QUEUE("I-SHOT", 0)
    return FLG

def PISTOL_F(game):
    """Pistol handler"""
    if game.VERB("EXAMINE"):
        if game.FSET("PISTOL", "TOUCHBIT"):
            game.TELL(
                "The pistol is bloody and has clearly been used recently."
            )
        else:
            game.TELL(
                "The pistol has bloodstains on it. It has recently been fired."
            )

def CORPSE_F(game):
    """Corpse handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The corpse is most gruesome. Ms. Dunbar was apparently shot in the "
            "head at close range, leaving a most distasteful mess."
        )
    elif game.VERB("RUB"):
        game.TELL(
            "The body is still quite warm.", end=""
        )

def GLOBAL_PEN_F(game):
    """Global pen handler"""
    if game.VERB("FIND"):
        if game.HERE == "DUNBAR-ROOM":
            game.TELL(
                "It doesn't seem to be around here."
            )
        else:
            game.TELL(
                "There isn't one here."
            )
    elif game.VERB("ASK-FOR", "ASK-ABOUT"):
        return False
    else:
        game.TELL("There is no pen to be seen here.")

def PEN_F(game):
    """Pen handler"""
    if game.VERB("WRITE"):
        game.TELL(
            "The pen makes a mark in a fine blue line."
        )

def I_SHOW_HOLE(game):
    """Show hole interrupt"""
    game.SETG("SHOW-WAIT", game.GETG("SHOW-WAIT") + 1)
    if game.GETG("SHOW-WAIT") > 4:
        game.SETG("NO-SHOW", True)
        game.QUEUE("I-SHOW-HOLE", 0)
        return False
    elif game.HERE == "IN-ROSES":
        if game.GETG("SHOW-WAIT") != 1:
            game.TELL(
                "McNabb gives you a sideways glance. \"What kept you?\" he asks."
            )
        game.SHOW_HOLE()
        game.QUEUE("I-SHOW-HOLE", 0)

def TODAY_F(game):
    """Today handler"""
    if game.VERB("WHAT"):
        game.TELL("Today is Friday, July 10.")

def GLOBAL_WARRANT_F(game):
    """Global warrant handler"""
    if game.VERB("TAKE", "FIND"):
        game.TELL(
            "Knowing the courts, it would take weeks to get one."
        )

def CORRIDOR_WINDOW_F(game):
    """Corridor window handler"""
    if game.VERB("LOOK-INSIDE"):
        game.TELL("You can see the west lawn through the window.")

def I_BAXTER_ARRIVE(game):
    """Baxter arrival"""
    game.MOVE("BAXTER", "SOUTH-LAWN")
    if game.HERE == "SOUTH-LAWN":
        game.TELL(
            "A limosine pulls up the drive. Mr. Baxter exits and the limo pulls away. "
            "Baxter takes a deep breath and looks around."
        )
    elif game.HERE in ["FRONT-PATH", "EAST-LAWN", "WEST-LAWN", "EAST-OF-DOOR", "WEST-OF-DOOR"]:
        game.TELL(
            "A car pulls up the drive to the south, and Mr. Baxter steps out onto "
            "the lawn."
        )

def I_COATES_ARRIVE(game):
    """Coates arrival"""
    game.MOVE("COATES", "SOUTH-LAWN")
    game.ESTABLISH_GOAL("COATES", "LIVING-ROOM", True)
    if game.HERE == "SOUTH-LAWN":
        game.TELL(
            "A large automobile pulls up the drive. Mr. Coates, the lawyer, steps out of "
            "the car. \"Oh, hello! You must be the Inspector. I'll be reading the will at "
            "noon, you know. Don't be late!\" he says."
        )
    elif game.HERE in ["FRONT-PATH", "EAST-LAWN", "WEST-LAWN", "EAST-OF-DOOR", "WEST-OF-DOOR"]:
        game.TELL(
            "A car pulls up the drive to the south, and Mr. Coates steps out onto "
            "the lawn."
        )

def TRASH_F(game):
    """Trash handler"""
    if game.VERB("TAKE", "READ", "EXAMINE"):
        game.FSET("TRASH", "TOUCHBIT")
        game.FSET("TRASH-BASKET", "TOUCHBIT")
        return False
    


def GLOBAL_DUFFY_F(game):
    """Global Duffy handler"""
    if game.VERB("FIND"):
        game.TELL(
            "Like a lurking grue in the dark places of the earth, Sergeant Duffy is always "
            "near the scene of a crime. If you want something analyzed, he will arrive in "
            "an instant to take the evidence to the lab. When the results are available, "
            "he rushes them back to you. If you wish to arrest someone, Duffy will be there "
            "with the handcuffs. A more dedicated civil servant cannot be found."
        )

def L_RAILING_F(game):
    """Library railing handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The railing is made of a sturdy metal and helps prevent nasty falls. There is "
            "a small area of paint scraped off the outside edge."
        )

def B_RAILING_F(game):
    """Bedroom railing handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "This sturdy railing protects people on the balcony from being impaled upon "
            "the exotic plants below. The railing itself is uniformly painted."
        )

def L_BALCONY_F(game):
    """Library balcony handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The balcony itself is made of wood, except the railing which is metal. The "
            "balcony is in good repair, but a few spots of dried mud soil the floor."
        )

def B_BALCONY_F(game):
    """Bedroom balcony handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The balcony is wooden, excepting the metal railing surrounding it. "
            "It is in good repair and is quite clean."
        )

def GLOBAL_ROOM_F(game):
    """Global room handler"""
    TIM = 0
    if game.VERB("THROUGH"):
        game.V_WALK_AROUND()
    elif game.VERB("KNOCK"):
        if game.HERE == "UPSTAIRS-CLOSET":
            game.TELL(
                "The wall to the north here sounds unusually hollow."
            )
        elif game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C":
            game.TELL("You're acting very strangely!")
        else:
            game.TELL(
                "Knocking on the walls reveals nothing unusual."
            )
    elif game.VERB("LOOK-INSIDE") and game.HERE == "CORRIDOR-2":
        game.TELL("From here, it looks quite ordinary.")
    elif game.VERB("SEARCH", "EXAMINE"):
        if game.GETP(game.HERE, "P?LINE") == "OUTSIDE-LINE-C":
            TIM = 10
        elif game.GETP(game.HERE, "P?CORRIDOR") != 0:
            TIM = 3
        else:
            TIM = 2 + game.GETP(game.HERE, "P?SIZE")
        game.TELL(
            "An exhaustive search of even a single room would take hours. A more "
            "productive approach would be to examine or search various items of interest "
            "within the room. A cursory search would take on the order of ", end=""
        )
        game.N(TIM)
        game.TELL(
            " minutes, but it wouldn't reveal much. Would you like to do it anyway? (Y/N)", end=""
        )
        if game.YES():
            if game.INT_WAIT(TIM):
                game.TELL(
                    "Your brief search revealed nothing that was not obvious before."
                )
            else:
                game.TELL(
                    "You didn't get a chance to finish looking over the room."
                )
        else:
            game.TELL("Ok.")

def COATES_F(game, RARG=False):
    """Coates character handler"""
    if RARG == "M-OBJDESC":
        if game.IS_IN_MOTION("COATES"):
            return True
        else:
            game.TELL("Mr. Coates is here.")
        game.CARRY_CHECK("COATES")
    elif game.WINNER == "COATES":
        if game.VERB("FIND"):
            return False
        elif game.COM_CHECK("COATES"):
            return True
        else:
            game.TELL(game.PICK_ONE("WHY-ME"))
    elif game.VERB("PHONE"):
        game.TELL(game.D(game.PRSO), end="")
        if game.PRESENT_TIME > 710:
            game.TELL(
                "'s office phone rings. His secretary answers and informs you that "
                "he will be out for the rest of the day."
            )
        elif game.PRESENT_TIME > 650:
            game.TELL(
                "'s secretary answers and informs you that Mr. Coates is on his way "
                "to the Robner estate."
            )
        else:
            game.TELL(
                "'s secretary informs you that Mr. Coates is in a very important "
                "meeting and can't be disturbed. She reminds you that he "
                "will be at the Robner estate before noon."
            )
    elif game.VERB("ASK-ABOUT") and game.PRSO == "COATES":
        if game.PRSI in ["GLOBAL-OLD-WILL", "GLOBAL-NEW-WILL", "GLOBAL-FOCUS", "GLOBAL-OMNIDYNE"]:
            game.TELL(
                "\"I am not at liberty to discuss Mr. Robner's legal matters. That is "
                "privileged information between attorney and client.\""
            )
        else:
            game.TELL(
                "\"I am sorry, but I can't help you there.\""
            )

def LETTER_F(game):
    """Letter handler"""
    if game.VERB("TAKE"):
        game.FSET("ENVELOPE", "TOUCHBIT")
        return False

def OBJECT_PAIR_F(game):
    """Object pair handler for arrests"""
    if game.VERB("ARREST"):
        if game.PRESENT_TIME < 600:
            game.TELL(
                "It is rather early in the case to be making hasty judgments."
            )
        elif ((game.P_PRSO[0] in ["BAXTER", "GLOBAL-BAXTER"] and 
               game.P_PRSO[1] in ["DUNBAR", "GLOBAL-DUNBAR"]) or
              (game.P_PRSO[0] in ["DUNBAR", "GLOBAL-DUNBAR"] and
               game.P_PRSO[1] in ["BAXTER", "GLOBAL-BAXTER"])):
            if game.GETG("CORPSE-SEEN"):
                game.TELL("Ms. Dunbar is dead!")
            elif game.GETG("DUNBAR-DEAD"):
                game.TELL(
                    "Sergeant Duffy rushes into view. \"Ms. Dunbar is dead! She has "
                    "shot herself in her room! Come quickly!\" He dashes off."
                )
            elif (game.FSET("BAXTER-PAPERS", "TOUCHBIT") and
                  game.FSET("LAB-REPORT", "TOUCHBIT") and
                  game.GETG("NOTE-READ") and
                  game.GETG("STUB-D")):
                game.CRLF()
                game.END_HEADER("September 5")
                game.TELL(
                    "Congratulations on your superb handling of the Robner case. As you have "
                    "probably heard, a jury convicted Mr. Baxter and Ms. Dunbar today of the "
                    "murder of Mr. Robner. Thanks to you, the murderers will be behind bars, "
                    "possibly for the rest of their lives. Thanks for a job brilliantly done. "
                    "Which reminds me of another fascinating case I would like to assign you to...\n"
                    "\n"
                    "Coming soon: Another INTERLOGIC Mystery from Infocom\n"
                )
                game.EPILOGUE()
            elif game.PRESENT_TIME < 700:
                game.TELL(
                    "You realize the arrest would be a trifle premature, since you're not even "
                    "sure that a murder was committed."
                )
            elif not game.FSET("LAB-REPORT", "TOUCHBIT"):
                game.CRLF()
                game.END_HEADER("August 19")
                game.TELL(
                    "The District Attorney has decided not to seek an indictment in the Robner "
                    "case. He points out that it has never been proven that a murder was committed, "
                    "despite the deep suspicions to the contrary. Thanks for your help on this "
                    "case. It's too bad we couldn't find out more about the circumstances "
                    "surrounding the death of Mr. Robner.\n\n"
                )
            elif not game.FSET("BAXTER-PAPERS", "TOUCHBIT"):
                game.CRLF()
                game.END_HEADER("September 2")
                game.TELL(
                    "A grand jury looking into the death of Mr. Robner has decided not to indict "
                    "the accused. They felt that the lack of motive as well as the contorted "
                    "hypothesis involving the actual mechanism of the murder of Mr. Robner was not "
                    "convincing. Personally, I think you're on the right track, but I must admit "
                    "that the evidence is meager. Thank you for helping in the case.\n\n"
                )
            elif not game.GETG("NOTE-READ"):
                game.CRLF()
                game.END_HEADER("October 4")
                game.TELL(
                    "The jury in the Robner case has declined to convict Mr. Baxter and Ms. "
                    "Dunbar. Appearances indicate that the verdict was difficult, and that several "
                    "jury members were convinced that the two were guilty. However, no evidence "
                    "was presented directly relating the Focus case with the murder of Mr. Robner. "
                    "This left the question of motive unresolved. I appreciate your efforts in the "
                    "case and am sorry to report this outcome to you.\n\n"
                )
            else:
                game.CRLF()
                game.END_HEADER("October 6")
                game.TELL(
                    "The jury in the Robner case has declined to convict Mr. Baxter and Ms. Dunbar. "
                    "Although most of the jury was convinced of their guilt, it seems that one or "
                    "two felt there was some reasonable doubt about the proposed conspiracy. Their "
                    "main concern was the lack of evidence that Baxter was near the grounds on the "
                    "night of the murder. His alibi of having been to the symphony was confirmed by "
                    "several people. Although this doesn't mean that he didn't go back to the "
                    "Robner estate later, it nevertheless was not convincing. Thank you for your "
                    "excellent efforts. It is sad to think that we may have let the murderers slip "
                    "between our fingers.\n\n"
                )
            game.CASE_OVER()
        elif ((game.P_PRSO[0] in ["BAXTER", "GLOBAL-BAXTER"] and
               game.P_PRSO[1] in ["GEORGE", "GLOBAL-GEORGE"]) or
              (game.P_PRSO[0] in ["GEORGE", "GLOBAL-GEORGE"] and
               game.P_PRSO[1] in ["BAXTER", "GLOBAL-BAXTER"])):
            if not game.FSET("LAB-REPORT", "TOUCHBIT"):
                game.TELL(
                    "You realize that there is no evidence that a murder has been committed "
                    "and decide not to go ahead with the arrest."
                )
            elif ((game.GETG("NEW-WILL-SEEN") or game.GETG("GEORGE-RUN")) and
                  game.FSET("BAXTER-PAPERS", "TOUCHBIT") and
                  game.GETG("NOTE-READ")):
                game.CRLF()
                game.END_HEADER("November 12")
                game.TELL(
                    "\nThe district attorney, after extensive interrogation of George Robner and Mr. "
                    "Baxter, has declined to seek an indictment against them. He agrees that there "
                    "has been foul play in the death of Mr. Robner and that both suspects have "
                    "motives for the crime. However, no coherent theory could be proposed which "
                    "involved the two of them conspiring to murder Mr. Robner. On the other hand, "
                    "it seems unlikely that either of them alone could have committed the crime. "
                    "I am sorry that your work has gone for naught.\n\n"
                )
                game.CASE_OVER()
            else:
                game.CRLF()
                game.END_HEADER("August 1")
                game.TELL(
                    "The district attorney has declined to indict George Robner and Mr. Baxter "
                    "in the death of Marshall Robner, noting that there is no link between the "
                    "accused, except hatred, and that all of the evidence is circumstantial. "
                    "I wish you luck on your future cases.\n\n"
                )
                game.CASE_OVER()
        else:
            game.TELL(
                "You realize that this arrest is quite farfetched and would result "
                "only in your humiliation."
            )



def EPILOGUE(game):
    """Game epilogue"""
    game.CRLF()
    game.TELL(
        "You have solved the case! If you would like, you may see the author's summary "
        "of the story. We would advise you to come up with your own first! Would you "
        "like to see the author's summary? (Y/N)", end=""
    )
    if game.YES():
        game.CRLF()
        game.TELL(
            "Mr. Robner's work was his life, as pointed out by a number of the principals. "
            "George knew that his father had lost control of the company, and a story in "
            "the newspaper indicated that Baxter intended to sell the company to a "
            "multi-national conglomerate, presumably to advance his career. Baxter admitted "
            "to the merger plans, but indicated that Mr. Robner was in complete agreement. "
            "This is contrary to what George and Mrs. Robner said. The note pad found in "
            "the library was Robner's last, desperate attempt to save the company, in which "
            "Robner threatened to expose Baxter's involvement in the Focus scandal. Baxter "
            "denied getting the note, but it was not in the trash. The papers detailing "
            "Baxter's criminality in the scandal were kept locked in a safe in a hidden "
            "closet near the library. Only George and Marshall Robner knew the whereabouts "
            "of the safe.\n"
            "  Baxter planned to murder his partner, aided by the fact that Robner was "
            "known to be depressed, even suicidal. He enlisted the help of his lover, "
            "Dunbar, one of whose medicines was found to interact fatally with the pills "
            "Robner was taking. The relationship of Baxter and Dunbar was kept quiet, "
            "although Mrs. Rourke had an inkling of it. After the concert in Hartford which "
            "both Baxter and Dunbar attended, they returned to the Robner estate. Dunbar "
            "placed some LoBlo in Robner's tea. After Robner died, Baxter used the ladder "
            "from the shed to enter the library and exchange the incriminating cup for a "
            "clean one (counting the china in the kitchen reveals that a cup is missing). "
            "Coming down the ladder, Baxter presumably dropped the cup and inadvertently "
            "left one piece on the ground in the rose garden, near the ladder holes that "
            "McNabb found while tending his roses.\n\n"
        )
    game.QUIT()

def COM_CHECK(game, PERSON):
    """Common communication check"""
    if game.VERB("WHAT"):
        game.WINNER = "PLAYER"
        game.PERFORM("V?ASK-ABOUT", PERSON, game.PRSO)
        return True
    elif game.VERB("EXAMINE"):
        game.WINNER = "PLAYER"
        game.PERFORM("V?SHOW", PERSON, game.PRSO)
        return True
    elif game.VERB("TELL-ME") and game.PRSO == "PLAYER":
        game.WINNER = "PLAYER"
        game.PERFORM("V?ASK-ABOUT", PERSON, game.PRSI)
        return True
    elif game.VERB("SHOW") and game.PRSO == "PLAYER":
        game.TELL("\"I'm sure you can find it, Inspector.\"")
        return True
    elif game.VERB("FOLLOW") and game.PRSO == "PLAYER":
        game.TELL("\"I would rather not.\"")
        return True

def PORTRAITS_F(game):
    """Portraits handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "There are five portraits: two on each side of and one above the bay window. "
            "The fading portraits are of members of the Phillips family, among the oldest "
            "in New England."
        )
    elif game.VERB("TAKE"):
        game.NO_TOUCH()

def LR_CABINETS_F(game):
    """Living room cabinets handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The cabinets are beautifully handworked walnut and mahogany."
        )

def SEURAT_F(game):
    """Seurat painting handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The painting by Seurat is a cheerful design which suits the bright decor of "
            "the dining room. It must be worth a fortune."
        )
    elif game.VERB("TAKE"):
        game.NO_TOUCH()

def PAINTINGS_F(game):
    """Paintings handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The paintings are by various artists. They are brightly colored (but not "
            "overly loud) works of cheerful outdoor scenes and still-lifes. They give the "
            "room a light and pleasant feel."
        )
    elif game.VERB("TAKE"):
        game.NO_TOUCH()

def APPLIANCE_F(game):
    """Appliance handler"""
    if game.VERB("TAKE", "USE"):
        game.TELL(
            "The appliances here are useful in preparing meals, cleaning dishes, and the "
            "like. It is unlikely that Mrs. Rourke would like you using them."
        )

def K_CABINETS_F(game):
    """Kitchen cabinets handler"""
    pass

def SILVERWARE_F(game):
    """Silverware handler"""
    if game.VERB("TAKE"):
        game.TELL(
            "Although the set would make a fine addition to your home, you resist the "
            "temptation. You would never get away with it anyway, as Mrs. Robner will no "
            "doubt count the silverware upon your departure."
        )
    elif game.VERB("COUNT"):
        game.TELL("There are 16 complete sets of silver.")
    elif game.VERB("EXAMINE"):
        game.TELL("The silver is of the finest quality and design.")

def GLASSES_F(game):
    """Glasses handler"""
    if game.VERB("COUNT"):
        game.TELL("There are at least two dozen.")
    elif game.VERB("TAKE"):
        game.NO_TOUCH()

def NO_TOUCH(game):
    """No touch response"""
    game.TELL(
        "You would be an impolite guest to fool with these things without cause."
    )

def FOODS_F(game):
    """Foods handler"""
    if game.VERB("EAT"):
        game.TELL(
            "Although manners are not taught at the Academy, surely your mother must have "
            "given you some sense of proper behavior."
        )

def FRUIT_TREES_F(game):
    """Fruit trees handler"""
    if game.VERB("PICK", "EAT", "TAKE"):
        game.TELL(
            "The fruits are not abundant, and those within reach are far from ripe."
        )

def BERRY_BUSH_F(game):
    """Berry bush handler"""
    if game.VERB("PICK", "EAT", "TAKE"):
        game.TELL(
            "You pick a few berries and pop them into your mouth. Delicious!"
        )

def BATHROOM_MIRROR_F(game):
    """Bathroom mirror handler"""
    if game.VERB("MUNG"):
        game.TELL(
            "Don't you know it's bad luck to break mirrors?"
        )
    elif game.VERB("LOOK-INSIDE"):
        game.TELL(
            "A weary Police Inspector looks back at you, with "
            "a look that seems to be saying \"Look what the cat dragged in.\""
        )

def TREE_TOPS_F(game):
    """Tree tops handler"""
    game.TELL("You can't reach the tree tops from here.")



def LIQUOR_F(game):
    """Liquor handler"""
    if game.VERB("DRINK"):
        if game.GETG("DRUNK-FLAG"):
            game.TELL(
                "It's one thing to take a bracer on occasion, but you must resist "
                "the temptation to indulge too often."
            )
        else:
            game.TELL(
                "You take a small swig of the golden fluid, which burns as it goes "
                "down."
            )
            game.SETG("DRUNK-FLAG", True)

def STEREO_F(game):
    """Stereo handler"""
    if game.VERB("LAMP-ON"):
        game.TELL(
            "The stereo is now on."
        )
        game.SETG("STEREO-ON", True)
    elif game.VERB("LAMP-OFF"):
        if game.GETG("TUNE-ON") and game.IN("GEORGE", game.HERE):
            game.TELL(
                "George turns toward you in disgust as you turn off the " + game.GETG("TUNE-ON") + "."
            )
        else:
            game.TELL("The stereo is now off.")
        game.SETG("STEREO-ON", False)
        game.SETG("TUNE-ON", False)
        game.QUEUE("I-TUNE-OFF", 0)
        return True
    elif game.VERB("TURN-UP"):
        if game.GETG("TUNE-ON"):
            game.TELL(
                "The " + game.GETG("TUNE-ON") + " is already quite loud. Any louder would probably "
                "disturb the rest of the house."
            )
        else:
            game.TELL("It's not on!")
    elif game.VERB("TURN-DOWN"):
        if game.GETG("TUNE-ON"):
            if game.IN("GEORGE", game.HERE):
                game.TELL(
                    "George stops you from turning down the volume. He is practically "
                    "addicted to the " + game.GETG("TUNE-ON") + "."
                )
            else:
                game.TELL("You can't.")
        else:
            game.TELL("It's not on!")
    elif game.VERB("LISTEN"):
        if game.GETG("TUNE-ON"):
            game.TELL(
                "You can hardly avoid it."
            )
        else:
            game.TELL(
                "Nothing's playing."
            )

def RECORDS_F(game):
    """Records handler"""
    if game.VERB("PLAY", "LISTEN"):
        game.TELL(
            "You pick a record at random and start it playing. It is a ", end=""
        )
        game.SETG("TUNE-ON", game.PICK_ONE("RECORD-TABLE"))
        game.TELL(game.GETG("TUNE-ON") + ".")
        game.ENABLE(game.QUEUE("I-TUNE-OFF", 20))
    elif game.VERB("EXAMINE"):
        game.TELL(
            "This is a large collection, with many different types of music represented. "
            "George is evidently not very particular when it comes to music."
        )

def TAPES_F(game):
    """Tapes handler"""
    if game.VERB("PLAY", "LISTEN"):
        game.TELL(
            "You pick one at random and start it up. What you hear is a ", end=""
        )
        game.SETG("TUNE-ON", game.PICK_ONE("TAPE-TABLE"))
        game.ENABLE(game.QUEUE("I-TUNE-OFF", 30))
        game.TELL(game.GETG("TUNE-ON") + ".")
    elif game.VERB("EXAMINE"):
        game.TELL(
            "George's collection of tapes is large and quite odd in its variety of "
            "music."
        )


def I_TUNE_OFF(game):
    """Turn off tune interrupt"""
    TBL = None
    if game.HERE == "GEORGE-ROOM":
        game.TELL(
            "The " + game.GETG("TUNE-ON") + " has ended (and not soon enough)."
        )
        if game.IN("GEORGE", game.HERE):
            game.TELL(
                "George walks over to his stereo and returns the music to its "
                "proper place. He then chooses a ", end=""
            )
            if game.PROB(50):
                game.TELL("record", end="")
                TBL = "RECORD-TABLE"
            else:
                game.TELL("tape", end="")
                TBL = "TAPE-TABLE"
            game.TELL(
                " from his large collection "
                "and starts it up. Dear Lord! It's a ", end=""
            )
            game.SETG("TUNE-ON", game.PICK_ONE(TBL))
            game.TELL(game.GETG("TUNE-ON") + ".")
            game.ENABLE(game.QUEUE("I-TUNE-OFF", 25))
        return True
    elif game.IN("GEORGE", "GEORGE-ROOM"):
        game.SETG("TUNE-ON", game.PICK_ONE("TAPE-TABLE"))
        game.ENABLE(game.QUEUE("I-TUNE-OFF", 35))
        return False

def CLOSET_STUFF_F(game):
    """Closet stuff handler"""
    if game.VERB("TAKE", "MOVE", "USE"):
        game.TELL(
            "You have no need for them."
        )
    elif game.VERB("SEARCH", "EXAMINE"):
        game.TELL(
            "You go through the" + game.PRSO + " and find nothing of interest."
        )

def LIBRARY_CARPET_F(game):
    """Library carpet handler"""
    if game.VERB("LOOK-UNDER"):
        game.TELL(
            "The carpeting is wall-to-wall so you can't look under it."
        )
    elif game.VERB("EXAMINE"):
        game.TELL(
            "The carpet is an expensive affair, and quite clean, except for "
            "a few small areas of dried mud in the vicinity of the desk. "
            "There are no other stains or markings that you can see."
        )
        game.FCLEAR("MUD-SPOT", "INVISIBLE")

def GLOBAL_MURDER_F(game):
    """Global murder/suicide handler"""
    STR = None
    if game.VERB("ASK-ABOUT"):
        if game.PRSI == "GLOBAL-MURDER":
            STR = game.GET("MURDER-TABLE", game.GETP(game.PRSO, "P?CHARACTER"))
            if STR == 0:
                return False
            else:
                game.TELL(STR)
        else:
            game.TELL(
                "\"I told everything I know about it to the other detectives.\""
            )

def GUEST_WINDOW_F(game):
    """Guest window handler"""
    if game.VERB("LOOK-INSIDE"):
        game.TELL(
            "From here you have a good view of the east lawn, a shed, and the "
            "lake in the background."
        )
        game.PUTP("GUEST-ROOM", "P?CORRIDOR", 512)
        game.CORRIDOR_LOOK()
        game.ENABLE(game.QUEUE("I-WINDOW-LOOK", 2))
        return True
    elif game.VERB("OPEN"):
        game.TELL("This window cannot be opened.")

def I_WINDOW_LOOK(game):
    """Window look interrupt"""
    game.PUTP("GUEST-ROOM", "P?CORRIDOR", 0)
    return False

def I_WILL_MISSED(game):
    """Will missed interrupt"""
    if game.IN("MRS-ROBNER", game.HERE):
        game.TELL(
            "Mrs. Robner turns to you. \"I don't understand why you missed the will "
            "reading. You seem so interested in everything else that goes on around "
            "here.\""
        )
        game.QUEUE("I-WILL-MISSED", 0)
    elif game.IN("COATES", game.HERE):
        game.TELL(
            "Mr. Coates says, in passing, \"To tell you the truth, Inspector, my "
            "suspicions about this case are not quite allayed. I wish you had been "
            "at the will reading. Good day.\""
        )
        game.QUEUE("I-WILL-MISSED", 0)

def S_SHELVES_F(game):
    """Shed shelves handler"""
    if game.VERB("EXAMINE"):
        game.TELL(
            "The shelves contain various garden tools."
        )

def END_HEADER(game, STR):
    """End header for letters"""
    game.TELL("Text of a letter from Police Commissioner Klutz dated ", end="")
    game.TELL(STR)
    game.TELL(":\n\nDear Inspector,\n\n     ")

def GLOBAL_HERE_F(game):
    """Global here handler"""
    FLG = False
    F = None
    if game.VERB("WHAT", "ASK-ABOUT"):
        F = game.FIRST(game.HERE)
        while F:
            if game.FSET(F, "PERSON") and F != "PLAYER":
                FLG = True
                game.DESCRIBE_OBJECT(F, True, 0)
            F = game.NEXT(F)
        if not FLG:
            game.TELL("There's nobody else here.")
        return True

def BALCONY_DOOR_F(game):
    """Balcony door handler"""
    if game.VERB("HIDE-BEHIND"):
        if not game.FSET(game.PRSO, "OPENBIT"):
            game.TELL("You open the balcony door carefully.")
            game.FSET(game.PRSO, "OPENBIT")
        if game.HERE == "LIBRARY":
            game.GOTO("LIBRARY-BALCONY")
        elif game.HERE == "LIBRARY-BALCONY":
            game.GOTO("LIBRARY")
        elif game.HERE == "MASTER-BEDROOM":
            game.GOTO("BEDROOM-BALCONY")
        else:
            game.GOTO("MASTER-BEDROOM")
        return True
    elif game.VERB("LOOK-INSIDE"):
        if game.HERE in ["MASTER-BEDROOM", "LIBRARY"]:
            game.TELL(
                "You can see the balcony, but not much beyond."
            )
        elif game.HERE == "LIBRARY-BALCONY":
            game.TELL(
                "You can see into the library from here."
            )
        else:
            game.TELL("You can see the bedroom from here.")

def GLOBAL_RED_HERRINGS_F(game):
    """Global red herrings handler"""
    if game.IN("GEORGE", "DINING-ROOM"):
        if game.VERB("EAT", "TAKE", "MOVE"):
            game.TELL(
                "You reach for the juicy herrings, but George forces you away. He "
                "is a killer where herrings are concerned."
            )
        elif game.VERB("FIND"):
            game.TELL(
                "There are more in this room than elsewhere."
            )
    elif game.VERB("FIND"):
        game.TELL("They're all around you.")
    elif game.VERB("WHAT"):
        game.TELL("That would be telling.")

def LIBRARY_DESK_F(game):
    """Library desk handler"""
    if game.VERB("LOOK-INSIDE"):
        game.TELL("There's nothing of interest in the desk.")

def RECURSIVE_BOOK_F(game):
    """Recursive book handler"""
    if game.VERB("ASK-FOR") and game.PRSO == "BAXTER":
        game.FCLEAR(game.PRSI, "NDESCBIT")
        return False
    elif game.VERB("TAKE") and game.IN("RECURSIVE-BOOK", "BAXTER"):
        game.FCLEAR(game.PRSO, "NDESCBIT")
        return False
    elif game.VERB("EXAMINE"):
        game.TELL(
            "This is a novelization of DEADLINE, a classic work of computer fiction."
        )
    elif game.VERB("READ", "OPEN"):
        game.TELL(
            "The book is a novelization of DEADLINE. You start to read it, and it seems "
            "oddly familiar, as if you had lived it."
        )

def GLOBAL_ENDING_F(game):
    """Global ending handler"""
    if game.IN("RECURSIVE-BOOK", "PLAYER"):
        if game.VERB("READ", "WHAT", "TURN"):
            game.TELL(
                "You thumb to the last page and start to read the ending, in which the "
                "protagonist reads the plot of the story and kills himself in disgust. "
                "Disgustedly, you reach into your pocket, remove a gun, and end your life."
            )
            game.QUIT()
    elif game.VERB("WHAT"):
        game.TELL("That's up to you!")
    else:
        game.TELL("You don't have the book that tells the ending.")

def CASE_OVER(game):
    """Case over handler"""
    game.CRLF()
    game.CRLF()
    game.TELL(
        "The case has ended. Would you like to start your investigation over "
        "from scratch? (Y/N)", end=""
    )
    if game.YES():
        game.RESTART()
    else:
        game.QUIT()

def SAFE_F(game):
    """Safe handler"""
    if game.VERB("OPEN") and not game.FSET("SAFE", "OPENBIT"):
        game.TELL("The safe is locked.")
    elif game.VERB("CLOSE", "LOCK") and game.FSET("SAFE", "OPENBIT"):
        game.TELL("The safe closes and locks.")
        game.FCLEAR("SAFE", "OPENBIT")
    elif game.VERB("LOCK"):
        game.TELL("It already is.")
    elif game.VERB("UNLOCK"):
        game.TELL("You don't know the combination.")
    elif game.VERB("LOOK-INSIDE", "EXAMINE"):
        game.FCLEAR("BAXTER-PAPERS", "INVISIBLE")
        return False

def SUICIDE_NOTE_F(game):
    """Suicide note handler"""
    if game.VERB("ANALYZE"):
        game.TELL(
            "The handwriting is very shaky and would be impossible to compare with samples "
            "on file. The blood makes the finding of fingerprints impossible."
        )

def GLOBAL_MR_ROBNER_F(game):
    """Global Mr. Robner handler"""
    if game.VERB("FOLLOW"):
        game.TELL("Is this what they call a death wish?")
    elif game.VERB("CALL"):
        game.TELL("You are, for the moment, not with him.")

def RANDOM_MEAL_F(game):
    """Random meal handler"""
    if game.VERB("EAT", "FIND"):
        game.TELL(
            "Although rather hungry, you realize that the case is too important "
            "for you to be eating meals."
        )
    else:
        game.TELL("What a strange notion!")

def GLOBAL_HOUSE_F(game):
    """Global house handler"""
    if game.VERB("WALK-AROUND"):
        game.TELL("Use directions to move around inside the house.")

def GRAPE_ARBOR_F(game):
    """Grape arbor handler"""
    if game.VERB("EAT"):
        game.TELL("You pick a few grapes and eat them. Mmmm!")

def GLOBAL_CALL_F(game):
    """Global call handler"""
    if (game.VERB("LISTEN") and 
        game.GETG("SECRET-MEETING") != 0 and
        game.HERE in ["BEHIND-SHED", "EAST-LAWN"]):
        game.TELL(
            "The voices from within the shed are too quiet to make out."
        )
    elif (game.VERB("LISTEN") and
          game.GETG("CALL-IN-PROGRESS") and
          game.HERE == "CORRIDOR-1"):
        game.TELL(
            "You can't make out the conversation through the door."
        )
    elif game.VERB("LISTEN"):
        game.TELL(
            "You can't hear any conversation."
        )

def GLOBAL_FINGERPRINTS_F(game):
    """Global fingerprints handler"""
    if game.VERB("TAKE") and game.PRSO == "GLOBAL-FINGERPRINTS":
        if not game.PRSI:
            game.TELL(
                "You must specify what to take the fingerprints from."
            )
        else:
            game.PERFORM("V?FINGERPRINT", game.PRSI)
            return True

def GLOBAL_LADDER_F(game):
    """Global ladder handler"""
    if ((game.HERE == "LIBRARY-BALCONY" and game.GETG("LADDER-FLAG")) or
        (game.HERE == "BEDROOM-BALCONY" and game.GETG("LADDER-FLAG-2"))):
        if game.VERB("TAKE"):
            game.TELL("It's too difficult from here.")
        elif game.VERB("RUB"):
            return False
        elif game.VERB("EXAMINE"):
            game.TELL(
                "The top of the ladder is visible, but the rest is hard to see."
            )
        else:
            game.TELL("You can't do that from here.")