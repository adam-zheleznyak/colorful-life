# The Colorful Game of Life
Reimagining Conway's Game of Life with color.

![example.gif](https://github.com/adam-zheleznyak/colorful-life/blob/master/example.gif?raw=true)

[YouTube Montage](https://youtu.be/RG0_Fw-aKpY)

[YouTube Montage of Alternative Rulesets](https://youtu.be/qSU_csTgVIA)

## The Game
The Colorful Game of Life has the same rules as Conway's Game of Life, except that all living cells also have a color assigned to them. When a new cell is born, it will take on the average color of its parents. However, there is some color variation so that newly born cells can deviate slightly from their parents. Living cells will keep their color fixed until they die.

The idea is to make Conway's Game of Life look even more lifelike by giving each cell some representation of its "genetics." In the long run, some colors will be naturally selected and will often form colonies. Adding color variation is a way to represent natural mutations that might occur over time. Although Conway's Game of Life is deterministic, having this color variation makes the colors of the cells non-deterministic (but this can be disabled in the code).

Download the project and run `examples.py` in order to see a randomized game, or uncomment some of the other examples. The main script `colorful_life.py` includes many customization options and ways to download animations of the game.
