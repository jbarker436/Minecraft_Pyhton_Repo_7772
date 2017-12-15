from mcpi.minecraft import Minecraft

mc = Minecraft.create()

blockType = int(input("What type of block do you want?: "))
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)
try:
    noOfSunglasses = int(input("How many sunglasses do you own? "))
    mc.setBlock(x, y, z, blockType)
except:
    print("please enter a number")
