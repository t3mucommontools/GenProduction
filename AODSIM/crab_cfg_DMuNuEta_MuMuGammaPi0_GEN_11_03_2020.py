from WMCore.Configuration import Configuration  
config = Configuration()  

config.section_("General")  
config.General.requestName = 'DMuNuEta_MuMuGammaPi0_GEN_11_03_2020'
config.General.workArea =  'crab_area' 
config.General.transferLogs = True 

config.section_("JobType") 
config.JobType.allowUndistributedCMSSW = True 
config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'DMuNuEta_MuMuGammaPi0_GEN_11_03_2020_DIGI.py'  
config.JobType.maxMemoryMB = 5000 
config.JobType.numCores = 4 
config.section_("Data")  

config.Data.inputDataset = '/DMuNuEta_MuMuGammaPi0_GEN_11_03_2020/cherepan-DMuNuEta_MuMuGammaPi0_GEN_11_03_2020-2c9912c72108c252c02b22bd1c4743d6/USER' 
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 1 
config.Data.totalUnits = -1 
config.Data.inputDBS = 'phys03' 
config.Data.outLFNDirBase = '/store/user/cherepan/' 
config.Data.outputDatasetTag = 'DMuNuEta_MuMuGammaPi0_GEN_11_03_2020_AOD' 
config.Data.publication = True 

config.section_("Site") 
config.Site.storageSite = 'T2_US_Florida' 
dont_check_proxy =  1 
