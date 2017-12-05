from mcpi.minecraft import Minecraft
mc = Minecraft.create()

crater = str("Y")
answer = input("Create a crator Y/N: ")

if answer == crater:

    pos = mc.player.getPos()
mc.setBlocks(pos.x + 100, pos.y + 100, pos.z +100, pos.x - 100, pos.y -100, pos.z -100, 0)
mc.postToChat("Boom!")
