from mcpi.minecraft import Minecraft
mc = Minecraft.create()

height = 5
width1 = 6
length1 = 6
width2 = 4
length2 = 4

def growTree(x, y, z):
    mc.setBlock(x, height, z)
    mc.setBlock(width1 + 5, y, length1 + 5)
    mc.setBlock(width2 + 6, y, length2 + 6)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
