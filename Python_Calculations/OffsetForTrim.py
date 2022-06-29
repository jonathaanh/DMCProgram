from inputVariables import *

def OffsetForTrim(t_r, D, LBP):
	print("Offset for Trim")
	print() 

	print("LBP = " + str(LBP))
	print("t_r = " + str(t_r))
	print("depth = " + str(D))
	print()

	O_t = (t_r * D * CF_L)/ LBP
	print("O_t = (t_r * depth * CF_L)/ LBP")
	print(O_t)
	print()

if __name__ == "__main__":
	if v:
		OffsetForTrim(v.t_r, v.D, v.LBP)