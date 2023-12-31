# Create a function which allows automatically generate subfolders based on the file types currently existed in a specified folder
# Then move all the files to the subfolders that belong to their category


# import os and shutil modules to allow interact with the operating system and perform actions such as move, copy and delete files
import os, shutil 

# create a function which takes the file path containing the files need to be sorted as a parameter
def autoFileSorter(filePath):    

    # add a forward slash at the end of the path
    filePath+="/"

    # check whether the path exists
    if os.path.exists(filePath):

        # show all files in the specified path and store them into a list
        fileNames=os.listdir(filePath)

        # loop through all files in the specified path to extract the extensions
        fileExt=[]
        for tempFileNames in fileNames:
                pathPart, extPart= os.path.splitext(filePath+tempFileNames)
                # add ext to the list if ext is not blank
                if extPart:
                    fileExt.append(extPart)

        # create subfolder names by using the extensions and store them into a list 
        # eg: a subfolder named pngFile will be generated if a png file was found
        folderNames=[]
        for tempFileExt in fileExt:
            folderNames.append(tempFileExt[1:].title()+"_"+"Files")

        # create subfolders based on the names generated above if those subfolders are not already existed
        for tempFolderNames in folderNames:
            if not os.path.exists(filePath+tempFolderNames):
                os.makedirs(filePath+tempFolderNames)

        # loop through all files with extension in the specified path
        # check whether the files are already existed in the subfolders before moving the files to the subfolders that belong to their category
        for tempFileNames in fileNames:
                pathPart, extPart= os.path.splitext(filePath+tempFileNames)
                if extPart and not os.path.exists(filePath+extPart[1:].title()+"_"+"Files/"+tempFileNames):
                    shutil.move(filePath+tempFileNames,filePath+extPart[1:].title()+"_"+"Files/"+tempFileNames)
                elif os.path.exists(filePath+extPart[1:].title()+"_"+"Files/"+tempFileNames):
                    print("One or multiple files already existed in the subfolder")
    
    # warn user if the path that they entered is not found
    else:
         print("Path cannot be found, please pass a valid path to the function.")

# call the autoFileSorter function
# enter the file path containing the files need to be sorted as an argument for this function
# add r before the path or change the backslash to \\ or / to escape the backslash
autoFileSorter(r"C:\Users\baby_\Desktop\Projects\Python_Projects\Automatic_File_Sorter_In_File_Explorer_Files_For_Sorting")
autoFileSorter("C:/Users/baby_/Desktop/test")
autoFileSorter(r"C:\Users\baby_\Desktop\Not_Exist_Path")

