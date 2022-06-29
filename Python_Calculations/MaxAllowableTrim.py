from inputVariables import *

def MaxAllowableTrim(LBP,t):
	print("Maximum Allowable Trim")
	print("LBP = " + str(LBP))
	print("t = " + str(t))
	t_max = LBP/100
	print("t_max = LBP/100")
	print()

	print("Maximum Trim Check")
	print("|t| < t_max")
	if(t< t_max):
		print("Pass")
	else: 
		print("Fail")
	print()

if __name__ == "__main__":
	if v:
		MaxAllowableTrim(v.LBP, v.t)