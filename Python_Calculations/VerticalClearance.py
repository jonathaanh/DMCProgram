from inputVariables import *

h_E = 0
def VerticalClearance(T_max, h_Prj,h_Clr,h_SB, h_BL):
	print("Vertical Clearance")
	print() 

	print("T_max = " + str(T_max))
	print("h_Prj = " + str(h_Prj))
	print("h_Clr = " + str(h_Clr))
	print("h_SB = " + str(h_SB))
	print("h_BL = " + str(h_BL))
	print()

	h_E = T_max + h_Prj + h_Clr + h_SB + h_BL
	print("h_E = T_max + h_Prj + h_Clr + h_SB + h_BL")
	print(h_E)
	print()
	return h_E

h_E = VerticalClearance(v.T_max, v.h_Prj,v.h_Clr,v.h_SB, v.h_BL)