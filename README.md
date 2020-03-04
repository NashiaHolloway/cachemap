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

## Genetic Algoritm Breakdown
Genetic algorithms are cool because they mimic evolution in the natural world. They are used in certain cases where brute forcing the problem would take too long.


## Resources
[Genetic Algorithm Training](https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV)

[The Nature of Code](https://natureofcode.com/book/chapter-9-the-evolution-of-code/)

[GA Jigsaw Puzzle Research Paper](https://arxiv.org/pdf/1711.06766v1.pdf)

[Tyler Foxworthy's Presentation](https://www.youtube.com/watch?v=6DohBytdf6I)

[Kris Nguyen's Jigsaw Puzzle Solver](https://github.com/KrisNguyen135/Genetic-Jigsaw-Solver)

