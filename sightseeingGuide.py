from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'Things': (46, 7, 16), 
         'Crater': (78, 1, 11),
         'Desert': (-19, 9, 36),
         'Lake': (-17, -1, 9)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x = location[0]
        y = location[1]
        z = location[2]
        
        mc.player.setTilePos(x, y, z) 
        
