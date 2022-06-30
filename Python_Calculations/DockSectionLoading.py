from inputVariables import *
import numpy as np
import pandas as pd

def DockSectionLoading(LKBearingLengthsTxt, LL_a, LL_f,SternToStill):

	#These might be inputs later
	LKBearingLengths = np.array(eval(LKBearingLengthsTxt))
	#LKBearingLengths = np.LKBearingLengths(eval(sys.argv[1]))
	Sections = ["A", "B", "C", "D", "E", "F", "G", "H"]
	bulk = ["A/Sill", "B/A", "C/B", "D/C", "E/D", "F/E", "G/F", "H/G", "End/H"]

	print("Dock Section Loading")
	print()
	print("LL_a = " + str(LL_a))
	print("LL_f = " + str(LL_f))
	print("m = " + str(m))
	print("SternToStill = " + str(SternToStill))
	print()

	print("LK Bearing Lengths")
	table = pd.DataFrame({"Sections":Sections, "Bearing Lengths":LKBearingLengths})
	print(table)
	print()

	print("Section Differentials = m x LK Bearing Lenghts")
	SectionDifferentials = LKBearingLengths * m
	table = pd.DataFrame({"Sections":Sections, "Bearing Lengths":SectionDifferentials})
	print(table)
	print()

	print("Bulkhead Line Loads")
	size = np.size(LKBearingLengths)+1
	BulkheadLL = np.zeros(size)

	#Find index of left-most nonzero value
	first = min(np.nonzero(LKBearingLengths)[0])
	#plus one because bulkhead line loads is longer by 1
	last = max(np.nonzero(LKBearingLengths)[0]) + 1

	if (SternToStill==1):
		BulkheadLL[first] = LL_a
		for i in range(first,last):
			BulkheadLL[i] = BulkheadLL[i]-SectionDifferentials[i]
	else:
		BulkheadLL[first] = LL_f
		for i in range(first,last):
			BulkheadLL[i+1] = BulkheadLL[i]+SectionDifferentials[i]
		
	table = pd.DataFrame({"Bulkheads":bulk, "Line Loads":BulkheadLL})
	print(table)
	print()


	print("Averaged Bulkhead Line Loads")
	AveragedBulkheadLL = np.zeros(len(Sections))
	for i in range(first,last):
		AveragedBulkheadLL[i] = (BulkheadLL[i]+BulkheadLL[i+1])/2
		#SectionDifferentials.append((table.iloc[i]['Line Loads']+table.iloc[i+1]['Line Loads'])/2)
	table = pd.DataFrame({"Bulkheads":Sections, "Line Loads":AveragedBulkheadLL})
	print(table)
	print()

	print("Section Loading = Averaged Bulkhead Line Loads x LK Bearing Lengths")
	SectionLoading = []
	SectionLoading = LKBearingLengths*AveragedBulkheadLL
	#for i in range(0,8):
	#	SectionDifferentials.append(table.iloc[i]['Line Loads']*LKBearingLengths[i])
	table = pd.DataFrame({"Bulkheads":Sections, "Line Loads":SectionLoading})
	print(table)
	print()

if __name__ == '__main__':
	if v:
		
		LL_a = 18.89
		LL_f = 7.39
		""""
		LKBearingLengthsTxt = "[0,0,82.17,96,89.33,0,0,0]"
		LK = 267.42
		m = (LL_a-LL_f)/LK
		SternToStill = 0
		"""
		#trapezoidal loading approx import LL_a, LL_F
		m = (LL_a-LL_f)/v.LK
		DockSectionLoading(v.LKBearingLengths, m, LL_a, LL_f, v.SternToStill)
	