from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BdTau3Mu_13TeV_MC2018_DIGI'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../Run2018/TSG-RunIIAutumn18DR-step2_cfg.py'

config.Data.inputDataset = '/BdTau3Mu/bjoshi-CRAB3_MC2018_BdTau3Mu_13TeV_SIM-ce0c60e02433ca4f7ace3e70e3940d4d/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100
config.JobType.numCores = 4
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_BdTau3Mu_13TeV_DIGI'

config.Site.storageSite = 'T2_US_Florida'
