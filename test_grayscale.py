import glob
import skimage.color
import os, os.path, sys

if __name__ == "__main__":
    source = os.path.dirname(os.path.realpath(__file__))
    print (source)
    dest = os.path.dirname(os.path.realpath(__file__))
    print (dest)

    source = input("source: ")
    dest = input("dest: ")

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

    image = glob.glob("%s/*.jpg" % source)
    tile = skimage.color.rgb2gray(image)

