from inputVariables import *

def SeismicBlockLoading(disp, KG, EAF, SBPL, HB_SB, n_SB, A_SB, S_MC):
	print("Seismic Block Loading")
	print()

	print("disp = " + str(disp))
	print("KG = " + str(KG))
	print("EAF = " + str(EAF))
	print("SBPL = " + str(SBPL))
	print("HB_SB = " + str(HB_SB))
	print("n_SB = " + str(n_SB))
	print("A_SB = " + str(A_SB))
	print("S_MC = " + str(S_MC))
	print()


	print("Earthquake Overturning Movement")
	print("M_E = EAF x disp x KG")
	M_E = EAF*disp*KG
	print(M_E)
	print()

	print("Dead Load")
	print("L_D = disp * SBPL/(2*100)")
	L_D = disp * SBPL/(2*100)
	print(L_D)
	print()

	print("Applied Load onto Side Blocks")
	print("L_A = M_E/HB_SB + L_D")
	L_A = M_E/HB_SB + L_D
	print(L_A)
	print()

	print("Side Block Stress")
	print("S_SB = (L_A * CF_W)/(n_SB/2*A_SB)")
	S_SB = (L_A * CF_W)/(n_SB/2*A_SB)
	print(S_SB)
	print()

	print("Side Block Stress Check")
	print("S_SB < S_MC")
	if(S_SB < S_MC):
		print("Pass")
	else:
		print("Fail")
	print()



if __name__ == "__main__":
	if v:
		SeismicBlockLoading(v.disp, v.KG, v.EAF, v.SBPL, v.HB_SB, v.n_SB, v.A_SB, v.S_MC)