JOB_NAME='ZTau3Mu_MC2017_tauMassNominal'

export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.sh

source $VO_CMS_SW_DIR/cmsset_default.sh
tar -zxvf archive.tar

cd CMSSW_10_6_12
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

cd CMSSW_10_6_2
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

cd CMSSW_10_6_4
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

cd CMSSW_9_4_14_UL_patch1
scramv1 b ProjectRename
eval `scram runtime -sh`
scram b 
cd -

##GEN
cd CMSSW_10_6_12
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_GEN.py
##SIM
cd CMSSW_10_6_2
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_SIM.py
##DRP
cd CMSSW_10_6_4
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_DRP.py
##HLT
cd CMSSW_9_4_14_UL_patch1
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_HLT.py
##RECO MINIAOD
cd CMSSW_10_6_2
eval `scramv1 runtime -sh`
cd -
cmsRun ZTau3Mu_RECO.py
## always run last step with job report
cmsRun -e -j FrameworkJobReport.xml ZTau3Mu_MINIAOD.py
