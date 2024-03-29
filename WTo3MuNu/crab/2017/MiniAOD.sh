cmsDriver.py step1                                  \
  --mc                                              \
  --eventcontent MINIAODSIM                         \
  --runUnscheduled                                  \
  --datatier MINIAODSIM                             \
  --conditions 106X_mc2017_realistic_v9             \
  --step PAT                                        \
  --procModifiers run2_miniAOD_UL                   \
  --geometry DB:Extended                            \
  --era Run2_2017                                   \
  --filein file:RECO.root                           \
  --fileout file:MiniAOD.root                       \
  --python_filename pset_MiniAOD.py                 \
  -n -1 --no_exec --nThreads 4