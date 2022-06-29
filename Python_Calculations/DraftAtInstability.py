#from inputVariables import *
import numpy as np
import pandas as pd
from Interpolation import Interpolate

def DraftAtInstability(disp, KG, HydrostaticsArrayTxt, T_Ld, UseHaulingBlocks):

	print("Draft At Instability")
	print()

	print("disp = " + str(disp))
	print("KG = " + str(KG))
	print("UseHaulingBlocks = " + str(UseHaulingBlocks))
	print()

	print("Residual Buoyancy Moment per Selected Drafts ")
	print("M_RB(T_m) = disp(T_m) * KM(T_m)")
	HydrostaticsArray = np.array(eval(HydrostaticsArrayTxt))
	M_RB = HydrostaticsArray[1] * HydrostaticsArray[2]
	table = pd.DataFrame({"Mean Draft":HydrostaticsArray[0], "Displacement":HydrostaticsArray[1], 
	"Keel to Metacenter":HydrostaticsArray[2], "Residual Buoyancy Moment": M_RB})
	print(table)
	print()

	print("Required Righting Moment")
	print("M_R = disp x KG")
	M_R = disp * KG
	print(M_R)
	print()

	T_I = Interpolate("M_R", M_R, "M_RB(T_m)", M_RB, "T_m", HydrostaticsArray[0], "T_I")

	print("Stability Check")
	if(UseHaulingBlocks):
		print("T_I + 1 ft <= T_Ld")
		if(T_I + 1 <= T_Ld):
			print("Pass")
		else:
			print("Fail")
	else:
		print("T_I + 0.5 ft <= T_Ld")
		if(T_I + 0.5 <= T_Ld):
			print("Pass")
		else:
			print("Fail")
	
	
if __name__ == '__main__':
	#if v:
	HydrostaticsArrayTxt = "[15,14,13,12],[3655,3270,2900,2560],[22.35,22.5,22.65,22.8]"
	disp = 3510
	KG = 19
	UseHaulingBlocks = 1
	T_Ld = 14.04
	DraftAtInstability(disp, KG, HydrostaticsArrayTxt,T_Ld, UseHaulingBlocks)
	