from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
        print("Don't forget to put your message in quotes")
        message = input("What do you want to say? ")
        mc.postToChat(message)
