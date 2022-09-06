import numpy as np
import math
from Interpolation import Interpolate

def ListCalculation(T_m_0, List_0, KG_0, H_T_mArrayTxt, H_DispArrayTxt, H_KMArrayTxt, Sum_TankWeightChanges, Sum_TankVertMom, Sum_TankTransMom, Sum_OtherWeightChanges, Sum_OtherVertMom, Sum_OtherTransMom):

	print("<T>List Calculation")
	print(" ")

	H_T_mArray = np.array(H_T_mArrayTxt)
	H_DispArray = np.array(H_DispArrayTxt)
	H_KMArray = np.array(H_KMArrayTxt)
	Disp_0 = Interpolate("T_m_0", T_m_0, "T_m", H_T_mArray, "Disp", H_DispArray, "Disp_0")

	print("Compute Displacement")
	print("Disp_0 = " + str(Disp_0))
	print("Sum_TankWeightChanges = " + str(Sum_TankWeightChanges) + " (added: +  removed: -)")
	print("Sum_OtherWeightChanges = " + str(Sum_OtherWeightChanges) + " (added: +  removed: -)")
	print("Disp_1 = Disp_0 + Sum_TankWeightChanges + Sum_OtherWeightChanges")
	Disp_1 = Disp_0 + Sum_TankWeightChanges + Sum_OtherWeightChanges
	print("Disp_1 = " + str(Disp_1))
	print(" ")

	T_m_1 = Interpolate("Disp_0", Disp_0, "Disp", H_DispArray, "T_m", H_T_mArray, "T_m_1")
	KM_1 = Interpolate("Disp_0", Disp_0, "Disp", H_DispArray, "KM", H_KMArray, "KM_1")

	print("Compute new center of gravity KG_1")
	print("KG_0 = " + str(KG_0))
	print("Disp_0 = " + str(Disp_0))
	print("Disp_1 = " + str(Disp_1))
	print("Sum_TankVertMom = " + str(Sum_TankVertMom))
	print("Sum_OtherVertMom = " + str(Sum_OtherVertMom))
	print("KG_1 = (KG_0*Disp_0 + Sum_TankVertMom + Sum_OtherVertMom)/Disp_1")
	KG_1 = (KG_0*Disp_0 + Sum_TankVertMom + Sum_OtherVertMom)/Disp_1
	print("KG_1 = " + str(KG_1))
	print(" ")

	print("Compute new GM")
	print("KM_1 = " + str(KM_1))
	print("KG_1 = " + str(KG_1))
	print("GM_1 = KM_1 - KG_1")
	GM_1 = KM_1 - KG_1
	print("GM_1 = " + str(GM_1))
	print(" ")
	
	print("Compute new List")
	print("List_0 = " + str(List_0))
	print("GM_1 = " + str(GM_1))
	print("Disp_1 = " + str(Disp_1))
	print("Sum_TankTransMom = " + str(Sum_TankTransMom))
	print("Sum_OtherTransMom = " + str(Sum_OtherTransMom))
	print("List_1 = List_0 + (180/3.14159265359)*(Sum_TankTransMom+Sum_OtherTransMom)/(GM_1*Disp_1)")
	List_1 = List_0 + (180/math.pi)*(Sum_TankTransMom+Sum_OtherTransMom)/(GM_1*Disp_1)
	print("List_1 = " + str(List_1))
	print(" ")
	
	print("List Check")
	print("List_1 = " + str(List_1))	
	print("abs(List_1) <= 2")
	if(abs(List_1) <= 2):
		print("Pass")
	else:
		print("Fail")	
	print(" ")
	return T_m_1
	

if __name__ == "__main__":
	T_m_0 = 21.25
	List_0 = 1
	KG_0 = 24.69826
	H_T_mArrayTxt =  [15,16,17,18,19,20,21,22,23,24,25]
	H_DispArrayTxt = [5245,5775,6320,6890,7480,8090,8720,9350,10000,10650,11310]
	H_KMArrayTxt = [28.09,28.25,28.41,28.6,28.76,28.83,28.89,28.95,29.01,29.11,29.26]
	Sum_TankWeightChanges = -778.036
	Sum_TankVertMom = -5682.37
	Sum_TankTransMom = -500.938
	Sum_OtherWeightChanges = 22.67857
	Sum_OtherVertMom = 1643.032
	Sum_OtherTransMom = 0
	ListCalculation(T_m_0, List_0, KG_0, H_T_mArrayTxt, H_DispArrayTxt, H_KMArrayTxt, Sum_TankWeightChanges, Sum_TankVertMom, 
	Sum_TankTransMom, Sum_OtherWeightChanges, Sum_OtherVertMom, Sum_OtherTransMom)