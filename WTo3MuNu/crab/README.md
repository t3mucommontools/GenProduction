## LHEGEN

LHE and GEN events are produced in one single step using the gridpack in this directory. 
Since crab cannot read on /eos, the gridpack is uploaded to the crab server together with the CMSSW working area, and a custom script calls cmsRun. 
The pset file must be generated before submission. 

```bash
./LHEGEN.sh
crab submit crab_LHEGEN.sh
```

*NOTE*: since this generation is run through a custom script, the number of events generated per job is decided by the .sh file and not by crab. For convenience, we can set

```python
config.Data.unitsPerJob   = 2000
config.Data.totalUnits    = 5e+6
```

where unitsPerJob **must be identical** to what is written in the .sh file (and has no direct effect), while totalUnits is the total number of events we want. Crab will determine the number of jobs based on this numbers (2500 in this case). The value nEvents for the externalLHEProducer is overridden by the .sh file. 
The output of this step is a .root file containing the LHE and GEN information, and a .txt file containing the random seed used for the generation. 