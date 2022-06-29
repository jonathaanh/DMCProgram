#from inputVariables import *
import numpy as np
import pandas as pd
from Interpolation import Interpolate

def HydrostaticInterpolation(T_m, HydrostaticsArrayTxt):
	print("Hydrostatic Interpolation")
	print()

	print("Hydrostatics")
	HydrostaticsArray = np.array(eval(HydrostaticsArrayTxt))
	table = pd.DataFrame({"Mean Draft":HydrostaticsArray[0],"Disp":HydrostaticsArray[1],
	"MCT":HydrostaticsArray[2],"Im":HydrostaticsArray[3],"KM":HydrostaticsArray[4],"LCF":HydrostaticsArray[5]})
	print(table)
	print()

	print("Current Mean Draft = " + str(T_m))
	print()

	Interpolate("Current T_m", T_m, "T_m", HydrostaticsArray[0], "Disp", HydrostaticsArray[1], "Current Disp")
	Interpolate("Current T_m", T_m, "T_m", HydrostaticsArray[0], "MCT", HydrostaticsArray[2], "Current MCT")
	Interpolate("Current T_m", T_m, "T_m", HydrostaticsArray[0], "Im", HydrostaticsArray[3], "Current Im")
	Interpolate("Current T_m", T_m, "T_m", HydrostaticsArray[0], "KM", HydrostaticsArray[4], "Current KM")
	Interpolate("Current T_m", T_m, "T_m", HydrostaticsArray[0], "LCF", HydrostaticsArray[5], "Current LCF")

if __name__ == '__main__':
	T_m = 7.75
	HydrostaticsArrayTxt = "[4,5,6,7,8,9,10],[79.91,149.05,231.43,318.44,411.59,500.6,594.21],[32.1,63.1,72.7,77.4,80.6,83.9,86.4],[4.8,6.52,7.07,7.4,7.57,7.75,7.85],[18.37,17.72,17.39,17.06,16.71,16.08,15.42],[9.48,19.52,18.9,16.67,13.88,11.58,9.38]"
	#T_m = 14.5
	#HydrostaticsArrayTxt = "[15,14,13,12],[3655,3270,2900,2560],[766,720,650,585],[32.30,31.45,30.25,28.80],[22.35,22.5,22.65,22.8],[23.65,22.60,18.80,14.9]"
		#if v:
	HydrostaticInterpolation(T_m, HydrostaticsArrayTxt)