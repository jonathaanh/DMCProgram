from inputVariables import *

def DraftAtLanding(T_m, Im):
	print("Draft At Landing")
	print() 

	print("T_m = " + str(T_m))
	print("R_Kn = " + str(R_Kn))
	print("Im = " + str(Im))
	print()

	T_Ld = T_m - (R_Kn/ (Im * CF_L))
	print("T_Ld = T_m - (R_Kn/ (Im * CF_L))")
	print(T_Ld)
	print()

if __name__ == "__main__":
	if v:
		DraftAtLanding(v.T_m, v.Im)