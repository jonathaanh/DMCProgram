#from inputVariables import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def PumpingPlan(stops,touch, min_dock_draft,tank_to_dock_pontoon,pontoon_height,tank_pontoon_cap,tank_cap,
	max_dock_draft,max_tank_level,dock_draft_at_touch,dock_draft_fully_loaded, section_loading):

	#x and y points 
	DockWaterContained = [0, tank_to_dock_pontoon, tank_cap]
	DockDraft = [min_dock_draft,pontoon_height,max_dock_draft]
	TankWaterContained = [0, tank_pontoon_cap, tank_cap]
	TankLevel = [0,pontoon_height,max_tank_level]

	#interpolate points for correction curve
	dock_touch_water = np.interp(dock_draft_at_touch, DockDraft, DockWaterContained)
	dock_loaded_water = np.interp(dock_draft_fully_loaded, DockDraft, DockWaterContained) - section_loading
	final_dock_draft = np.interp(section_loading, DockWaterContained, DockDraft)

	#labels, title, and plotting points
	plt.figure(figsize=(15, 8), dpi=80)
	plt.xlabel('Weight of Contained Water(in Long Tons)')
	plt.ylabel('Draft of dock or Depth of Contained Water(in Feet)')
	plt.title('Pumping Plan')
	plt.plot(DockWaterContained, DockDraft, label="Dock Draft")
	plt.plot(TankWaterContained, TankLevel, label="Tank Level")

	#correction curve 
	#plt.plot([dock_touch_water,dock_loaded_water],[dock_draft_at_touch,dock_draft_fully_loaded], color='green')
	#plt.plot([dock_loaded_water, tank_to_dock_pontoon-section_loading],[dock_draft_fully_loaded, pontoon_height], color='green')
	#plt.plot([tank_to_dock_pontoon-section_loading, 0],[pontoon_height, final_dock_draft], color='green')
	CCx = [0,tank_to_dock_pontoon-section_loading,dock_loaded_water,dock_touch_water ]
	CCy = [final_dock_draft,pontoon_height, dock_draft_fully_loaded, dock_draft_at_touch ]
	plt.plot(CCx,CCy, label="Correction Curve")
	#legend
	plt.legend(loc='upper center')
	# for xy in zip(DockWaterContained, DockDraft):
	# 	plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data', horizontalalignment='right')
	# for xy in zip(TankWaterContained, TankLevel):
	# 	plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data', horizontalalignment='left')

	#plot stops
	outputArray = []
	i = 0
	#0 dock, 1 correction
	for stop in stops:
		if touch[i] == 0:
			x3 = np.interp(stop, DockDraft, DockWaterContained)
			plt.plot([0,x3],[stop,stop], color='red')
			y3 = np.interp(x3, TankWaterContained, TankLevel)
			plt.plot([x3,x3],[y3,stop], color = 'red')
			plt.plot([0,x3],[y3,y3], color = 'red')
			plt.annotate('%.3f' % stop, xy=(0,stop+1), textcoords='data', horizontalalignment='left')
			plt.annotate('%.3f' % y3, xy=(0,y3+1), textcoords='data', horizontalalignment='left')
			outputArray.append(y3)
		else:
			x3 = np.interp(stop, CCy, CCx)
			print(x3)
			plt.plot([0,x3],[stop,stop], color='red')
			y3 = np.interp(x3, TankWaterContained, TankLevel)
			plt.plot([x3,x3],[y3,stop], color = 'red')
			plt.plot([0,x3],[y3,y3], color = 'red')
			plt.annotate('%.3f' % stop, xy=(0,stop+1), textcoords='data', horizontalalignment='left')
			plt.annotate('%.3f' % y3, xy=(0,y3+1), textcoords='data', horizontalalignment='left')
			outputArray.append(y3)
		i = i + 1
	#Dock Draft vs Tank Levels table
	table = pd.DataFrame({"Dock Draft":stops, "Tank Levels":outputArray})
	print(table)
	plt.show()
	return outputArray

if __name__ == '__main__':	

	min_dock_draft = 5
	tank_to_dock_pontoon = 4000
	pontoon_height = 15
	tank_pontoon_cap = 4500
	tank_cap = 6000
	max_dock_draft = 50
	max_tank_level = 40
	stops = [40,20,18]
	touch = [0,1,0]

	dock_draft_at_touch = 40
	dock_draft_fully_loaded = 25
	section_loading = 1500


	PumpingPlan(stops, touch,min_dock_draft,tank_to_dock_pontoon,pontoon_height,tank_pontoon_cap,tank_cap,
	max_dock_draft,max_tank_level,dock_draft_at_touch,dock_draft_fully_loaded, section_loading)