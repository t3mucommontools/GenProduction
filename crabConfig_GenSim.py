from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MinBias_13TeV_MC2016_GENSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'MinBias_Gen.py'
#config.JobType.numCores = 8

config.Data.outputPrimaryDataset = 'DsTau3Mu'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000 #we expect 50 events per file
NJOBS = 10 #total number of events = 500000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/cherepan/'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2016_MinBias'

config.Site.storageSite = 'T2_US_Florida'
