from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsTau3Mu_13TeV_MC2018_AOD_v2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../Run2018/TSG-RunIIAutumn18DR-step3_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4

config.Data.inputDataset = '/DsTau3Mu/bjoshi-CRAB3_MC2018_DsTau3Mu_13TeV_DIGI-1162bb0e8e81f3fa543a3ebd40ed90ff/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_DsTau3Mu_13TeV_AOD'

config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Purdue','T1_US_FNAL']
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_US_Florida'
