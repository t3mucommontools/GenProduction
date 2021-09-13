# GenProduction


How to setup: 
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

**Make sure you also cloned T3MuAnalysisTools/GeneratorInterface.git**


There are 3 directories: GEN, DIGI, AODSIM. 

GEN (GENeration):
Pythia cards can be found in GEN/pythia, the card name should be self-explanatory, e.g. DMuNuEtaMuMuGamma_EvtGen_cfi.py  is D/Ds-> MuNuEta(MuMuGamma)


One can setup gen  configs as:

```sh
./configureGenJob.py -f <card name in pythia dir> -ne <Number of events per job> -nj <Number of jobs> -tag <Tag> -site <T2 site> -user <T2 user name>
```

Options are:

* card name in pythia dir     - the process you want to generate, all are in pythia directory; Give a name to the config w/o pythia/ prefix.
* Number of events per job    - 1000000 is found to be practicaly best
* number of jobs              - Number of Jobs, one may just take maximum allowed - 10000
* Tag                         - Tag that will be added as a prefix to all samples, in practice one can use date or something else to navigate sample in future. For example if you do several rounds you can set Tag to RoundI, RoundII ...

* T2 site                     - Storage site, Florida by default, for Bari should be specificaly given -site T2_IT_Bari
* T2 user name                - cherepan by default :) Everybody else should specify.

Have a look also at the help message:

```sh
./configureGenJob.py -h
```



For example I want to submit MuNuEta(MuMuGamma), I do:
```sh
./configureGenJob.py -f DMuNuEtaMuMuGamma_EvtGen_cfi.py -ne 1000000 -nj 10000 -tag Round01_10_2020 -site T2_US_Florida -user cherepan
```

This will create corresponding fragment and crab config, output looks like:
```sh
Crab and gen fragment configured:
crab_cfg_DMuNuEtaMuMuGamma_EvtGen.py
DMuNuEtaMuMuGamma_EvtGen_GEN.py
```
And now you can just submit:

```sh
crab submit -c crab_cfg_DMuNuEtaMuMuGamma_EvtGen.py
```




When generation is completed setup next step in DIGI/:


```
./configureDIGJob.py -s <Path to Generated Sample> -nu <Number of units> -tag <Tag> -site <T2 site> -user <T2 user name>
```

* Path to Generated Sample - a path to generated sample, can be obtained by crab report
* Number of units          - number of gen files to be taken per DIGI job, since each GEN file will contain a few jobs, it is practical here to reduce number of jobs from 10 000 to less amount
* Tag, T2 site, T2 user name as before

As in GEN step this command will generate python and crab config, the last can be submited by crab -c submit




When DIGI is completed setup next step in AODSIM/:


```
./configureAODJob.py   -s <Path to DIGI Sample> -nu <Number of units> -tag <Tag> -site <T2 site> -user <T2 user name>
```

* Path to DIGI Sample - a path to digi sample, can be obtained by crab report
* Number of units     - number of digi  files to be taken per AODSIM job, here number of units can be well increased, assuming that you ended up with 100000 events in whole digi sample, the number of units here can be chosen such that AODSIM sample of 100000 events will be of 5 files ( each 20 000 events)

* Tag, T2 site, T2 user name as before

As in GEN/DIGI step this command will generate python and crab config, the last can be submited by crab -c submit



