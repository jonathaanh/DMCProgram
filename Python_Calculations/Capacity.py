from inputVariables import *

def Capacity(disp, disp_max):
	print("Capacity")
	print()

	print("disp = " + str(disp))
	print("disp_max = " + str(disp_max))
	print()

	print("Maximum Displacement Check")
	print("disp < disp_max")
	if(disp < disp_max):
		print("Pass")
	else:
		print("Fail")
	print()


if __name__ == '__main__':
	if v:
		Capacity(v.disp, v.disp_max)