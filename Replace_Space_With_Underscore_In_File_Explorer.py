# Simple 

# import os and shutil modules to allow interact with the operating system and perform actions such as move, copy and delete files
import os, shutil 

# create a function which takes the file path containing the files need to be renamed as a parameter
def autoReplaceSpaceWithUnderscore(filePath):    

    # add a forward slash at the end of the path
    filePath+="/"

    # check whether the path exists
    if os.path.exists(filePath):

        # show all files in the specified path and store them into a list
        fileNames=os.listdir(filePath)

        # loop through all files in the specified path to rename them
        fileExt=[]
        for tempFileNames in fileNames:
                os.rename(filePath+tempFileNames,filePath+tempFileNames.replace(" ", "_"))

autoReplaceSpaceWithUnderscore(r"C:\Users\baby_\Desktop\Projects\Python_Projects\Web_Scrapping_Generated_Data_File")












