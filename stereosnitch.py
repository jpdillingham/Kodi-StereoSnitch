import sys
import os
import re

# Search the specified directory for all *.nfo files
def searchdirectory(directory):
    print("Searching directory " + directory + "...")

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            if name.endswith(".nfo"):
                checknfo(os.path.join(root, name))

# Check the contents of the specified NFO for 2 channel audio
def checknfo(nfo):
    contents = readfile(nfo)

    try:
        m = re.search(r"<channels>(.*)<\/channels>", contents)
        if m.group(1) == '2':
            print(nfo)
    except:
        pass


# Read and return the contents of the specified file
# If the read fails for any reason, return an empty string
def readfile(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        return ""

# Check the input, and if it is valid search the specified directory
if len(sys.argv) == 1:
    print("Specify a directory to search.")
elif not os.path.isdir(sys.argv[1]):
    print("Directory '" + sys.argv[1] + "' not found.")
else:
    searchdirectory(sys.argv[1])
