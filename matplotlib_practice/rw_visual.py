import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	rw = RandomWalk(20000)
	rw.fill_walk()
	
	plt.figure(dpi = 128, figsize=(10,6))
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor = 'none', s=5)

	plt.scatter(0, 0, c = 'blue', edgecolors = 'none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors = 'none', s=100)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)	
	plt.show()

	keep_running = raw_input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
