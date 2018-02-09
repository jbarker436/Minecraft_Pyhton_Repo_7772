from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

blockTypes = [1,
              2,
              3,
              4,
              5]
blockType = random.choice(blockTypes)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)

            


