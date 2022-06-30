import argparse

global CF_W, CF_L, CF_WP
CF_W = 2240
CF_L = 12
CF_WP = 0.001786

parser = argparse.ArgumentParser(description='Process some variables.')
parser.add_argument('--T_a', dest='T_a', type=float, help='')
parser.add_argument('--T_f', dest='T_f', type=float, help='')
parser.add_argument('--T_max', dest='T_max', type=float, help='')
parser.add_argument('--T_m', dest='T_m', type=float, help='')
parser.add_argument('--t_r', dest='t_r', type=float, help='')
parser.add_argument('--l_t', dest='l_t', type=float, help='')
parser.add_argument('--l_agl', dest='l_agl', type=float, help='')
parser.add_argument('--KG', dest='KG', type=float, help='')
parser.add_argument('--LCG', dest='LCG', type=float, help='')
parser.add_argument('--t', dest='t', type=float, help='')
parser.add_argument('--LOA', dest='LOA', type=float, help='')
parser.add_argument('--LBP', dest='LBP', type=float, help='')
parser.add_argument('--d_AP', dest='d_AP', type=float, help='')
parser.add_argument('--B', dest='B', type=float, help='')
parser.add_argument('--h_Prj', dest='h_Prj', type=float, help='')
parser.add_argument('--D', dest='D', type=float, help='')
parser.add_argument('--SBPL', dest='SBPL', type=float, help='')
parser.add_argument('--disp', dest='disp', type=float, help='')
parser.add_argument('--MCT', dest='MCT', type=float, help='')
parser.add_argument('--Im', dest='Im', type=float, help='')
parser.add_argument('--KM', dest='KM', type=float, help='')
parser.add_argument('--LCF', dest='LCF', type=float, help='')
parser.add_argument('--B_T', dest='B_T', type=float, help='')
parser.add_argument('--B_DClr', dest='B_DClr', type=float, help='')
parser.add_argument('--h_DClr', dest='h_DClr', type=float, help='')
parser.add_argument('--h_Clr', dest='h_Clr', type=float, help='')
parser.add_argument('--h_MLLW', dest='h_MLLW', type=float, help='')
parser.add_argument('--D_D', dest='D_D', type=float, help='')
parser.add_argument('--disp_max', dest='disp_max', type=float, help='')
parser.add_argument('--LL_max', dest='LL_max', type=float, help='')
parser.add_argument('--S_SA', dest='S_SA', type=float, help='')
parser.add_argument('--S_MC', dest='S_MC', type=float, help='')
parser.add_argument('--v_W', dest='v_W', type=float, help='')
parser.add_argument('--EAF', dest='EAF', type=float, help='')
parser.add_argument('--OHA', dest='OHA', type=float, help='')
parser.add_argument('--LK', dest='LK', type=float, help='')
parser.add_argument('--h_BL', dest='h_BL', type=float, help='')
parser.add_argument('--h_SB', dest='h_SB', type=float, help='')
parser.add_argument('--HB_SB', dest='HB_SB', type=float, help='')
parser.add_argument('--d_Sill', dest='d_Sill', type=float, help='')
parser.add_argument('--A_KB', dest='A_KB', type=float, help='')
parser.add_argument('--n_KB', dest='n_KB', type=float, help='')
parser.add_argument('--A_SB', dest='A_SB', type=float, help='')
parser.add_argument('--n_SB', dest='n_SB', type=float, help='')
parser.add_argument('--SternToSill', dest='SternToSill', type=float, help='')
parser.add_argument('--MatchTrimOfDockToShip', dest='MatchTrimOfDockToShip', type=float, help='')
parser.add_argument('--UseHaulingBlocks', dest='UseHaulingBlocks', type=float, help='')

parser.add_argument('--LKBearingLengths',dest='LKBearingLengths',type=float, help='' )
parser.add_argument('--HydrostaticsArrayTxt', dest='HydrostaticsArrayTxt',type =float, help='')
parser.add_argument('--WindLoadingArray', dest='WindLoadingArray',type =float, help='')

#calculated values
parser.add_argument('--R_Kn', dest='R_Kn',type =float, help='')
parser.add_argument('--h_E', dest='h_E',type =float, help='')


v,w= parser.parse_known_args()

