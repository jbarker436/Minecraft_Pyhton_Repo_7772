from mcpi.minecraft  import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12

gift = mc.getBlock(x, y, z)
p = mc.player.getTilePos()
if gift != 0:
    mc.setBlocks(1, 2, 1, -10, -10, -10, 57)
    mc.setBlocks(0, 2, 0, -9, -9, -9, 0)
    mc.postToChat("The secret room has been opened")

else:
    mc.postToChat("Place an offering on the pedestal.")
    mc.setBlocks(p.x + 1, p.y + 1, p.z + 1, p.x - 1, p.y - 1, p.z - 1, 10)
