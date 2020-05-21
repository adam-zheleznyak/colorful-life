import math
from random import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import matplotlib.colors as clrs

class Hue:
	"""This is a class to represent a color's hue as a float mod 1. Two Hue objects can be added together to get a new Hue object."""
	
	def __init__(self, value):
		self.value = float(value % 1)
	
	def __bool__(self):
		return True
	
	def __float__(self):
		return float(self.value)
	
	def __repr__(self):
		return repr(self.value)
	
	def __add__(self, other):
		return Hue(self.value + other.value)

def average_hue(list_of_hues):
	"""
	Gets the average hue from a list of hues.
	
	Parameters:
	list_of_hues (list of Hue objects)
	
	Returns:
	Hue
	"""
	
	x = 0.0
	y = 0.0
	# Take all the hues as points on a unit circle and average their coordinates to find the average
	for hue in list_of_hues:
		x += math.cos(hue.value*2*math.pi)
		y += math.sin(hue.value*2*math.pi)
	x /= len(list_of_hues)
	y /= len(list_of_hues)
	return Hue(math.atan2(y,x)/(2*math.pi))

def random_grid(height, width, density=.3, padding=0):
	"""
	Gives a random 2D grid of 1s and 0s.
	
	Parameters:
	height (int): How many rows the grid will have
	width (int): How many columns the grid will have
	density (float): The probability any given cell will be a 1
	padding (int): If a padding value is specified, cells within the padding distance of an edge will always be 0
	
	Returns:
	2D list
	"""
	
	if not padding:
		return [[1 if random()<density else 0 for x in range(width)] for y in range(height)]
	else:
		return [[(1 if random()<density else 0) if (not (x < padding or x >= width - padding)) and (not (y < padding or y >= height - padding)) else 0 for x in range(width)] for y in range(height)]

def random_colors(grid):
	"""
	Gives random colors to a grid of cells.
	
	Parameters:
	grid (2D list): Any cell that evaluates to True will become a random color
	
	Returns:
	2D list of Hue objects
	"""
	
	return [[Hue(random()) if cell else None for cell in row] for row in grid]

def colorful_life_step(colored_grid, color_variation=0.05, hard_boundary=True):
	"""
	Runs a step for The Colorful Game of Life.
	
	The Colorful Game of Life has the same rules as Conway's Game of Life, except that all living cells also have a color assigned to them. When a new cell is born, it will take on the average color of its parents. Color variation can be added so that newly born cells can deviate slightly in color. Living cells will keep their color fixed until they die.
	
	Parameters:
	colored_grid (2D list of Hue objects): The grid that should be stepped through
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	
	Returns:
	2D list of Hue objects
	"""
	
	height = len(colored_grid)
	width = len(colored_grid[0])
	next_grid = []
	if not hard_boundary:
		if width >= 3 and height >= 3:
			for j in range(height):
				row = []
				for i in range(width):
					live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in (-1,0,1) for b in (-1,0,1) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					neighbor_count = len(live_neighbors)
					if colored_grid[j][i]:
						if neighbor_count is 2 or neighbor_count is 3:
							row.append(colored_grid[j][i])
						else:
							row.append(None)
					else:
						if neighbor_count is 3:
							hue = average_hue(live_neighbors)
							row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
						else:
							row.append(None)
				next_grid.append(row)
			return next_grid
		else:
			# Need to tweak things so cells aren't double-counted
			for j in range(height):
				row = []
				for i in range(width):
					if height >= 3:
						# width is short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in (-1,0,1) for b in range(width) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					elif width >= 3:
						# height is short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in range(height) for b in (-1,0,1) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
					else:
						# width and height are short
						live_neighbors = [colored_grid[(j+a) % height][(i+b) % width] for a in range(height) for b in range(width) if ((a is not 0 or b is not 0) and colored_grid[(j+a) % height][(i+b) % width])]
						
						
					neighbor_count = len(live_neighbors)
					if colored_grid[j][i]:
						if neighbor_count is 2 or neighbor_count is 3:
							row.append(colored_grid[j][i])
						else:
							row.append(None)
					else:
						if neighbor_count is 3:
							hue = average_hue(live_neighbors)
							row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
						else:
							row.append(None)
				next_grid.append(row)
			return next_grid
	else:
		for j in range(height):
			row = []
			for i in range(width):
				live_neighbors = [colored_grid[j+a][i+b] for a in (-1,0,1) for b in (-1,0,1) if ((a is not 0 or b is not 0) and ((j+a) % height is j+a) and ((i+b) % width is i+b) and colored_grid[j+a][i+b])]
				neighbor_count = len(live_neighbors)
				if colored_grid[j][i]:
					if neighbor_count is 2 or neighbor_count is 3:
						row.append(colored_grid[j][i])
					else:
						row.append(None)
				else:
					if neighbor_count is 3:
						hue = average_hue(live_neighbors)
						row.append(Hue(hue.value+uniform(-color_variation, color_variation)))
					else:
						row.append(None)
			next_grid.append(row)
		return next_grid

