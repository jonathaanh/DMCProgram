from inputVariables import *

def TrimOfBlocks(LBP, t_Bagl):

	print("Trim of the Blocks")
	print()
	
	print("LBP = " + str(LBP))
	print("t_Bagl = " + str(t_Bagl))
	print()

	t_B = LBP*tan(t_Bagl)
	print("t_B = LBP*tan(t_Bagl)")
	print(t_B)
	print()

if __name__ == '__main__':
	if v:
		TrimOfBlocks(v.LBP, v.t_Bagl)