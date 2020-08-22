##############################
# Created by Nashia Holloway #
##############################

# import helpers
import argparse, sys, os, os.path
from PIL import Image, ImageOps

class cachemap:
    def __init__(self, source=os.path.dirname(os.getcwd()), dest=os.path.dirname(os.getcwd())):
        self.src = source
        self.dst = dest

    def read_bmp(tile):
        # as tiles come in, add them to the end of the 1D array after grayscaling

        # save images in greyscale
        tile = skimage.color.rgb2gray(tile)
        return True

    def genetic_algo():
        pass
    
    def export_sol():
        pass

    def cleanup():
        pass

if __name__ == "__main__":
    # cool ascii art
    print("   ___    ________  ________  ________  ___  ___  _______   _____ ______   ________  ________     ___            ")
    print(" _|\  \__|\   ____\|\   __  \|\   ____\|\  \|\  \|\  ___ \ |\   _ \  _   \|\   __  \|\   __  \  _|\  \__         ")
    print("|\   ____\ \  \___|\ \  \|\  \ \  \___|\ \  \\\  \ \   __/|\ \  \\\__\ \  \ \  \|\  \ \  \|\  \|\   ____\        ")
    print("\ \  \___|\ \  \    \ \   __  \ \  \    \ \   __  \ \  \_|/_\ \  \\|__| \  \ \   __  \ \   ____\ \  \___|_       ")
    print(" \ \_____  \ \  \____\ \  \ \  \ \  \____\ \  \ \  \ \  \_|\ \ \  \    \ \  \ \  \ \  \ \  \___|\ \_____  \      ")
    print("  \|____|\  \ \_______\ \__\ \__\ \_______\ \__\ \__\ \_______\ \__\    \ \__\ \__\ \__\ \__\    \|____|\  \     ")
    print("    ____\_\  \|_______|\|__|\|__|\|_______|\|__|\|__|\|_______|\|__|     \|__|\|__|\|__|\|__|      ____\_\  \    ")
    print("   |\___    __\                                                                                   |\___    __\   ")
    print("   \|___|\__\_|                                                                                   \|___|\__\_|   ")
    print("        \|__|                                                                                          \|__|     ")

    # args
        # -h to show usage
        # -src or -s read in data from specified dir (containing .bmp files)
        # -dst or -d output final pic to specified dir
        # -num max tiles to solve
    arg = argparse.ArgumentParser(description = "RDP Bitmap Cache Solver")
    arg.add_argument("-s", "--source", help="Specify directory to read .bmp images from.", required=True)
    arg.add_argument("-d", "--destination", help="Specify the directory to output final image to.", required=True)
    arg.add_argument("-n", "--num_tiles", help="Max number of tiles to solve.", required=False)
    use = arg.parse_args(sys.argv[1:])
    cm = cachemap(source=use.s, dest=use.d)

    if os.path.isdir(use.s): # if source is valid, proceed
        sys.stdout.write("[+] Reading in images from %s" % (os.linesep))
        images = []
        
    elif not os.path.isfile(use.s): # if source is invalid, handle 
        sys.stderr.write("Invalid -s/--source path %s. Use -h/--help for help" % (os.linesep))
        exit(-1)
    else:
        pass
    for img in images:
        if cm.read_bmp(img):
            cm.genetic_algo()
            cm.export_sol()
            cm.cleanup()

    # flow
        # create a 1D array of tiles (grayscale? yes or no? Do research on what's best)
            # NOTE: no need to rotate or resize tiles, they will be 64x64 bit pixel tiles
        # create initial population with edge pieces, n size, and n segments
        # calculate fitness (or how close to the final answer we are)
        # output the "solved" or generations of "solved" pictures
        # do more research on what is right :D

