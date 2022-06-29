from inputVariables import *

def AverageBlockLoading(A_KB, n_KB, A_SB, n_SB, disp, S_SA):

	print("Average Block Loading")
	print()
	
	print("A_KB = " + str(A_KB))
	print("n_KB = " + str(n_KB))
	print("A_SB = " + str(A_SB))
	print("A_SB = " + str(n_SB))
	print("disp = " + str(disp))
	print("S_SA = " + str(S_SA))
	print()

	print("Total Keel Block Bearing Area")
	A_KBt = A_KB * n_KB
	print("A_KBt = A_KB * n_KB")
	print(A_KBt)
	print()

	print("Total Side Block Bearing Area")
	A_SBt = (A_SB) * (n_SB)
	print("A_SBt = A_SB * n_SB")
	print(A_SBt)
	print()

	print("Total Block Bearing Area")
	A_Bt = A_KBt + A_SBt
	print("A_Bt = A_KBt + A_SBt")
	print(A_Bt)
	print()

	print("Block Stress")
	S_B = ((disp) * CF_W) / A_Bt 
	print("S_B = (disp * CF_W) / A_Bt ")
	print(S_B)
	print()

	print("Block Stress Check")
	print("S_B < S_SA")
	if(S_B < (S_SA)):
		print("Pass")
	else:
		print("Fail")
	print()

if __name__ == '__main__':
	if v:
		AverageBlockLoading(v.A_KB, v.n_KB, v.A_SB, v.n_SB, v.disp, v.S_SA)