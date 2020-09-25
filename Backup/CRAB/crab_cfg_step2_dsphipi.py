from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsPhiPi_13TeV_MC2018_DIGI_v4'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TSG-RunIIAutumn18DR-step2_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 10000

config.Data.inputDataset = '/DsPhiPi/bjoshi-CRAB3_MC2018_DsPhiPi_13TeV_SIM-147e38f897ce9fb68e3ae92ad4c3f8ee/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_DsPhiPi_13TeV_DIGI'

config.Site.storageSite = 'T2_US_Florida'
config.Site.whitelist = ['T2_US_Wisconsin','T2_US_Purdue','T1_US_FNAL']
config.Data.ignoreLocality = True
