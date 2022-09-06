import numpy as np
import pandas as pd
from inputVariables import *

def WindLoading(v_W, disp, SBPL, HB_SB, n_SB, A_SB, S_MC, SailAreaArrayTxt):

	print("Wind Loading")
	print()

	print("Overturning Moment")
	SailAreaArray = np.array(eval([SailAreaArrayTxt[1],SailAreaArrayTxt[2]]))
	table = pd.DataFrame({"Item":SailAreaArrayTxt[0],"Sail Area": SailAreaArray[1], "Center height to the Keel": SailAreaArray[2] })
	M_A = 0
	for i in range(0,3):
		M_A = M_A + (SailAreaArray[1][i])*(SailAreaArray[2][i])
	print(table)
	print("M_A = " + str(M_A))
	print()

	print("Force of the Wind")
	print("F_W = CF_WP/1000 * (V_W)^2")
	F_W = CF_WP/1000 * v_W**2
	print("F_W = " + str(F_W))
	print()

	print("Overturning Moment")
	print("M_W = F_W x M_A")
	M_W = F_W * M_A
	print("M_W = " + str(M_W))
	print()

	print("Dead Load")
	print("L_D = disp x SBPL/(2x100)")
	L_D = disp * SBPL/(2*100)
	print("L_D = " + str(L_D))
	print()

	print("Applied Load onto Side Blocks")
	print("L_A = M_W/HB_SB + L_D")
	L_A = M_W/HB_SB + L_D
	print("L_A = " + str(L_A))
	print()

	print("Side Block Stress")
	print("S_SB = (L_A x CF_W)/(n_SB/2 x A_SB)")
	S_SB = (L_A * CF_W)/((n_SB/2) * A_SB)
	print("S_SB = " + str(S_SB))
	print()

	print("Side Block Stress Check")
	print("S_SB < S_MC")
	if(S_SB < S_MC):
		print("Pass")
	else:
		print("Fail")


if __name__ == "__main__":
	SailAreaArrayTxt = "[Hull,Deck house,Mast],[15068,2337,925],[19.9, 50.7,82.7]"
	WindLoading(v.v_W, v.disp, v.SBPL, v.HB_SB, v.n_SB, v.A_SB, v.S_MC, SailAreaArrayTxt)

