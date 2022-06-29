import numpy as np
import pandas as pd

def Interpolate(InputLabel, InputValue, InputArrayLabel, InputArrayTxt, OutputArrayLabel, OutputArrayTxt, OutputLabel):

	InputArray = np.array(InputArrayTxt)
	OutputArray = np.array(OutputArrayTxt)

	#print("Interpolate")
	#print()

	#print(str(InputLabel) + " = " + str(InputValue))
	#table = pd.DataFrame({InputArrayLabel:InputArray, OutputArrayLabel:OutputArray})
	#print(table)
	#print()
	
	index1 = (np.abs(InputArray-InputValue)).argmin()
	InputArrayNextSmallest = np.delete(InputArray, index1)
	index2 = (np.abs(InputArrayNextSmallest-InputValue)).argmin()
	if (index2>=index1):
		index2 = index2 + 1
	print("Interpolation Setup")
	table = pd.DataFrame({InputArrayLabel:[InputArray[index1],InputArray[index2]], OutputArrayLabel:[OutputArray[index1],OutputArray[index2]]})
	print(table)
	print()

	print("Interpolation")
	OutputValue = (InputValue-InputArray[index1])*(OutputArray[index2]-OutputArray[index1])/(InputArray[index2]-InputArray[index1])+OutputArray[index1]
	print("("+InputLabel+"-"+InputArrayLabel+"(0))*("+OutputArrayLabel+"(1)-"+OutputArrayLabel+"(0))/("+InputArrayLabel+"(1)-"+InputArrayLabel+"(0))+"+OutputArrayLabel+"(0)")
	print(OutputLabel + " = " + str(OutputValue))
	print()

	return(OutputValue)

#if __name__ == '__main__':
	#Interpolate("M_R", 66690, "M_RB(T_m)", "[81689,73575,65685,58368]", "T_m", "[15,14,13,12]", "T_I")
	#Interpolate(InputLabel, InputValue, InputArrayLabel, InputArrayTxt, OutputArrayLabel, OutputArrayTxt, OutputLabel)