from inputVariables import *

def TrimOfBlocks(t, t_B):

	print("Relative Trim")
	print()
	
	print("t = " + str(t))
	print("t_B = " + str(t_B))
	print()

	t_r = t-t_B
	print("t_r = t-t_B")
	print(t_r)
	print()

if __name__ == '__main__':
	if v:
		TrimOfBlocks(v.t, v.t_B)