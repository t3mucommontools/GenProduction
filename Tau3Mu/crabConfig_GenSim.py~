from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MinBias_13TeV_MC2016_GENSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'MinimumBias_Config.py'

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000 
NJOBS = 5
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/cherepan/'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2016_MinBias_SmallScaleTest'

config.Site.storageSite = 'T2_US_Florida'
