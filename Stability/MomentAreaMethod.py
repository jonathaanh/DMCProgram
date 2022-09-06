#from inputVariables import *

import numpy as np
import pandas as pd


def MomentAreaMethod(LK_sections, OHAArray, widthArray, d_AP, LBP, LCG, disp):

	print("Moment Area Method")
	print("d_AP = " +str(d_AP))
	print("LBP = "+ str(LBP))
	print("LCG = " + str(LCG))
	print("disp = " + str(disp))
	print(" ")

	print("Center of Area (Area Moment Average)")
	print("X = (Σi d(i) x A(i)) / Σi A(i)")
	AreaMoment = 0
	TotalBlockArea = 0
	for i in range(len(LK_sections)):
		AreaMoment = AreaMoment + (OHAArray[i]+i/2) * (LK_sections[i]*widthArray[i])
	for i in range(len(LK_sections)):
		TotalBlockArea = TotalBlockArea + (LK_sections[i]*widthArray[i])
	X = AreaMoment / TotalBlockArea
	print("X = "+ str(X))
	print(" ")

	print("Area Moment of Inertia")
	print("I = Σ((A(i) x LK(i)^2)/12 +A(i) x (d(i) - X)^2")
	I = 0
	for i in range(len(LK_sections)):
		I = I + ((LK_sections[i]*widthArray[i]) * (LK_sections[i])**2)/12 + (LK_sections[i]*widthArray[i]) * ((OHAArray[i]+i/2) - X)**2
	print("I = " + str(I))
	print(" ")

	print("Center of Gravity Eccentricity")
	print("e = X - d_AP - LBP/2 + LCG")
	e = X - d_AP - LBP/2 + LCG
	print("e = " + str(e))
	print(" ")
	
	print("Line Load")
	SectionEndsToX = []
	LineLoad = []
	for i in range(len(LK_sections)):
		SectionEndsToX.append([X-OHAArray[i],X-(OHAArray[i]+LK_sections[i])])
		LineLoad.append(disp*(widthArray[i])*((1/TotalBlockArea)+e*np.array(SectionEndsToX)/I))
	table = pd.DataFrame({"A/E, F/E": LineLoad})
	print(table)
	print(" ")

if __name__ == '__main__':
	disp = 3510
	LK_sections = [267.42]
	OHAArray = [86.75]
	widthArray = [12]
	d_AP = 12.5
	LBP  = 408
	LCG = 15.6
	LL_max = 42
	MomentAreaMethod(LK_sections, OHAArray, widthArray, d_AP, LBP, LCG, disp)