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
	ax.set_xlim(0, 10)
	ax.set_ylim(0, 10)
  
	plt.xlabel('Length (feet)')
	plt.ylabel('LL (LT/ft)')
	plt.title('LL (LT/ft) vs Length (feet)')
	ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=True))

	LL_aX = [0, LK]
	LL_aY = [LL_a, LL_a]
	ax.plot(LL_aX, LL_aY, linestyle='dashed')
	ax.annotate("LL_a",(0,LL_a),ha='left')

	LL_fX = [0, f]
	LL_fY = [LL_f, LL_f]
	ax.plot(LL_fX, LL_fY, linestyle='dashed')
	ax.annotate("LL_f",(0,LL_f),ha='left')
		
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
	LK = 8
	LL_a = 9
	LL_f = 5
	f = 2
	x = [f,LK,LK, f]
	y = [0,0,LL_a, LL_f]
	MakeTrapezoid(x,y)