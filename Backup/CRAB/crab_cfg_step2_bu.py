from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BuTau3Mu_13TeV_MC2018_DIGI_v2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TSG-RunIIAutumn18DR-step2_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4

config.Data.inputDataset = '/BuTau3Mu/bjoshi-CRAB3_MC2018_BuTau3Mu_13TeV_SIM-515d13a7c2da025849741ef1a17ef91e/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_BuTau3Mu_13TeV_DIGI'

config.Site.storageSite = 'T2_US_Florida'
