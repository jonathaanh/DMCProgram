import pandas as pd

def OperationalStopsSummary(T_m, h_E, h_BL, T_max, h_Clr, T_Ld, D_D):
	print("Operational Stops Summary")
	stops = ["Stop 1", "Stop 2", "Stop 3", "", "", "Stop 4", "Stop 5"]
	description = ["Before Operation", "Min Clearance to Enter", "Alignment Before Touching",
	"Ship Touches Down", "Ship Lands", "Checking After Landing", "After Operation"]
	ship_draft = [T_m, T_m, T_m, T_m, T_Ld, T_Ld - h_Clr, ""]
	inside_dock_draft = ["", h_E, h_BL+T_max+h_Clr, h_BL +T_max, h_BL + T_Ld, h_BL+T_Ld-h_Clr, ""]
	outside_dock_draft = [D_D-h_Clr, D_D+h_E, D_D+h_Clr+h_BL+T_max, D_D+h_BL+T_max, D_D+h_BL+T_Ld,
	D_D+h_BL+T_Ld-h_Clr, D_D-h_Clr]
	table = pd.DataFrame({"Stops":stops, "Description":description, "Ship Draft":ship_draft, 
	"Inside Dock Draft":inside_dock_draft, "Outside Dock Draft":outside_dock_draft})
	print(table)
	print(" ")
	stops = [outside_dock_draft[0], outside_dock_draft[1],outside_dock_draft[2], 
	outside_dock_draft[5], outside_dock_draft[6]]
	touching = [0,0,1,1,1]
	print([stops,touching,outside_dock_draft[3]])
	return [stops,touching,outside_dock_draft[3]]

if __name__ == "__main__":
	T_m = 14.5
	h_E = 34.59
	h_BL = 8.5
	T_Ld = 14.04
	T_max = 15.5
	h_Clr = 1.00
	D_D = 16.83
	OperationalStopsSummary(T_m, h_E, h_BL, T_max, h_Clr, T_Ld, D_D)