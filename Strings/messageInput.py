from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("What do you want to say?: ")
mc.postToChat(message)
