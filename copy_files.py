# This copies all the files from a mentioned directory(including files in subfolders) to mentioned destination
import os
import sys
import shutil
source = sys.argv[1]
destination = sys.argv[2]
if os.path.isdir(source):
        if os.path.isdir(destination):
                for root, dirs, files in os.walk(source):
                        for file in files:
                                path_file = os.path.join(root,file)
                                shutil.copy2(path_file,destination)
        else:
                print("Destination Directory Doesn't exist. Please create it")
else:
        print("Source Is not a folder")
