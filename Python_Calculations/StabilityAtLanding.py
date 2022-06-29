from inputVariables import *

def StabilityAtLanding(disp, KM, KG, UseHaulingBlocks):
	print("Stability at Landing")
	print()

	print("disp = " + str(disp))
	print("KM = " + str(KM))
	print("KG = " + str(KG))
	print("R_Kn = " + str(R_Kn))
	print("UseHaulingBlocks = " + str(UseHaulingBlocks))
	print()

	print("GM_Ld = KM - (disp*KG)/(disp-R_Kn)")
	GM_Ld = KM - (disp*KG)/(disp-R_Kn)
	print(GM_Ld)
	print()

	print("Stability Check")
	if(UseHaulingBlocks == 1):
		print("GM_Ld >= 1 ft (Hauling)")
		if(GM_Ld >=1):
			print("Pass")
		else:
			print("Fail")
	else:
		print("GM_Ld >= 0.5 ft")
		if(GM_Ld >=1):
			print("Pass")
		else:
			print("Fail")


if __name__ == '__main__':
	if v:
		#take in caluclated R_Kn
		StabilityAtLanding(v.disp, v.KM, v.KG, v.UseHaulingBlocks)