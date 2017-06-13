import sys
import os

directory = sys.argv[1]

# Search the specified directory for all *.nfo files
def searchdirectory(directory):
    print("Searching directory " + directory + "...")

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            if (name.endswith(".nfo")):
                print(os.path.join(root, name))

# Check input and only continue if the specified directory is valid
if os.path.isdir(directory):
    searchdirectory(directory)
else:
    print("Invalid directory: '" + directory + "'")
