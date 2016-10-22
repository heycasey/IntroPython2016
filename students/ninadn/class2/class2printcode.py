"""
Grid printer
"""

def horzline(grid_size,grid_count,border):
	if border == 1:
		for i in range (grid_count):
			line = ("+",end="")
			for j in range (grid_size):
				line = ("-",end="")
	else:
		for i in range (grid_count):
			line = ("|",end="")
			for j in range (grid_size):
				line =  (" ",end="") 
	return line

def print_grid(grid_size, grid_count):
	for i in range(grid_count):
		for j in range (grid_size):
			if j = 0 or grid_size:
				print horzline(grid_size,grid_count,1)
			else:
				print horzline(grid_size,grid_count,0)





def main():
	grid_count=int(input("How many grids: "))
	grid_size=int(input("Grid size: "))
	print_grid(grid_size, grid_count)

main()