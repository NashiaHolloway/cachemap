import glob
import PIL
from PIL import Image, ImageOps
import os, os.path, sys

if __name__ == "__main__":
    source = os.path.dirname(os.path.realpath(__file__))
    print (source)
    dest = os.path.dirname(os.path.realpath(__file__))
    print (dest)

    #source = input("source: ")
    #dest = input("dest: ")

    if os.path.isdir(source): # if source is valid, proceed
        sys.stdout.write("[+] Reading in images from %s\n" % (source))
    else:
        sys.stderr.write("Invalid -s/--source path %s. Use -h/--help for help\n" % (source))
        exit(-1)

    if os.path.isdir(dest):
        sys.stdout.write("[+] Writing images to %s\n" % (dest))
    else:
        os.makedirs(dest)
        sys.stdout.write("[+] Created directory %s\n" % (dest))
        sys.stdout.write("[+] Writing images to %s\n" % (dest))
    
    # import all *.jpg images in greyscale
    # NOTE There is no "easy" way to convert greyscale to rgb; must map each greyscale value to right rgb value in order to get original
    for filename in glob.glob('%s\*.jpg' % source):
        print(filename)
        gray_image = ImageOps.grayscale(Image.open(filename))
        # gray_image.show()
        gray_image.save(filename)


