# ---------- Packages -----------


import os
from os.path import isfile, join
from PIL import Image
from PIL.ExifTags import TAGS


# ------------ Start Execution -------------


# Folder path
folderpath = os.getcwd() + r"\images"

# Adding all available files in a list
all_files = [ f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]
print("-"*100)
for image in all_files:    
    print("Showing data of "+image)
    print("-"*100)
    # Adding full image path
    image1= folderpath+"\\"+image    
    img = Image.open(image1)
    exifdata = img.getexif()
    
    # Looping through all the tags 
    for tagid in exifdata:
        
        # Getting the name of each tag
        tagname = TAGS.get(tagid, tagid)

        # Getting the value of each tag
        value = exifdata.get(tagid)
        
        # Printing the information obtained
        print(f"{tagname:25}: {value}")
    print("-"*100)