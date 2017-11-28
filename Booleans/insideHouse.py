from mcpi.minecraft import Minecraft
mc = Minecraft.create

buildX = 12
buildY = 1
buildZ = 21
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width 

inside = buildY < y < buildY + height 

inside buildZ < z < buildZ + length 
