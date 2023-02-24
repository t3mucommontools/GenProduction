from CRABClient.UserUtilities import config
config = config()

config.General.requestName      = 'W3MuNu_HLT'
config.General.transferOutputs  = True
config.General.transferLogs     = True
config.General.workArea         = 'crabHLT'

config.JobType.pluginName       = 'Analysis'
config.JobType.psetName         = 'pset_HLT.py'
config.JobType.numCores         = 4
config.JobType.maxMemoryMB      = 2499
config.JobType.maxJobRuntimeMin = 2750

config.Data.inputDBS             = 'phys03'

config.Data.splitting     = 'FileBased'
config.Data.unitsPerJob   = 1
config.Data.publication   = True

# to be modified
config.Data.inputDataset  = 'changeme'
config.Data.outLFNDirBase = '/store/user/lguzzi/'
config.Site.storageSite   = 'T3_IT_MIB'
config.Site.ignoreGlobalBlacklist  = True
