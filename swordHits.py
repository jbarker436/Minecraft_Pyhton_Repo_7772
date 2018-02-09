from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(10)

blockHits = mc.events.pollBlockHits()

blockHitsLength = len(blockHits)

mc.postToChat("Your score is " + str(blockHitsLength))
