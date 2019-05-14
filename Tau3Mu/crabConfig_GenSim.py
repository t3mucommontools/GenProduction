from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'MinBias_13TeV_MC2016_GENSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Ds_Tau_3mu_pythia8.py'

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 5
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/cherepan/'
config.Data.publication = True
config.Data.outputDatasetTag = 'Ds_Tau_3mu_pythia8'

config.Site.storageSite = 'T2_US_Florida'
