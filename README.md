# cachemap
Program to "solve" RDP Bitmap Cache images using a Genetic Algorithm

## Questions That Need Answers
1. What are the most used bitmap cache parsers?

* [bmc-tools](https://github.com/ANSSI-FR/bmc-tools) python script. works on .bin and .bmc files and outputs .bmp files to a sepcified directory. BMCViewer apparently works too, but you need to buy commercial software in order to use it.

2. After parsing, what does it look like?

* Using bmc-tools, .bmp files are the result of running the python script. They can either be on their own, or aggregated together to create one collage .bmp file.

3. Are the "tiles" oriented the right way?

* Yes. There will be no need to "orient" the tiles a specific way.

## Niche Breakdown
There are RDP bitmap cache parsers out in the world, so we don't need to repeat that work. What I'm interested in is creating a way to "solve the puzzle" of bitmap caches. This idea sparked after hearing about an IR where an analyst had to manually cut up the parsed bitmap cache and organize the "tiles" to create a picture of what the adversary was doing on the host. When it comes to IRs, the faster you are able to find answers, the better. By implementing a genetic algorithm, I hope to automate a solution to this puzzle.

## Integration with bmc-tools
When decoding the .bin or .bmc files, a .bmp image is created with the naming convention "Cachexxxx.bin_tileNum.bmp" (xxxx starts as 0000 and is incremented by 1 for each individual .bin file) for .bin or "bcache24.bmc_tileNum.bmp" for .bmc. They are all exported to the same directory, most times numbering in the thousands, depending on how many individual .bin or .bmc files there are. However, with the naming convention, we will be able to group them together based on which original file they're associated with.

I have updated the bmc-tools code for compatability with Python 3. I will make a pull request once finished with this project, but cloning my fork of it will guarantee success.

## Genetic Algoritm Breakdown
Genetic algorithms are cool because they mimic evolution in the natural world. They are used in certain cases where brute forcing the problem would take too long. There are three principles we need to take into account when creating a genetic algorithm:

1. **Herdity**: Traits need to be passed down from parents to children (the next generation).
2. **Variation**: Without mutations, the next generation will be exactly the same as the previous and remain stagnant.
3. **Selection**: Only the "fittest" should be able to pass on their traits to the next generation.

### Steps
**Create a Population**

We need to populate the tiles in order to process them with the genetic algorithm. This is made simple, since we have already parsed the .bin and .bmc files with bmc-tools. So the first step is to stage the tiles in some data structure. A one dimensional array will be good for this. I have chosen to process the images in grayscale, as [my research has shown](https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/) it is easier that way.


## Resources
[Genetic Algorithm Training](https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV)

[The Nature of Code](https://natureofcode.com/book/chapter-9-the-evolution-of-code/)

[GA Jigsaw Puzzle Research Paper](https://arxiv.org/pdf/1711.06766v1.pdf)

[Tyler Foxworthy's Presentation](https://www.youtube.com/watch?v=6DohBytdf6I)

[Kris Nguyen's Jigsaw Puzzle Solver](https://github.com/KrisNguyen135/Genetic-Jigsaw-Solver)

[The Importance of Grayscaling](https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/)

[Skimage Library](https://scikit-image.org/docs/dev/api/skimage.html)

