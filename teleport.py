from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()

x=10
y=110
z=12

mc.player.setTilePos(x, y, z)

x=32
y=155
z=15

mc.player.setTilePos(x, y, z)

time.sleep(10)
