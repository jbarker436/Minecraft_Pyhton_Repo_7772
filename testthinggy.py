from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

position = mc.player.getTilePos()

while True:
        x = x + 1
        mc.postToChat("Yeet" + x)
