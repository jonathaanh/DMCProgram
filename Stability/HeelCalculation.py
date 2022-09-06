#from inputVariables import *
from Interpolation import Interpolate
import math
import pandas as pd

def HeelCalculation(LBP, Sum_Sail_Area, M_A, T_M_1, v_W, angles, Disp_1, GZ_Disp_array, GZ_per_angle, KG_1, KG_for_cross_curve, List):
	#M_A - Sum of Area Lever Arm
	#T_M_1 - Mean Draft 1
	print("<T>Heel Calculation")
	print(" ")
	
	print("T_M_1 = " + str(T_M_1))
	print("LBP = " + str(LBP))
	print("Sum_Sail_Area = " + str(Sum_Sail_Area))
	print("M_A = " + str(M_A))
	print("v_W = " + str(v_W))
	print("Disp_1 = " + str(Disp_1))
	print("GZ_Disp_array = " + str(GZ_Disp_array))
	print("GZ_per_angle = " + str(GZ_per_angle))
	print("KG_1 = "+ str(KG_1))
	print("KG_for_cross_curve = " +str(KG_for_cross_curve))
	print("List = " + str(List))
	print(" ")

	print("Compute Effective Seal Area")
	Eff_Sail_Area = Sum_Sail_Area - T_M_1 * LBP
	print("Eff_Sail_Area = Sum_Sail_Area - T_M_1 * LBP")
	print("Eff_Sail_Area = " + str(Eff_Sail_Area))
	print(" ")

	print("Compute Wind Lever Arm")
	Wind_Lever_Arm=((M_A)-(T_M_1*LBP)*(0.5*T_M_1))/Eff_Sail_Area - 0.5*T_M_1 
	print("Wind_Lever_Arm=((M_A)-(T_M_1*LBP)(.5*T_M_1))/Eff_Sail_Area - 0.5*T_M_1")
	print("Wind_Lever_Arm = " + str(Wind_Lever_Arm))
	print(" ")

	print("Compute Wind Overturning Moment per Angle")
	print("0.004*(v_W^ 2)*cos(angle)*Wind_Lever_Arm*cos(angle)*Eff_Sail_Area")
	Moment = []
	i = 0
	for angle in angles:
		radians = angle * math.pi / 180
		Moment.append(0.004*math.pow(v_W, 2)*math.cos(radians)*Wind_Lever_Arm*math.cos(radians)*Eff_Sail_Area)
		i = i + 1
	table = pd.DataFrame({"Angle[deg]":angles,"Moment[ft*lb]":Moment})
	print(table)
	print(" ")

	print("Interpolate new Displacement, per each Angle in the GZ Cross Curves of Stability"+ 
	" table to find GZ per Angle of Displacement")
	i = 0
	GZ__per_angle_at_Disp_1 = []
	for angle in angles:
		GZ__per_angle_at_Disp_1.append(Interpolate("Disp_1", Disp_1, "Disp", GZ_Disp_array, "GZ_per_angle", GZ_per_angle[i], "GZ__per_angle_at_Disp_1"))
		i = i+1
	table = pd.DataFrame({"Angle[deg]":angles,"GZ[ft]":GZ__per_angle_at_Disp_1})
	print(table)
	print(" ")

	print("Compute Corrected GZ per Angle at Displacement")
	i = 0
	Corrected_GZ_Per_Angle_At_Disp_1 = []
	for angle in angles:
		radian = angle *math.pi/180
		Corrected_GZ_Per_Angle_At_Disp_1.append(GZ__per_angle_at_Disp_1[i] - (KG_1-KG_for_cross_curve)*math.sin(radian))
		i = i + 1
	table = pd.DataFrame({"Angle[deg]":angles,"GZ[ft]":Corrected_GZ_Per_Angle_At_Disp_1})
	print(table)
	print(" ")

	print("Computing Righting Moment per Angle")
	i = 0
	Righting_Moment_per_Angle = []
	for angle in angles:
		Righting_Moment_per_Angle.append(Corrected_GZ_Per_Angle_At_Disp_1[i]*Disp_1*2240)
		i = i + 1
	table = pd.DataFrame({"Angle[deg]":angles,"Moment[ft*lb]":Righting_Moment_per_Angle})
	print(table)
	print(" ")
"""
	print("Computer Heel_0")
	i = 0
	X_3 = []
	for angle in angles :
		X_3[i] = Interpolate("Disp_1", Disp_1, "Righting Moment", Righting_Moment_per_Angle, "Wind Overturning Moment", 
		Wind_Overturning_Moment[angle], "X_3")
		i = i+1
	table = pd.DataFrame({"X_3[deg]":angles,"Heel[deg]":X_3})
	print(table)
	print(" ")

	print("Computer Heel_1")
	Heel_1 = List + Heel_0
	print("Heel_1 = List + Heel_0")
	print("Heel_1 = " + str(Heel_1))
	print("")

"""

if __name__ == "__main__":
	LBP= 471
	T_M_1  =20.04002
	Sum_Sail_Area = 30069.53
	M_A = 1045218
	v_W = 60
	angles = [10,15,20,30,40,45,50,55,60]
	Disp_1 = 8121.892
	GZ_Disp_array = [6500,7000,7500,8000,8500,9000,9500]
	GZ_per_angle = [[0.8,0.8,0.8,0.8,0.8,0.9,0.9],
					[1.1,1.2,1.2,1.2,1.3,1.3,1.3],
					[1.5,1.6,1.6,1.7,1.7,1.8,1.8],
					[2.4,2.5,2.6,2.7,2.8,2.8,2.9],
					[3.6,3.7,3.9,4,4,4.1,4.1],
					[4.3,4.3,4.4,4.4,4.4,4.4,4.3],
					[4.6,4.6,4.6,4.5,4.5,4.4,4.3],
					[4.7,4.6,4.5,4.4,4.3,4.2,4.1],
					[4.6,4.4,4.2,4,3.8,3.6,3.5]]
	KG_1 = 26.49792
	KG_for_cross_curve = 24.07
	List = 0.469697
	HeelCalculation(LBP, Sum_Sail_Area, M_A, T_M_1, v_W, angles, Disp_1, GZ_Disp_array, GZ_per_angle, KG_1, KG_for_cross_curve, List)
