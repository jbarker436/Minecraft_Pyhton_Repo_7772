from mcpi.minecraft import Minecraft

mc = Minecraft.create()

blockType = int(input("Yeet: "))
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)
try:
    noOfSunglasses = int(input("How many sunglasses do you own? "))
except:
    print("please enter a number")
