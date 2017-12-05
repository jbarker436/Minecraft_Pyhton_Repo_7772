from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 5
shwrY = 5
shwrZ = 5

width = 10
heigth = 10
length = 10

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length:
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                 shwrX + width, shwrY + height, shwrZ + lenght, 8)

else:
    mc.setBlocks(shwrX,shwrY + height, shwrZ,
                 shwrX + width, shwrY + height, shwrZ + length, 0)
