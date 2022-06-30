

genericInput = "--T_a 15.5 --T_f 13.5 --t_r 2 --l_t -0.5 --l_agl -0.64 --KG 19 --LCG 15.6 --T_max 15.5 --T_m 14.5 --t 2 --LOA 451.86 --LBP 408 --d_AP 12.5 --B 47.1 --h_Prj 9.59 --D 30 --SBPL 15 --disp 3510 --MCT 740 --Im 32.5 --KM 22.5 --LCF 23.65 --B_DClr 96 --h_DClr 37.27 --h_MLLW 47.5 --D_D 16.83 --disp_max 29000 --LL_max 42 --S_SA 370 --S_MC 800 --v_W 110 --EAF 0.2 --OHA 86.75 --LK 267.42 --h_BL 8.5 --h_SB 5.09 --HB_SB 11.4 --d_Sill 448.08 --A_KB 588 --n_KB 39 --A_SB 324 --n_SB 39 --SternToSill 0 --MatchTrimOfDockToShip 1 --UseHaulingBlocks 1 --B_T 42 --h_Clr 1 --LKBearingLengths 1";

var spawn1 = require("child_process").spawn;
var process1 = spawn1('python3', ["./AverageBlockLoading.py", genericInput]);
process1.stdout.on('data', function (data) {
    console.log(data.toString());
});

var spawn2 = require("child_process").spawn;
var process2 = spawn2('python3', ["./Capacity.py", genericInput]);
process2.stdout.on('data', function (data) {
    console.log(data.toString());
});

var spawn3 = require("child_process").spawn;
var process3 = spawn3('python3', ["./DraftAtLanding.py", genericInput]);
process3.stdout.on('data', function (data) {
    console.log(data.toString());
});