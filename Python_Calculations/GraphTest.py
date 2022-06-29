#from inputVariables import *
import matplotlib.pyplot as plt
import os

def MakeGraph(xPoints,yPoints):

	x = xPoints
	y = yPoints
  
	# plotting the points 
	plt.plot(x, y)
  
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
	plt.title('Graph Test')

	curr_dir = os.path.dirname(__file__)
	output_dir = os.path.join(curr_dir, 'Graphs/')
	sample_file_name = "graph1"
	print("@@@" +output_dir + sample_file_name)
	plt.savefig(output_dir + sample_file_name)
	plt.show()


if __name__ == '__main__':	
	xPoints = [1,2]
	yPoints = [2,4]
	MakeGraph(xPoints,yPoints)