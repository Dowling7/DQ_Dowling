#!/usr/bin/bash
cd /seaquest/users/dwong/mye1039/e1039-core/DarkQuest/e1039-analysis/SimHits/
source setup_mye1039.sh
cd macro
#macro is to analyze simulation in SpinQuest
#1. number of events
#2. simulation type
#isim = 1 to run on Aprime to dimuon signal
#isim = 2 to run on Aprime to dielectron signal
#isim = 3 to run on single particle gun:
#isim = 4 to run on DY to dimuon sample generated with Pythia
#isim = 5 to run on J/psi to dimuon sample generated with Pythia
#isim = 6 to run on cosmic sample
#isim = 7 to run on trimuon sample
#isim = 8 to run on background-simulation only
##3. particle type
#igun = 1: muon
#igun = 2: electron
#igun = 3: positron
#igun = 4: proton
#igun = 5: gamma
#igun = 6: pi+
#igun = 7: pi-
#igun = 8: klong
#igun = 9: pi0 
#4. the location where the particle is generate
#5. input specifies that the particle is “displaced” (ie not produced at the SQ target)
#6. input specifies that an ntuple should be created
#7. tells the code whether or not to run pileup
#8. name of outputfile
#9. where to store the output
#-------------------------------------------------------------------------------#Here is an example
#		 const int nevents = 200,
#		 const int isim = 1,
#		 const int igun = 0,
#		 const double zvertex = -300, // target_coil_pos_z
#		 const bool do_displaced_tracking = true,
#		 const bool do_analysis = true,
#		 bool run_pileup = false,
#		 std::string input_file = "Brem_2.750000_z500_600_eps_-6.4",
#		 std::string input_path = "/seaquest/users/cmantill/DarkQuest/lhe/output/displaced_Aprime_Muons_z500-600/",
#		 std::string out_file = "output.root",
#		 std::string out_path = "./",
#		 std::string pileup_file = "/pnfs/e1039/persistent/users/apun/bkg_study/e1039pythiaGen_26Oct21/10_bkge1039_pythia_wshielding_100M.root",
#		 const int verbosity = 0
#root -b -q RecoE1039Sim.C\(50,3,3,520.00,true,true,false,\"\",\"\",\"output.root\",\"./\",\"/pnfs/e1039/persistent/users/apun/bkg_study/e1039pythiaGen_26Oct21/10_bkge1039_pythia_wshielding_100M.root\",0\)
root -b -q RecoE1039Sim.C\(20, 3, 2, 520.00,true,true,false,\"\",\"\",\"electron_520_20eve.root\",\"/seaquest/users/dwong/ntuple_big/\",\"/pnfs/e1039/persistent/users/apun/bkg_study/e1039pythiaGen_26Oct21/10_bkge1039_pythia_wshielding_100M.root\",0\)
#/seaquest/users/dwong/aprime_output
#root -b -q 'RecoE1039Sim.C(1000, 1, 0, -300., true, true, false, "Brem_1.850000_z500_600_eps_-6.4", "/seaquest/users/cmantill/DarkQuest/lhe/output/displaced_Aprime_Muons_z500-600/", "outputAmumuTest_m1.85_eps6.4_withEmu.root", "./","", 0)'

cd
