import os,pygame,send2trash

#username = os.getenv('USERNAME')
os.chdir("C:\\Users\\Von\\Desktop\\")
items = os.listdir(os.getcwd())
removeTotal = keptTotal = errorTotal = 0

print( os.getcwd() + " dir has " + str(len(items)-1) + " items\n")

for i in range(0,len(items)):
    try:
        fileName = items[i]
        img = pygame.image.load(fileName)
        if(items[i].endswith('jpg')):
            send2trash.send2trash(fileName)
            removeTotal += 1
            print("Remove: " + fileName + " " + str(i) + '/' + str(len(items)-1))
        elif(img.get_width() == 1920 and img.get_height() == 1080):
            print("Kept: " + fileName + " " + str(i) + '/' + str(len(items)-1))
            keptTotal += 1
    except:
        if(items[i].endswith("webm")):
            send2trash.send2trash(fileName)
            removeTotal += 1
            print("Remove: " + fileName + " " + str(i) + '/' + str(len(items)-1))
        errorTotal += 1
        print("Error: " + fileName + " " + str(i) + '/' + str(len(items)-1))
            
print("Total Removed: ", removeTotal)
print("Total Kept: ", keptTotal)
print("Errors: ", errorTotal)
