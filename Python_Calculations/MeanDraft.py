from inputVariables import *

def MeanDraft(T_a, T_f):

	print("Mean Draft")
	print()
	
	print("T_a = " + str(T_a))
	print("T_f = " + str(T_b))
	print()

	T_m = (T_a + T_f)/2
	print("(T_a + T_f)/2")
	print(T_m)
	print()

if __name__ == '__main__':
	if v:
		MeanDraft(v.T_a, v.T_f)