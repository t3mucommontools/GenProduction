CUSTOM="import os ; process.externalLHEProducer.args=cms.vstring(os.path.abspath('ppW3MuNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'))"
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