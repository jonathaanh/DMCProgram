from inputVariables import *


def KnuckleReaction(t_r, d_AP, LBP, LCF, OHA, LK, D, MCT, A_KB, S_SA):

	print("Knuckle Reaction")
	print()

	print("t_r = " + str(v.t_r))
	print("d_AP = " + str(v.d_AP))
	print("LBP = " + str(v.LBP))
	print("LCF = " + str(v.LCF))
	print("OHA = " + str(v.OHA))
	print("LK = " + str(v.LK))
	print("D = " + str(v.D))
	print("MCT = " + str(v.MCT))
	print("A_KB = " + str(v.A_KB))
	print("S_SA = " + str(v.S_SA))
	print()

	print("Knuckle Reaction Lever Arm")
	print()
	if(t_r > 0):
		X_Kn = d_AP + LBP/2 - LCF - OHA
		print("t_r > 0")
		print("Aft Knuckle: d_AP + LBP/2 - LCF - OHA")
		print(X_Kn)
	elif(t_r < 0):
		X_Kn = OHA + LK - d_AP - LBP/2 + LCF
		print("t_r < 0")
		print("Fwd Knuckle: OHA + LK - d_AP - LBP/2 + LCF")
		print(X_Kn)
	else:
		print("t_r = 0")
		print("No Knuckle: X_Kn = 0 & R_Kn = 0")

	print("Safety Factor")
	if(OHA < 1.5 * D):
		print("OHA < 1.5 * D")
		print("Small Overhang: 0.97")
		k = 0.97
	else:
		print("OHA >= 1.5 * D")
		print("Large Overhang: 0.94")
		k = 0.94
	print()

	print("Knuckle Reaction")
	print("R_Kn = (t_r x MCT x CF_L)/ k x X_Kn")
	R_Kn = (t_r * MCT * CF_L)/ k * X_Kn
	print(R_Kn)
	print()

	print("Knuckle Reaction Stress")
	print("S_Kn = (R_Kn x CF_W)/ A_KB")
	S_Kn = (R_Kn * CF_W)/ A_KB
	print(S_Kn)
	print()

	print("Knuckle Reaction Stress Check")
	print("S_Kn < S_SA")
	print(S_Kn)
	print()
	
	if(S_Kn < S_SA):
		print("Fail")
	else: 
		print("Pass")
	print()
	return(R_Kn)	

R_Kn = KnuckleReaction(v.t_r, v.d_AP, v.LBP, v.LCF, v.OHA, v.LK, v.D, v.MCT, v.A_KB, v.S_SA)