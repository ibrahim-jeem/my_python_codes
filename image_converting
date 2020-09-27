#This code will - Rotate, Resize, Save the image in a specific formate in a specific folder.

#!/usr/bin/env python3

import os, sys
from PIL import Image

rotate = input("Rotation degree:")
location = input("Where to save:")

for root, dirs, files in os.walk("."):    #this will look through the files
  for file in files:
    f, e = os.path.splitext(file)
    savefile = "location" + f          #save folder location
    try:
      #print(outfile)
      Image.open(file).rotate(rotate).resize((128,128)).convert("RGB").save(outfile, "JPEG")   #main operation

    except IOError:
      print("cannot convert", file)

print("task complete")
