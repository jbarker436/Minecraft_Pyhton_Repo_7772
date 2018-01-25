from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103

def water():
    return 8

def wool():
    return 35

def lava():
    return 10

def TNT():
    return 46

def flower():
    return 38

def diamond_block():
    return 57

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)
