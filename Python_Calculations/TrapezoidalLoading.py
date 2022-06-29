from inputVariables import *

def TrapezoidalLoading(disp, LK, OHA, d_AP, LBP, LCG, LL_max):

	print("Trapezoidal Loading Approximation")
	print()
	
	print("disp = " + str(disp))
	print("LK = " + str(LK))
	print("OHA = " + str(OHA))
	print("d_AP = " + str(d_AP))
	print("LBP = " + str(LBP))
	print("LCG = " + str(LCG))
	print("LL_max = " + str(LL_max))
	print()

	print("Average Line Load")
	print("LL_avg = disp/LK")
	LL_avg = disp/LK
	print(LL_avg)
	
	print("Center of Gravity Eccentricity")
	print("e = OHA + LK/2 - d_AP - LBP/2 + LCG")
	e = OHA + LK/2 - d_AP - LBP/2 + LCG
	print(e)
	print()
	
	print("Differential Line Load")
	print("LL_dif = 6*disp*e/LK^2")
	LL_dif = 6*disp*e/LK**2
	print(LL_dif)
	print()

	print("Line Load Aft")
	print("LL_a = LL_avg + LL_dif")
	LL_a = LL_avg + LL_dif
	print(LL_a)
	print()

	print("Line Load Forward")
	print("LL_f = LL_avg - LL_dif")
	LL_f = LL_avg - LL_dif
	print(LL_f)
	print()

	print("Line Load Check")
	print("LL_max > LL_f & LL_a")
	if(LL_max > LL_f and LL_max > LL_a):
		print("Pass")
	else:
		print("Fail")
	print()

	print("Trapezoidal Slope")
	print("m = (LL_a - LL_f)/ LK")
	m = (LL_a - LL_f)/ LK
	print(m)


if __name__ == '__main__':
	if v:
		TrapezoidalLoading(v.disp, v.LK, v.OHA, v.d_AP, v.LBP, v.LCG, v.LL_max)