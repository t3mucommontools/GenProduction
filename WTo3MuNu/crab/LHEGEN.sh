if [ -z $CRAB_Id ]; then
 CRAB_Id=1
fi
export SEED=$((123456 + $CRAB_Id))
echo $SEED > SEED.txt
CUSTOM="import os ; process.externalLHEProducer.args=cms.vstring(os.path.abspath('ppW3MuNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz')) ; process.load('Configuration.StandardSequences.Services_cff') ; process.RandomNumberGeneratorService=cms.Service('RandomNumberGeneratorService',generator=cms.PSet(initialSeed=cms.untracked.uint32($SEED)),externalLHEProducer=cms.PSet(initialSeed=cms.untracked.uint32($SEED)),VtxSmeared=cms.PSet(initialSeed=cms.untracked.uint32($SEED)))"
cmsDriver.py Configuration/GenProduction/python/ppW3MuNu_fragment.py  \
  --mc                                                                \
  --eventcontent RAWSIM,LHE                                           \
  --datatier GEN,LHE                                                  \
  --conditions 106X_upgrade2018_realistic_v4                          \
  --beamspot Realistic25ns13TeVEarly2018Collision                     \
  --step LHE,GEN                                                      \
  --geometry DB:Extended                                              \
  --era Run2_2018                                                     \
  --fileout file:LHEGEN.root                                          \
  --nThreads 4                                                        \
  -n 2000 --no_exec --python_filename=pset_LHEGEN.py                  \
  --customise_commands="$CUSTOM"