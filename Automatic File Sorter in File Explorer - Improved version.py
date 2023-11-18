# Automatically generate subfolders based on the file types currently existed in the main folder
# Then move all the files to the subfolders that belong to their category


# import os and shutil modules to allow interact with the operating system and perform actions such as move, copy and delete files
import os, shutil

# store the file path of the main folder into a variable
# use / instead of \
filePath= "C:/Users/baby_/Desktop/Projects/Python Projects/Automatic File Sorter in File Explorer - Files for sorting/"

# show all files in the specified path and store them into a list
fileNames=os.listdir(filePath)

# loop through all files in the main folder to extract the extensions
fileExt=[]
for tempFileNames in fileNames:
        pathPart, extPart= os.path.splitext(filePath+tempFileNames)
        # add ext to the list if ext is not blank
        if extPart:
            fileExt.append(extPart)

# create sub folder names by using the extensions and store them into a list 
folderNames=[]
for tempFileExt in fileExt:
    folderNames.append(tempFileExt[1:]+"Files")

# create folders if those folders are not existed
for tempFolderNames in folderNames:
    if not os.path.exists(filePath+tempFolderNames):
        os.makedirs(filePath+tempFolderNames)

# loop through all files with extension in the main folder
# check whether the files are already existed in the subfolders before moving the files to the subfolders that belong to their category
for tempFileNames in fileNames:
        pathPart, extPart= os.path.splitext(filePath+tempFileNames)
        if extPart and not os.path.exists(filePath+extPart[1:]+"Files/"+tempFileNames):
            shutil.move(filePath+tempFileNames,filePath+extPart[1:]+"Files/"+tempFileNames)
        elif os.path.exists(filePath+extPart[1:]+"Files/"+tempFileNames):
            print("One or multiple files already existed in the subfolder")
