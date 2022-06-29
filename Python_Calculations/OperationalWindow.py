from inputVariables import *

def OperationalWindow(D_D, h_MLLW, h_Clr):
	print("Operational Window")
	print() 

	print("h_E = " + str(h_E))
	print("D_D = " + str(D_D))
	print("h_MLLW = " + str(h_MLLW))
	print("h_Clr = " + str(h_Clr))
	print()

	Td_m = float(h_E) + D_D + h_Clr - h_MLLW
	print("(h_E + D_D  + h_Clr) - h_MLLW")
	print(Td_m)
	print()

if __name__ == "__main__":
	if v:
		#take in calculated h_E value
		OperationalWindow(v.D_D, v.h_MLLW, v.h_Clr)