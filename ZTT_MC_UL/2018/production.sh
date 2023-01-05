JOB_NAME='Tau3Mu_MC2018_tauMassNominal'

export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.sh

source $VO_CMS_SW_DIR/cmsset_default.sh
tar -zxvf archive.tar

cd CMSSW_10_2_16_UL
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

cd CMSSW_10_6_19_patch3
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

cd CMSSW_10_6_4_patch1
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

##GEN
cd CMSSW_10_6_19_patch3
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_GEN.py
##SIM DRP 
cd CMSSW_10_6_4_patch1
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_SIM.py
cmsRun ZTau3Mu_DRP.py
##HLT
cd CMSSW_10_2_16_UL
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_HLT.py
##RECO MINIAOD
cd CMSSW_10_6_4_patch1
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_RECO.py
## always run last step with job report
cmsRun -e -j FrameworkJobReport.xml ZTau3Mu_MINIAOD.py
