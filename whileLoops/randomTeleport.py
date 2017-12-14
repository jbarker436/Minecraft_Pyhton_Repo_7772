import random
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

loopCount = 0

while loopCount <= 10:

    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)

    mc.player.setTilePos(x, y, z)

    loopCount = loopCount + 1
    print(loopCount)
    time.sleep(.5)
