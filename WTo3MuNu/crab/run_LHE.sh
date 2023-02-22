export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh

tar -xf CMSSW_10_6_30_patch1.tar
cd CMSSW_10_6_30_patch1
scramv1 b ProjectRename
eval `scramv1 runtime -sh`
cd ..
cmsRun -e -j FrameworkJobReport.xml pset_LHEGEN.py
