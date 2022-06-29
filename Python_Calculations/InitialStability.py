from inputVariables import *

def InitialStability(KM, KG, UseHaulingBlocks):
	print("Initial Stability")
	print()

	print("KM = " + str(KM))
	print("KG  = " + str(KG))
	print()

	print("GM = KM - KG")
	GM = KM - KG
	print(GM)

	print("Stability Check")
	if(UseHaulingBlocks == 1):
		print("GM_Ld >= 1 ft (Hauling)")
		if(GM >= 1):
			print("Pass")
		else:
			print("Fail")
	else:
		print("GM_Ld >= 0.5 ft")
		if(GM >= 1):
			print("Pass")
		else:
			print("Fail")

if __name__ == "__main__":
	if v:
		InitialStability(v.KM, v.KG, v.UseHaulingBlocks)