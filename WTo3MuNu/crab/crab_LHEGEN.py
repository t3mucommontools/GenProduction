from CRABClient.UserUtilities import config
config = config()

config.General.requestName      = 'W3MuNu_LHEGEN'
config.General.transferOutputs  = True
config.General.transferLogs     = True
config.General.workArea         = 'testLHEGEN'

config.JobType.pluginName       = 'PrivateMC'
config.JobType.psetName         = 'pset_LHEGEN.py'
config.JobType.inputFiles       = ['pset_LHEGEN.py', 'CMSSW_10_6_30_patch1.tar']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.numCores         = 4
config.JobType.maxMemoryMB      = 10000
config.JobType.maxJobRuntimeMin = 2750
config.JobType.scriptExe        = 'run_LHE.sh'
config.JobType.outputFiles      = ['LHEGEN.root']


#config.Data.outputPrimaryDataset = 'WTo3MuNu_ptl0p5_drll0p01_TuneCP5_LO_13TeV_pythia8-madgraph'
config.Data.outputPrimaryDataset = 'WTo3MuNu_test'

config.Data.splitting     = 'EventBased'
config.Data.unitsPerJob   = 10
config.Data.totalUnits    = 30
config.Data.publication   = False
config.Data.outLFNDirBase = '/store/user/lguzzi/'

config.Site.storageSite = 'T3_IT_MIB'
