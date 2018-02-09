from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
count = 0
mc.setBlocks(pos.x+3,pos.y,pos.z,pos.x+3,pos.y+9,pos.z,20)
while count < 10:
    mc.setBlock(pos.x+3,pos.y+count,pos.z,22)
    count += 1
    
    time.sleep(1)
    print(count) 
