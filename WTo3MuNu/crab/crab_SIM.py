from CRABClient.UserUtilities import config
config = config()

config.General.requestName      = 'W3MuNu_SIM'
config.General.transferOutputs  = True
config.General.transferLogs     = True
config.General.workArea         = 'crabSIM'

config.JobType.pluginName       = 'Analysis'
config.JobType.psetName         = 'pset_SIM.py'
config.JobType.numCores         = 4
config.JobType.maxMemoryMB      = 2499
config.JobType.maxJobRuntimeMin = 2750

config.Data.inputDBS             = 'phys03'

config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 1
config.Data.publication   = True

# to be modified
config.Data.inputDataset         = '/WTo3MuNu_test4/lguzzi-crab_W3MuNu_LHEGEN-1bd52acfa6095ff2802965001ce9710f/USER'
config.Data.outLFNDirBase = '/store/user/lguzzi/'
config.Site.storageSite   = 'T3_IT_MIB'
config.Site.ignoreGlobalBlacklist  = True
