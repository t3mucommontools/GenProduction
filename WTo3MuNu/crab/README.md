## LHEGEN

LHE and GEN events are produced in one single step using the gridpack in this directory. 
Since crab cannot read on /eos, the gridpack is uploaded to the crab server together with the CMSSW working area, and a custom script calls cmsRun. 

```bash
crab submit crab_LHEGEN.sh
```

*NOTE*: since this generation is run through a custom script, the number of events generated per job is decided by the .sh file and not by crab. For convenience, we can set

```python
config.Data.unitsPerJob   = int(2e+3)
config.Data.totalUnits    = int(5e+6)
```

where unitsPerJob **must be identical** to what is written in the .sh file (and has no direct effect), while totalUnits is the total number of events we want. Crab will determine the number of jobs based on this numbers (2500 in this case). The value nEvents for the externalLHEProducer is overridden by the .sh file. 
The output of this step is a .root file containing the LHE and GEN information, and a .txt file containing the random seed used for the generation. The SEED.txt file should not be downloaded when publishing the dataset. 

In the crab_LHEGEN.sh modify accordingly:

```python
config.Data.outLFNDirBase = ' ... '
config.Site.storageSite   = ' ... '
```

## SIM to MiniAOD

From SIM onward, generation is done the standard way, that is specifying a pset and an input dataset in the crab config file. First generate the pset, then submit crab specifying the correct input dataset (from the previous step step). The chain order is:

### SIM

```bash
cmsrel CMSSW_10_6_17_patch1 
cd CMSSW_10_6_17_patch1/src
eval `scramv1 runtime -sh`
cd -
./SIM.sh
crab submit crab_SIM.py
```

### DigiRecoPremix

```bash
cmsrel CMSSW_10_6_17_patch1 
cd CMSSW_10_6_17_patch1/src
eval `scramv1 runtime -sh`
cd -
./DRPremix.sh
crab submit crab_DRP.py
```

### HLT

```bash
cmsrel CMSSW_10_2_16_UL # use CMSSW_9_4_14_UL_patch1 for 2017UL
cd CMSSW_10_2_16_UL/src
eval `scramv1 runtime -sh`
cd -
./HLT.sh
crab submit crab_HLT.py
```

### RECO

```bash
cmsrel CMSSW_10_6_17_patch1 
cd CMSSW_10_6_17_patch1/src
eval `scramv1 runtime -sh`
cd -
./RECO.sh
crab submit crab_RECO.py
```

### MiniAOD

```bash
cmsrel CMSSW_10_6_20 
cd CMSSW_10_6_20/src
eval `scramv1 runtime -sh`
cd -
./MiniAOD.sh
crab submit crab_MiniAOD.py
```