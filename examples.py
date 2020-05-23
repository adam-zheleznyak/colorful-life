from colorful_life import *

rand_grid = random_colors(random_grid(25, 25))
colorful_animation(rand_grid) 
#save_as_gif(rand_grid, 100, "random_example.gif") # this can take a minute and will only start after the animation window from the previous line is closed




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




high_life_replicator = [
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, Hue(0), Hue(0), Hue(0), None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, Hue(1/2), None, None, Hue(0), None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, Hue(1/2), None, None, None, Hue(0), None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, Hue(1/2), None, None, Hue(0), None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, Hue(1/2), Hue(1/2), Hue(1/2), None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]	
]
#colorful_animation_limited(high_life_replicator, 120, hard_boundary=False, rule=[[3,6],[2,3]]) #each time you run this, the color variation makes quite a difference in the colors of the final position
#save_as_html(high_life_replicator, 120, "high_life.html", hard_boundary=False, rule=[[3,6],[2,3]])




replicator_rule=[[None for i in range(65)] for j in range(65)]
replicator_rule[32][32] = Hue(0)
#colorful_animation(replicator_rule, hard_boundary=False, rule=[[1,3,5,7],[1,3,5,7]], interval=150, cell_size=.1)
#save_as_gif(replicator_rule, 190, "replicator_rule.gif", hard_boundary=False, rule=[[1,3,5,7],[1,3,5,7]], interval=150, cell_size=.1) #takes quite a bit of time




day_and_night_rule = []
size = 100 #should be even
density = .6
rand_grid = random_grid(size//2, size, density) + random_grid(size//2, size, 1-density)
# making this grid reverse symmetric across the horizontal and vertical to show off the symmetric properties of the day and night rule
for j in range(size):
	row=[]
	for i in range(size):
		if i<size/2:
			if j<size/2:
				cell = rand_grid[j][i]
			else:
				cell = 1-rand_grid[size-j-1][i]
		else:
			if j<size/2:
				cell = 1-rand_grid[j][i]
			else:
				cell = rand_grid[size-j-1][i]
		row.append(cell)
	day_and_night_rule.append(row)
day_and_night_rule = random_colors(day_and_night_rule)
#colorful_animation(day_and_night_rule, hard_boundary=False, rule=[[3,6,7,8],[3,4,6,7,8]], interval=150, cell_size=.05)
#save_as_mp4(day_and_night_rule, 200, "day_and_night_rule.mp4", hard_boundary=False, rule=[[3,6,7,8],[3,4,6,7,8]], interval=150, cell_size=.05)