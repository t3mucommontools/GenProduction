from CRABClient.UserUtilities import config
config = config()

config.General.requestName      = 'W3MuNu_LHEGEN'
config.General.transferOutputs  = True
config.General.transferLogs     = True
config.General.workArea         = 'crabLHEGEN'

config.JobType.pluginName       = 'PrivateMC'
config.JobType.psetName         = 'pset_LHEGEN.py'
config.JobType.inputFiles       = [
                                    'LHEGEN.sh',
                                    'CMSSW_10_6_30_patch1.tar', 
                                    'ppW3MuNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz',
                                  ]
config.JobType.disableAutomaticOutputCollection = True
config.JobType.numCores         = 4
config.JobType.maxMemoryMB      = 2499
config.JobType.maxJobRuntimeMin = 2750
config.JobType.scriptExe        = 'run_LHE.sh'
config.JobType.outputFiles      = [
                                    'LHEGEN.root',
                                    #'SEED.txt',  # don't include when publishingcra
                                  ]


config.Data.outputPrimaryDataset = 'WTo3MuNu_ptl0p5_drll0p01_TuneCP5_2017UL_LO_13TeV_pythia8-madgraph'
#config.Data.outputPrimaryDataset = 'WTo3MuNu_test4'

# unitsPerJob: number of events per job (keep reading)
# totalUnits: total number of events
# crab will use these numbers to determine the number of jobs to run
# IMPORTANT NOTE: unitsPerJob has no effect on the number of events per job
# since this generation is run via a custom scriptExe. The number of events
# per job is determined inside the pset python file.
# unitsPerJob value must be identical to that value to have a correct job splitting
config.Data.splitting     = 'EventBased'
config.Data.unitsPerJob   = int(2e+3)
config.Data.totalUnits    = int(5e+6)
config.Data.publication   = True

# to be modified
config.Data.outLFNDirBase = '/store/user/lguzzi/'
config.Site.storageSite   = 'T3_IT_MIB'
