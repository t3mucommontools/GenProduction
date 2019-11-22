# GenProduction

For generating events using PYTHIA8, login to lxplus and set up your workspace.

```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src
cmsenv
git clone git@github.com:T3MuAnalysisTools/GenProduction.git
scram b -j 8
cd GenProduction
```

The fragments for 2018 are stored in MCProduction_2018. The default filter settings are ds filter followed by a muon pair filter with pT_min (2.7,2.7) GeV. If necessary, change the filter settings. Then, change the parameters in crab configuration files (crab_cfg_DsTau3Mu_GEN.py, crab_cfg_BuTau3Mu_GEN.py, crab_cfg_BdTau3Mu_GEN.py, crab_cfg_DsPhiPi_GEN.py). Make sure have write access to the storage site mention in the config file. For submitting crab jobs to generate DsTau3Mu sample, do

```
cd CRAB
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init --voms cms --valid 192:00
crab submit -c crab_cfg_DsTau3Mu_GEN.py
```

For running step 2 and step 3 change the `config.Data.inputDataset` parameter in step2 and step3 crab configuration files in CRAB.
