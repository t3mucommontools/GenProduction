from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'DsPhiPi_13TeV_MC2018_step2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../Run2018/TSG-RunIIAutumn18DR-step2_cfg.py'

config.Data.inputDataset = '/DsPhiPi/bjoshi-CRAB3_MC2018_DsPhiPi_13TeV_SIM-03d9d05a1699e597b2e7ec2955fdf391/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100
config.JobType.numCores = 4
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_DsPhiPi_13TeV_step2'

config.Site.storageSite = 'T2_US_Florida'
