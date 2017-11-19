import os,pygame

#get the current username and path
username = "username"
os.chdir("C:\\Users\\" + username + "\\Documents\\Wallpapers")
items = os.listdir(os.getcwd())

removeTotal = 0
keptTotal = 0
errorTotal = 0

#for every item in the directory
#if it is not a png or not 1920x1080, remove it
#otherwise keep the image
for i in range(0,len(items)):
    try:
        fileName = items[i]
        img = pygame.image.load(fileName)
        if(fileName[len(fileName)-3:] != "png"):
            os.remove(fileName)
            removeTotal += 1
            print("Remove: " + fileName + " " + str(i) + '/' + str(len(items)-1))
        elif(img.get_width() == 1920 and img.get_height() == 1080):
            print("Keep: " + fileName + " " + str(i) + '/' + str(len(items)-1))
            keptTotal += 1
        else:
            os.remove(fileName)
            removeTotal += 1
            print("Remove: " + fileName + " " + str(i) + '/' + str(len(items)-1))
    except:
        errorTotal += 1
        print("ERROR: " + items[i])
            
print("Total Removed: ", removeTotal)
print("Total Kept: ", keptTotal)
print("Errors: ", errorTotal)
