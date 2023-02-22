cmsDriver.py step1 \
  --filein file:ZTau3Mu_BPH-RunIISummer19UL17HLT-evtgen.root \
  --fileout file:ZTau3Mu_BPH-RunIISummer19UL17RECO-evtgen.root \
  --mc                                                        \
  --eventcontent AODSIM                                       \
  --runUnscheduled                                            \
  --datatier AODSIM                                           \
  --conditions 106X_mc2017_realistic_v6            \
  --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI                      \
  --nThreads 4                                                \
  --geometry DB:Extended                                      \
  --era Run2_2017 \
  --python ZTau3Mu_RECO.py \
  --no_exec \
  -n -1