# GenProduction


First clone this repository
```sh
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src
cmsenv
git clone git@github.com:t3mucommontools/GenProduction.git
git clone git@github.com:T3MuAnalysisTools/GeneratorInterface.git
scram b -j 8
cd GenProduction
```

##Make sure you also cloned T3MuAnalysisTools/GeneratorInterface.git


There are 3 directories: GEN, DIGI, AODSIM. 

GEN (GENeration):
Pythia cards can be found in GEN/pythia, the QCD ( b-filter ) with muons filters for example is Pythia_BQuarkFilterTwoMuon_cfi.py.
One can setup the configs as:

```sh
./configureGenJob.py -f <card name in pythia dir> -ne <Number of events per job> -nj <number of jobs> -tag <Tag> -site T2_US_Florida -user cherepan
```

where tag will be used as a prefix to produced samples, for me the command would look like

```
./configureGenJob.py -f Pythia_BQuarkFilterTwoMuon_cfi.py  -ne 1000000 -nj 10000 -tag VladimirGeneration22_06_2020
```

For example I want to submit MuNuEta(MuMuGamma), I do:

```sh
./configureGenJob.py -f DMuNuEtaMuMuGamma_EvtGen_cfi.py -ne 1000000 -nj 10000 -tag Round01_10_2020 -site T2_US_Florida -user cherepan
```

Output looks like
```sh
Crab and gen fragment configured:
crab_cfg_DMuNuEtaMuMuGamma_EvtGen.py
DMuNuEtaMuMuGamma_EvtGen_GEN.py
```
And submit:

```sh
crab submit -c crab_cfg_DMuNuEtaMuMuGamma_EvtGen.py
```



This will create corresponding fragment and crab config, the last can be submitted: crab submit -c <crab_config>.


When generation is completed setup next step in DIGI:

```
./configureDIGJob.py -s <Path to Generated Sample> -nu <Number of units> -tag <Tag>
```

Path to Generated Sample  - the pass retrieved by crab report on gen sample
Number of units  - number of gen files per job ( better to use 1 or 2)
Tag - Tag



AODSIM:
Similarly to DIGI,

```
./configureAODJob.py  -s <Path to DIGI  Sample> -nu <Number of units> -tag <Tag>
```

Number of units here should be large (to end up with 200-300 final AOD files or with 10000-15000 events per AOD)

