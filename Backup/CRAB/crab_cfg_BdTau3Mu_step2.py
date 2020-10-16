from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DOmega_13TeV_MC2018_DIGI'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TSG-RunIIAutumn18DR-step2_cfg.py'
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 5000
config.JobType.allowUndistributedCMSSW = True



config.Data.inputDataset = '/DPlusMuNuOmega/cherepan-DPlusMuNuOmega_MuMuPi0_13TeV_SIM-3fbfe6da5cc9be48ffcd2145f34fdf39/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'


config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_DOmega_13TeV_DIGI'

config.Site.storageSite = 'T2_US_Florida'
