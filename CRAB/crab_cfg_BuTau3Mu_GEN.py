from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'BuTau3Mu_13TeV_MC2018_DIGI'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../MCProduction_2018/BuTau3Mu_13TeV_MC2018_DIGI.py'

config.Data.inputDataset = '/BuTau3Mu/bjoshi-CRAB3_MC2018_BuTau3Mu_13TeV_SIM-515d13a7c2da025849741ef1a17ef91e/USER' 
config.Data.outputPrimaryDataset = 'BuTau3Mu'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 100 #we expect 50 events per file
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'
config.JobType.allowUndistributedCMSSW = True

#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC2018_BuTau3Mu_13TeV_DIGI'

config.Site.storageSite = 'T2_US_Florida'
