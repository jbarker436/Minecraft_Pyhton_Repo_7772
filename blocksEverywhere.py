from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
blockType = 103
count = 0
def randomBlockLocations(blockType, repeats):
    count = 0    
while True:
    x = random.randint(-127,127)
    z = random.randint(-127,127)
    y = mc.getHeight(x, z)
    mc.setBlock(x, y, z, blockType)
    count += 1

