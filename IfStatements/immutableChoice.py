from mcpi.minecraft import Minecraft
mc = Minecraft.create()

immutable = str("Y")
response = input("Do you want blocks to be immutable? Y/N: ")

if response == immutable:

    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
else:
    mc.setting("world_immutable", False)
    mc.postToChat("World is mutable")
