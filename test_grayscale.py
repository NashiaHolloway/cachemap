import glob
import skimage.color
import os, os.path

if __name__ == "__main__":
    source = os.path.dirname(os.getcwd())
    print (source)
    dest = os.path.dirname(os.getcwd())
    print (dest)

    images = glob.glob("%s/*.bmp" % source)
    for tile in images:
        tile = skimage.color.rgb2gray(tile)

