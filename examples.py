from colorful_life import *

rand_grid = random_colors(random_grid(25, 25))
colorful_animation(rand_grid) 
#save_as_gif(rand_grid, 100, "random_example.gif") #this can take a minute and will only start after the animation window from the previous line is closed

example_grid_1 = [
	[None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, Hue(0), None, None, None, None, None, None, None, Hue(1/3), Hue(1/3), Hue(1/3), None, None, None, None, Hue(2/3), None, None, None, None, None, None, None],
	[Hue(0), Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, Hue(1/3), None, None, None, None, None, Hue(2/3), None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, Hue(1/3), None, None, None, None, Hue(2/3), Hue(2/3), Hue(2/3), None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, Hue(1/6), Hue(1/6), Hue(1/6), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, Hue(1/6), None, None, None, None, None, None, None, None, None, None, None, Hue(5/6), None, None, None, None, None],
	[None, None, None, None, None, None, Hue(1/6), None, None, None, None, None, None, None, None, None, None, None, Hue(5/6), None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(5/6), Hue(5/6), Hue(5/6), None, None, None, None],
	[None, Hue(1/2), Hue(1/2), Hue(1/2), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, Hue(1/2), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, Hue(1/2), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(1/2), Hue(1/2), Hue(1/2), None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, Hue(0), Hue(0), Hue(0), None, None, None, Hue(1/2), None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, None, Hue(1/2), None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[Hue(1/3), Hue(1/3), Hue(1/3), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(1/6), None, None, None, None],
	[None, None, Hue(1/3), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(1/6), None, None, None],
	[None, Hue(1/3), None, None, None, None, None, None, None, None, None, None, Hue(2/3), Hue(2/3), Hue(2/3), None, None, None, None, Hue(1/6), Hue(1/6), Hue(1/6), None, None, None],
	[None, None, None, None, None, None, None, Hue(5/6), None, None, None, None, Hue(2/3), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, Hue(5/6), None, None, None, None, Hue(2/3), None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, Hue(5/6), Hue(5/6), Hue(5/6), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
]
#colorful_animation(example_grid_1, hard_boundary=False, interval=100)
#save_as_gif(example_grid_1, 300, "example_grid_1.gif", hard_boundary=False, interval=100)

example_grid_2=[
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), Hue(0), None, None, None, None, None, None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), Hue(0), None],
	[None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), None, None, None, Hue(0), None, None, None, None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), Hue(0), None],
	[None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, Hue(0), None, None, None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, Hue(0), None, None, None, Hue(0), None, Hue(0), Hue(0), None, None, None, None, Hue(0), None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, Hue(0), None, None, None, None, None, None, None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), None, None, None, Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
]
#colorful_animation(example_grid_2, hard_boundary=False, interval=100)
#save_as_mp4(example_grid_2, 500, "example_grid_2.mp4", hard_boundary=False, interval=100)