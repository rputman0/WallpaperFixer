#ConvertFiles.py - convert a list of files in a directory, using ffmpeg, and sends the old files to the trash
import os,ffmpeg,pygame,send2trash

os.chdir("C:\\Users\\Von\\Desktop\\Desktop Shortcuts\\Digital Pics\\tv\\movie posters")
items = os.listdir(os.getcwd())
convertedTotal = keptTotal = errorTotal = 0

print( os.getcwd() + " dir has " + str(len(items)-1) + " items")

for i in range(0,len(items)):
    try:
        fileName = items[i]
        #need this to check img width and height, if needed
        img = pygame.image.load(fileName)
        if( fileName[len(fileName)-3:] == 'jpg' or
            fileName[len(fileName)-3:] == 'JPG' ):
            
            fileOut = (fileName)[:len(fileName)-4] + '.png'
            ffmpeg.input(fileName).output(fileOut).run()
            print("File Converted: " + fileName + " -> " + fileOut + " " + str(i) + '/' + str(len(items)-1))
            convertedTotal += 1

            send2trash.send2trash(fileName)

        if( fileName[len(fileName)-4:] == 'jpeg' ):

            fileOut = (fileName)[:len(fileName)-5] + '.png'
            ffmpeg.input(fileName).output(fileOut).run()
            print("File Converted: " + fileName + " -> " + fileOut + " " + str(i) + '/' + str(len(items)-1))
            convertedTotal += 1

            send2trash.send2trash(fileName)
            
        else:
            print("File Kept As Is: " + fileName + " " + str(i) + '/' + str(len(items)-1))
            keptTotal += 1
    except:
        #if file is not a image (pdf,zip,rar,folder,webm,mp4)
        errorTotal += 1
        print("Error: " + items[i])

print("Total Converted: ", convertedTotal)
print("Total Kept: ", keptTotal)
print("Errors: ", errorTotal)
