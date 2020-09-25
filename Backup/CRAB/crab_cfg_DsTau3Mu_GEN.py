from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsTau3Mu_13TeV_MC2018_GENSIM'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../MCProduction_2018/DsTauTo3Mu_GEN_cfg.py'

config.Data.outputPrimaryDataset = 'DsTau3Mu'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000 #we expect 50 events per file
NJOBS = 10000 #total number of events = 500000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True

config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_DsTau3Mu_13TeV_SIM'

config.Site.storageSite = 'T2_US_Florida'
