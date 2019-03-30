
COLOUR_DICTIONARY = {"Coral1": "#ff7256", "CornflowerBlue": "#6495ed", "DarkGreen": "#006400", "DarkOrchid": "#9932cc",
                     "DeepPink1": "#ff1493", "firebrick1": "#ff3030", "GhostWhite": "#f8f8ff", "goldenrod1": "#ffc125",
                     "green1": "#00ff00", "HotPink": "#ff69b4"}

colour_name = input("Please enter the colour you need: ")
while colour_name != "":
    if colour_name in COLOUR_DICTIONARY:
        print(colour_name + "'s hex number is", COLOUR_DICTIONARY[colour_name])
    else:
        print("Invalid Colour name")
    colour_name = input("Please enter the colour you need: ")

