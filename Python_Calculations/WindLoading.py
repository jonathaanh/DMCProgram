import numpy as np
import pandas as pd
from inputVariables import *

def WindLoading(v_W, disp, SBPL, HB_SB, n_SB, A_SB, S_MC, array):

	print("Wind Loading")
	print()

	print("Overturning Moment")
	newArray = np.array(eval(array))
	table = pd.DataFrame({"Sail Area": newArray[0], "Center height to the Keel": newArray[1] })
	M_A = 0
	for i in range(0,3):
		M_A = M_A + (newArray[0][i])*(newArray[1][i])
	print(table)
	print(M_A)
	print()

	print("Force of the Wind")
	print("F_W = CF_WP/1000 * (V_W)^2")
	F_W = CF_WP/1000 * v_W**2
	print(F_W)
	print()

	print("Overturning Moment")
	print("M_W = F_W x M_A")
	M_W = F_W * M_A
	print(M_W)
	print()

	print("Dead Load")
	print("L_D = disp x SBPL/(2x100)")
	L_D = disp * SBPL/(2*100)
	print(L_D)
	print()

	print("Applied Load onto Side Blocks")
	print("L_A = M_W/HB_SB + L_D")
	L_A = M_W/HB_SB + L_D
	print(L_A)
	print()

	print("Side Block Stress")
	print("S_SB = (L_A x CF_W)/(n_SB/2 x A_SB)")
	S_SB = (L_A * CF_W)/((n_SB/2) * A_SB)
	print(S_SB)
	print()

	print("Side Block Stress Check")
	print("S_SB < S_MC")
	if(S_SB < S_MC):
		print("Pass")
	else:
		print("Fail")


if __name__ == "__main__":
	WindLoadingArray = "([15068,2337,925],[19.9, 50.7,82.7])"
	WindLoading(v.v_W, v.disp, v.SBPL, v.HB_SB, v.n_SB, v.A_SB, v.S_MC, WindLoadingArray)

