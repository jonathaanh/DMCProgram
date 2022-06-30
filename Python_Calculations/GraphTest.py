#from inputVariables import *
from tkinter.messagebox import YES
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def MakeGraph(xPoints,yPoints):

	x = xPoints
	y = yPoints
  
	# plotting the points 
	plt.plot(x, y)
  
	plt.xlabel('Time (hours)')
	plt.ylabel('Tide Height (ft)')
	plt.title('Quarter-Ten Tidal Curve')
		
	curr_dir = os.path.dirname(__file__)
	output_dir = os.path.join(curr_dir, 'Graphs/')
	sample_file_name = "graph1"


	print("@@@" +output_dir + sample_file_name)
	plt.savefig(output_dir + sample_file_name)
	plt.show()

def MakeTrapezoid(x,y):

	fig = plt.figure()
	ax = fig.add_subplot(111, aspect='equal')
  
	plt.xlabel('Y-axis')
	plt.ylabel('X-axis')
	plt.title('Title')

	ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False))

		
	curr_dir = os.path.dirname(__file__)
	output_dir = os.path.join(curr_dir, 'Graphs/')
	sample_file_name = "graph1"


	print("@@@" +output_dir + sample_file_name)
	plt.savefig(output_dir + sample_file_name)
	plt.show()

if __name__ == '__main__':	
	#time = ["2200","0500","1100"]
	#tide = [-1,6,1]
	#MakeGraph(time,tide)
	LK = 10
	LL_a = 10
	LL_f = 3
	x = [0,LK,0, LK]
	y = [0,0,LL_f, LL_a]
	MakeTrapezoid(x,y)