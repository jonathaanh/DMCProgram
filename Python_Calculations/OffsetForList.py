from inputVariables import *

def OffsetForList(l_t, D, B_T):
	print("Offset for List")
	print() 

	print("l_T = " + str(l_t))
	print("depth = " + str(D))
	print("B_T = " + str(B_T))
	print()

	O_l = (l_t * D * CF_L)/ B_T
	print("O_l = (l_T * depth * CF_L)/ B_T")
	print(O_l)
	print()

if __name__ == "__main__":
	if v:
		OffsetForList(v.l_t, v.D, v.B_T)