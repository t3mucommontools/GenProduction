from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BuTau3Mu_13TeV_MC2018_step2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../Run2018/TSG-RunIIAutumn18DR-step2_cfg.py'

config.Data.inputDataset = '/BuTau3Mu/bjoshi-CRAB3_MC2018_BuTau3Mu_13TeV_SIM-515d13a7c2da025849741ef1a17ef91e/USER' 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100
config.JobType.numCores = 4
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_BuTau3Mu_13TeV_step2'

config.Site.storageSite = 'T2_US_Florida'
