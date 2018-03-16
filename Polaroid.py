'''
Made By Justyn And Daniel With Love!                    ----CSP 2017~2018 Room~A238 4th~Hour
'''
from picamera import PiCamera
from mcpi.minecraft import Minecraft
from time import sleep
from skimage import io, color

userborderblockname = "Made by Justyn and Daniel"
userborderblock = "Justyn and Daniel rule all others drool"
                      
print("Welcome To The Minecraft Photo Booth Created By Justyn And Daniel!")
print("To Take a Photo, Please Input takepicture() or takephoto() to the shell!")
print("Tip : 1) Stay away from world borders and get as low as possible for a good photo!")
print("Tip : 2) Be ready to take the photo, have good lighting and be close to the camera!")

def takepicture(): #Start of takepicture() function
        camera = PiCamera()
        camera.resolution = (80,60)
        print("Taking Picture In 15 Seconds!")
        camera.start_preview()
        sleep(15)
        camera.capture('selfie.jpg')
        camera.close()

        selfie_rgb = io.imread("selfie.jpg")
        map_rgb = io.imread("colour_map.png")

        selfie_lab = color.rgb2lab(selfie_rgb)
        map_lab = color.rgb2lab(map_rgb)

        colours={(0,0):(2,0),(0,1):(3,0),(0,2):(4,0),(0,3):(5,0),(0,4):(7,0),(0,5):(14,0),(0,6):(15,0),(1,0):(16,0),(1,1):(17,0),(1,2):(21,0),(1,3):(22,0),(1,4):(24,0),(1,5):(35,0),(1,6):(35,1),(2,0):(35,2),(2,1):(35,3),(2,2):(35,4),(2,3):(35,5),(2,4):(35,6),(2,5):(35,7),(2,6):(35,8),(3,0):(35,9),(3,1):(35,10),(3,2):(35,11),(3,3):(35,12),(3,4):(35,13),(3,5):(35,14),(3,6):(35,15),(4,0):(41,0),(4,1):(42,0),(4,2):(43,0),(4,3):(45,0),(4,4):(46,0),(4,5):(47,0),(4,6):(48,0),(5,0):(49,0),(5,1):(54,0),(5,2):(56,0),(5,3):(57,0),(5,4):(58,0),(5,5):(60,0),(5,6):(61,0),(6,0):(73,0),(6,1):(79,0),(6,2):(80,0),(6,3):(82,0),(6,4):(89,0),(6,5):(103,0),(6,6):(246,0)}

        mc = Minecraft.create()
        x, y, z = mc.player.getPos()
        
#start of user selected border
        userborder = str(input("Would You Like a Border? Please Respond with Yes or No : "))
        print("userborder")
        
        if userborder=="Yes":
                userborderblockname = input("What Block Would You Like For The Border? The Options are Wood, Wool, Stone, Log or Bedrock? : ")
                print(userborderblockname + " Border Selected!")
                
                if userborderblockname == "Wood":
                        userborderblock = 5
                if userborderblockname == "Stone":
                        userborderblock = 1
                if userborderblockname == "Bedrock":
                        userborderblock = 7
                if userborderblockname == "Wool":
                        userborderblock = 35
                if userborderblockname == "Log":
                        userborderblock = 17
                        
                mc.setBlocks(x-81,y+65,z+5,x+2,y-2,z+5,int(userborderblock))        
                print("Border Added!")
                               
        elif userborder == "No":
                print("Ok, No Border!")
        else:
                mc.setBlocks(x-81,y+65,z+5,x+2,y-2,z+5,7)
                print("Not Specified! Bedrock Border Added")
#end of user selected border
                
        for i, selfie_column in enumerate(selfie_lab):
                for j, selfie_pixel in enumerate(selfie_column):
                        distance = 300
                        for k, map_column in enumerate(map_lab):
                                for l, map_pixel in enumerate(map_column):
                                        delta = color.deltaE_ciede2000(selfie_pixel,map_pixel)
                                        if delta < distance:
                                                distance = delta
                                                block = colours[(k,l)]
                        mc.setBlock(x-j, y-i+60, z+5, block[0], block[1])
        print("Photo Taken!")
        print("To Take Another Photo, Please Input takepicture() or takephoto() to the shell!")

def takephoto(): #Start of takephoto() function which is the same as the takepicture() 
        camera = PiCamera()
        camera.resolution = (80,60)
        camera.start_preview()
        print("Taking Picture In 15 Seconds!")
        sleep(15)
        camera.capture('selfie.jpg')
        camera.close()

        selfie_rgb = io.imread("selfie.jpg")
        map_rgb = io.imread("colour_map.png")

        selfie_lab = color.rgb2lab(selfie_rgb)
        map_lab = color.rgb2lab(map_rgb)

        colours={(0,0):(2,0),(0,1):(3,0),(0,2):(4,0),(0,3):(5,0),(0,4):(7,0),(0,5):(14,0),(0,6):(15,0),(1,0):(16,0),(1,1):(17,0),(1,2):(21,0),(1,3):(22,0),(1,4):(24,0),(1,5):(35,0),(1,6):(35,1),(2,0):(35,2),(2,1):(35,3),(2,2):(35,4),(2,3):(35,5),(2,4):(35,6),(2,5):(35,7),(2,6):(35,8),(3,0):(35,9),(3,1):(35,10),(3,2):(35,11),(3,3):(35,12),(3,4):(35,13),(3,5):(35,14),(3,6):(35,15),(4,0):(41,0),(4,1):(42,0),(4,2):(43,0),(4,3):(45,0),(4,4):(46,0),(4,5):(47,0),(4,6):(48,0),(5,0):(49,0),(5,1):(54,0),(5,2):(56,0),(5,3):(57,0),(5,4):(58,0),(5,5):(60,0),(5,6):(61,0),(6,0):(73,0),(6,1):(79,0),(6,2):(80,0),(6,3):(82,0),(6,4):(89,0),(6,5):(103,0),(6,6):(246,0)}

        mc = Minecraft.create()
        x, y, z = mc.player.getPos()
        
        userborder = str(input("Would You Like a Border? Please Respond with Yes or No : "))
        print("userborder")

        if userborder=="Yes":
                userborderblockname = input("What Block Would You Like For The Border? The Options are Wood, Wool, Stone, Log or Bedrock? : ")
                print(userborderblockname + " Border Selected!")
                
                if userborderblockname == "Wood":
                        userborderblock = 5
                if userborderblockname == "Stone":
                        userborderblock = 1
                if userborderblockname == "Bedrock":
                        userborderblock = 7
                if userborderblockname == "Wool":
                        userborderblock = 35
                if userborderblockname == "Log":
                        userborderblock = 17
                
                mc.setBlocks(x-81,y+65,z+5,x+2,y-2,z+5,int(userborderblock))
                print("Border Added!")
                
        elif userborder == "No":
                print("Ok, No Border!")
        else:
                mc.setBlocks(x-81,y+65,z+5,x+2,y-2,z+5,7)
                print("Not Specified! Bedrock Border Added")
        
        for i, selfie_column in enumerate(selfie_lab):
                for j, selfie_pixel in enumerate(selfie_column):
                        distance = 300
                        for k, map_column in enumerate(map_lab):
                                for l, map_pixel in enumerate(map_column):
                                        delta = color.deltaE_ciede2000(selfie_pixel,map_pixel)
                                        if delta < distance:
                                                distance = delta
                                                block = colours[(k,l)]
                        mc.setBlock(x-j, y-i+60, z+5, block[0], block[1])
        print("Photo Taken!")
        print("To Take Another Photo, Please Input takepicture() or takephoto() to the shell!")

