#from inputVariables import *
import numpy as np
import pandas as pd
from Interpolation import Interpolate

def DraftAtInstabilityPlusKnuckle(d_AP, LBP, OHA, disp, KG, T_mArray, dispArray, MCTArray, 
ImArray, KMArray, LCFArray, T_Ld, UseHaulingBlocks, t_r, k):

	print("<T>Draft At Instability")
	print(" ")

	print("disp = " + str(disp))
	print("KG = " + str(KG))
	print("UseHaulingBlocks = " + str(UseHaulingBlocks))
	print("d_AP = " + str(d_AP))
	print("LBP = " + str(LBP))
	print("OHA = " + str(OHA))
	print("disp = " + str(disp))
	print("KG = " + str(KG))
	print("T_Ld = " + str(d_AP))
	print("t_r = " + str(t_r))
	print("k = " + str(k))
	print(" ")

	print("Partial Knuckle Reaction Lever Arm(Adt Knuckle)")
	print("B_Kn = d_AP + LBP/2 - OHA")
	B_Kn = d_AP + LBP/2 - OHA
	print("B_Kn = " + str(B_Kn))
	print(" ")

	print("Knuckle Reaction Lever Arm per Selected Drafts(Aft Knuckle)")
	print("X_Kn(T_m) = B_Kn - LCF(T_m)")
	B_KnArray = []
	for x in range(len(LCFArray)):
		B_KnArray.append(B_Kn)
	X_Kn = np.subtract(B_KnArray,LCFArray)
	table = pd.DataFrame({"Mean Draft":T_mArray, "Partial Knuckle Reaction Lever Arm":B_KnArray, 
	"Longitudinal Center of Floatation":LCFArray, "Knuckle Reaction Lever Arm": X_Kn})
	print(table)
	print(" ")

	print("Knuckle Reaction per Selected Drafts")
	print("R_Kn(T_m = (t_r x MCT x CF_L) / (k x X_kn(T_m))")
	CF_L = 12
	R_KnArray = (t_r * np.array(MCTArray) * CF_L)/ k * np.array(X_Kn)
	table = pd.DataFrame({"Mean Draft":T_mArray, "Relative Trim":t_r, 
	"Moment to Change Trim":MCTArray, "Length Conversion": CF_L, "safety factor": k, "Knuckle Recation Lever Arm": X_Kn, "Knuckle Reaction": R_KnArray})
	print(table)
	print(" ")


	print("Residual Buoyancy Moment per Selected Drafts ")
	print("M_RB(T_m) = (disp(T_m) - R_Kn(T_m)) * KM(T_m)")
	M_RB = (dispArray - R_KnArray) * KMArray
	table = pd.DataFrame({"Mean Draft":T_mArray, "Displacement":dispArray, 
	"Knuckle Reaction":R_KnArray, "Keel to Metacenter": KMArray, "Residual Buoyancy Moment": M_RB})
	print(table)
	print(" ")

	print("Required Righting Moment")
	print("M_R = disp x KG")
	M_R = disp * KG
	print("M_R = " + str(M_R))
	print(" ")

	T_I = Interpolate("M_R", M_R, "M_RB(T_m)", M_RB, "T_m", T_mArray, "T_I")

	print("Stability Check")
	if(UseHaulingBlocks):
		print("T_I <= T_Ld - 1 ft | 0.3 m ")
		if(T_I + 1 <= T_Ld):
			print("Pass")
		else:
			print("Fail")
	else:
		print("T_I <= T_Ld - 0.5 ft | 0.15 m ")
		if(T_I + 0.5 <= T_Ld):
			print("Pass")
		else:
			print("Fail")
	print(" ")
	
if __name__ == '__main__':
	#if v:
	T_mArray= [15,14,13,12]
	dispArray = [3655,3270,2900,2560]
	MCTArray = [766,720,650,585]
	ImArray = [32.30,31.45,30.25,28.80]
	KMArray = [22.35,22.5,22.65,22.8]
	LCFArray = [23.65,22.60,18.80,14.9]
	disp = 3510
	KG = 19
	UseHaulingBlocks = 1
	T_Ld = 14.04
	d_AP = 12.5
	LBP = 408
	OHA = 86.75
	t_r = 2
	k = 0.94
	DraftAtInstabilityPlusKnuckle(d_AP, LBP, OHA, disp, KG, T_mArray, dispArray, MCTArray, 
ImArray, KMArray, LCFArray, T_Ld, UseHaulingBlocks, t_r, k)
	