def colorful_animation(colored_grid, color_variation=0.05, hard_boundary=True, interval=300, cell_size=0.2, show=True):
	"""
	This will create an animation of The Colorful Game of Life using Matplotlib. The animation will run forever until closed.
	
	Parameters:
	colored_grid (2D list of Hue objects): The starting grid.
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	interval (int): The number of milliseconds each step should take in the animation.
	cell_size (float): The number of inches per side of each cell.
	show (bool): If this is True, the animation will open.
	
	Returns:
	An Animation object
	"""
	
	def grid_to_array(grid):
		X = np.asarray(grid)
		X = X.astype(float)
		return X
	
	height = len(colored_grid)
	width = len(colored_grid[0])
	
	fig = plt.figure(figsize=(width*cell_size, height*cell_size))
	ax = fig.add_axes([0,0,1,1], xticks=[], yticks=[], frameon=False)
	ax.axes.xaxis.set_visible(False)
	ax.axes.yaxis.set_visible(False)
	
	fig.patch.set_facecolor('black')
	
	def animate(colored_grid):
		plt.cla()
		ax.imshow(grid_to_array(colored_grid), cmap=plt.cm.hsv, norm=clrs.Normalize(vmin=0,vmax=1), interpolation='nearest')
	
	def frame_generator(colored_grid, color_variation, hard_boundary):
		yield colored_grid #for some reason, this generator is being called once before the animation start, so this is to account for that
		while True:
			yield colored_grid
			colored_grid = colorful_life_step(colored_grid, color_variation, hard_boundary)
	
	anim = anm.FuncAnimation(fig, animate, frames=frame_generator(colored_grid, color_variation, hard_boundary), interval=interval)
	
	if show:
		plt.show()
	
	return anim

def colorful_animation_limited(colored_grid, number_of_frames, color_variation=0.05, hard_boundary=True, interval=300, cell_size=0.2, show=True):
	"""
	This will create an animation of The Colorful Game of Life using Matplotlib. The animation will run for a limited number of steps and then restart.
	
	Parameters:
	colored_grid (2D list of Hue objects): The starting grid.
	number_of_frames (int): How many steps until the animation restarts.
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	interval (int): The number of milliseconds each step should take in the animation.
	cell_size (float): The number of inches per side of each cell.
	show (bool): If this is True, the animation will open.
	
	Returns:
	An Animation object
	"""
	
	def grid_to_array(grid):
		X = np.asarray(grid)
		X = X.astype(float)
		return X
	
	frames = []
	
	for i in range(number_of_frames):
		frames.append(colored_grid)
		colored_grid = colorful_life_step(colored_grid, color_variation, hard_boundary)
	
	height = len(colored_grid)
	width = len(colored_grid[0])
		
	fig = plt.figure(figsize=(width*cell_size, height*cell_size))
	ax = fig.add_axes([0,0,1,1], xticks=[], yticks=[], frameon=False)
	ax.axes.xaxis.set_visible(False)
	ax.axes.yaxis.set_visible(False)
	
	fig.patch.set_facecolor('black')
	
	def animate(colored_grid):
		plt.cla()
		ax.imshow(grid_to_array(colored_grid), cmap=plt.cm.hsv, norm=clrs.Normalize(vmin=0,vmax=1), interpolation='nearest')
	
	anim = anm.FuncAnimation(fig, animate, frames=frames, interval=interval)
	
	if show:
		plt.show()
	
	return anim

def save_as_html(colored_grid, number_of_frames, filename, color_variation=0.05, hard_boundary=True, cell_size=0.2, interval=300):
	"""
	Saves the animation as an HTML page.
	
	Parameters:
	colored_grid (2D list of Hue objects): The starting grid.
	number_of_frames (int): How many steps until the animation restarts.
	filename (str): What the HTML file should be saved as.
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	interval (int): The number of milliseconds each step should take in the animation.
	cell_size (float): The number of inches per side of each cell.
	"""
	
	colorful_animation_limited(colored_grid, number_of_frames, color_variation=color_variation, hard_boundary=hard_boundary, interval=interval, cell_size=cell_size, show=False).save(filename, writer='html', savefig_kwargs={'facecolor': 'black'})

def save_as_gif(colored_grid, number_of_frames, filename, color_variation=0.05, hard_boundary=True, cell_size=0.2, interval=300):
	"""
	Requires the package 'imagemagick' to be installed.
	
	Saves the animation as an HTML page.
	
	Parameters:
	colored_grid (2D list of Hue objects): The starting grid.
	number_of_frames (int): How many steps until the animation restarts.
	filename (str): What the HTML file should be saved as.
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	interval (int): The number of milliseconds each step should take in the animation.
	cell_size (float): The number of inches per side of each cell.
	"""
	
	colorful_animation_limited(colored_grid, number_of_frames, color_variation=color_variation, hard_boundary=hard_boundary, interval=interval, cell_size=cell_size, show=False).save(filename, writer='imagemagick', savefig_kwargs={'facecolor': 'black'})

def save_as_mp4(colored_grid, number_of_frames, filename, color_variation=0.05, hard_boundary=True, cell_size=0.2, interval=300):
	"""
	Requires the package 'ffmpeg' to be installed.
	
	Saves the animation as an HTML page.
	
	Parameters:
	colored_grid (2D list of Hue objects): The starting grid.
	number_of_frames (int): How many steps until the animation restarts.
	filename (str): What the HTML file should be saved as.
	color_variation (float): A newly born cell will deviate from its color randomly up or down, with this amount being the maximum possible deviation.
	hard_boundary (bool): Setting this to False will identify opposite edges so that cells touching the boundary will communicate with cells on the other side of the grid.
	interval (int): The number of milliseconds each step should take in the animation.
	cell_size (float): The number of inches per side of each cell.
	"""
	
	colorful_animation_limited(colored_grid, number_of_frames, color_variation=color_variation, hard_boundary=hard_boundary, interval=interval, cell_size=cell_size, show=False).save(filename, writer='ffmpeg', savefig_kwargs={'facecolor': 'black'})

# Example code:
#grid = random_colors(random_grid(25, 25))
#colorful_animation(grid) 
#save_as_gif(grid, 100, "example.gif") #can take a minute and will only start after the animation window from the previous line is closed