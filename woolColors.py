from mcpi.minecraft import Minecraft
mc = Minecraft.create()
'''
blockcolor=input("Enter a block color(pink,orange,magenta,light blue,yellow, or lime)")
block=35
blockstate=-1
pos = mc.player.getTilePos()
def getWoolState(color):
    if blockcolor == "pink":
        blockState = 6
    elif blockcolor == "orange":
        blockState = 1
    elif blockcolor == "magenta":
        blockState = 2
    elif blockcolor == "light blue":
        blockState = 3 
    elif blockcolor == "yellow":
        blockState = 4
    elif blockcolor == "lime":
        blockState = 5
mc.setBlock(pos.x,pos.y,pos.z,block,blockstate)

getWoolState 

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
'''
while True:
    color=input("Enter a block color(pink,orange,magenta,light blue,yellow, or lime)")
    block=35
    state=-1
    if str(color) == "pink":
        state=6
    elif str(color) == "orange":
        state=1
    elif str(color) == "magenta":
        state=2
    elif str(color) == "light blue":
        state=3
    elif str(color) == "yellow":
        state=4
    elif str(color) == "lime":
        state=5
    pos=mc.player.getTilePos()
    mc.setBlock(pos.x,pos.y+3,pos.z,block,state)
    
