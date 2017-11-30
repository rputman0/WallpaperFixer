#Python 3.6.0
#BulkFileMover.py - checks every subfolder and moves specific file types to a designated folder

import shutil,os,send2trash

src = #"C:\\Users\\Von\\Desktop\\other"
dst = "C:\\Users\\Von\\Desktop\\other\\coolStuff"
os.makedirs(dst,exist_ok=True)

filesMoved = 0
errors = 0

start = input("Do you want to move files from: " + src + '\n to\n' + dst + '\n(yes/no)')

while(start == 'yes'):
    os.chdir(src)
    for folderName,subFolder,fname in os.walk(os.getcwd()):
        for filename in fname:
            try:
                if(filename.endswith('.mp4')):
                    filePath = folderName + '\\' + filename
                    shutil.move(filePath,dst)
                    print("Moved: ",filename)
                    filesMoved += 1
            except:
                errors += 1
                print("Error",filename)

print("Files Moved: ",filesMoved)
print("Errors: ",errors)

#use for filename in os.listdir() for only one dir
