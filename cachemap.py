##############################
# Created by Nashia Holloway #
##############################

# import helpers
import argparse, sys, os, os.path
from PIL import Image, ImageOps # Pillow
from progress.bar import Bar # progress bar

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
    args = arg.parse_args()
    cm = cachemap(source=args.source, dest=args.destination)

    if os.path.isdir(args.source): # if source is valid, proceed
        image_list = []
        max = len(os.listdir(args.source)) # number of images in dir (starting at 1)
        bar = Bar("[+] Reading in images from %s" % (args.source), max=max)
        for image in os.listdir(args.source):
            if image.endswith(".bmp"):
                # add image to array
                image_list.append(Image.open(os.path.join(args.source,image)))
                bar.next()
    else:
        sys.stderr.write("Invalid -s/--source path %s. Use -h/--help for help" % (os.linesep))
        exit(-1)

#     for img in images:
#         if cm.read_bmp(img):
#             cm.genetic_algo()
#             cm.export_sol()
#             cm.cleanup()

    # flow
        # create a 1D array of tiles (grayscale? yes or no? Do research on what's best)
            # NOTE: no need to rotate or resize tiles, they will be 64x64 bit pixel tiles
        # create initial population with edge pieces, n size, and n segments
        # calculate fitness (or how close to the final answer we are)
        # output the "solved" or generations of "solved" pictures
        # do more research on what is right :D

