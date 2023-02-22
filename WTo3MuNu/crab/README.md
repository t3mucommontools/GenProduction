## LHEGEN

LHE and GEN events are produced in one single step using the gridpack in this directory. 
Since crab cannot read on /eos, the gridpack is uploaded to the crab server together with the CMSSW working area, and a custom script calls cmsRun. 
The pset file must be generated before submission. 
The pset must be modified by hand to allow crab to read a local gridpack (using sed). 

```bash
./LHEGEN.sh
sed -i 's$\x27$\"$g' pset_LHEGEN.py
sed -i 's$\"ppW3MuNu\_slc7\_amd64\_gcc700\_CMSSW\_10\_6\_19\_tarball\.tar\.xz\"$os\.path\.abspath(\"ppW3MuNu\_slc7\_amd64\_gcc700\_CMSSW\_10\_6\_19\_tarball\.tar\.xz\")$g' pset_LHEGEN.py
sed -i '1,1s$^$import os\n$' pset_LHEGEN.py
crab submit crab_LHEGEN.sh
```