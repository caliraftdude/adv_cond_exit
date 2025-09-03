from Deadline import load_config

# Load the game.json file to find out the import list
config = load_config()

doors_json = load_config(config["doors"])
rooms_json = load_config(config["rooms"])

print(config["game_name"])
