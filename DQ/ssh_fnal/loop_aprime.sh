#!/usr/bin/bash
cd /seaquest/users/dwong/mye1039/e1039-core/DarkQuest/e1039-analysis/SimHits/
source setup_mye1039.sh
cd macro

input_directory="/seaquest/users/yfeng/DarkQuest/DarkQuest/lhe/output/displaced_Aprime_Electrons/"
output_directory="/seaquest/users/dwong/Aee/"

for input_file in "$input_directory"/*.txt; do
    input_file_name=$(basename "$input_file" .txt)
    output_file_name="${input_file_name}_withbkg.root"
    
    root -b -q "RecoE1039Sim.C(1000, 1, 0, -300., true, true, false, '$input_file_name', '$input_directory', '$output_file_name', '$output_directory','/pnfs/e1039/persistent/users/apun/bkg_study/e1039pythiaGen_26Oct21/10_bkge1039_pythia_wshielding_100M.root', 0)"
done

cd