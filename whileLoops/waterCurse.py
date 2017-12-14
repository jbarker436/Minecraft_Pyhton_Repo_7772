from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()

mc.setBlock(pos.x, pos.y, pos.z, 8)
