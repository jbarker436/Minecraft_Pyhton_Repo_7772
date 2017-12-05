from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.postToChat("thxn 4 teh diamondd")

elif gift == 6:
    mc.postToChat("i ges sapelinks r gud lyk diamondz")

else:
    mc.postToChat("Bring a gift to " +str(x) + ", " + str(y) + ", " + str(z))
