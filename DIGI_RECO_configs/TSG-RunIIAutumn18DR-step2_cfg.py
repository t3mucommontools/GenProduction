# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:innput.root --fileout file:TSG-RunIIAutumn18DR-00006_step1.root --pileup_input dbs:/MinBias_TuneCP5_13TeV-pythia8/RunIIFall18GS-102X_upgrade2018_realistic_v9-v1/GEN-SIM#986c4721-fac5-498a-b972-540b34fcc43f --mc --eventcontent RAWSIM --pileup 2018_25ns_JuneProjectionFull18_PoissonOOTPU --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --customise_commands process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62) \n process.mix.input.nbPileupEvents.probValue = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571)\n process.simHcalDigis.markAndPass = cms.bool(True) --step DIGI,L1,DIGI2RAW,HLT:@relval2018 --nThreads 4 --geometry DB:Extended --era Run2_2018 --python_filename TSG-RunIIAutumn18DR-00006_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 67
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2018_25ns_JuneProjectionFull18_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_2018v32_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
    #'file:TSG-RunIIFall18GS-doublemu.root'
    'DsTau3Mu_13TeV_MC2018_SIM.root'
    ),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:67'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('DsTau3Mu_MC2018_DIGI.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/F6D5ED9F-1592-E811-82D4-008CFA197418.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/7C15A912-1392-E811-87E6-008CFA111224.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/743CE35A-F991-E811-86BD-008CFA197444.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/30003F8E-1792-E811-BA0D-008CFA197E30.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/202C0E5D-F991-E811-AD2A-008CFA165F5C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/1C83C67C-1992-E811-8D38-008CFA197AC4.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/12723A5D-F991-E811-9833-008CFA197904.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/0AFA7F5B-F991-E811-A160-008CFA197A20.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90012/0A77A556-1592-E811-B450-008CFA197D34.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/FA8E8FA3-1292-E811-9583-008CFA197CF0.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/EE73332F-0A92-E811-A928-008CFA197BDC.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/EABB93F6-F891-E811-8943-008CFA197A20.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/E025B927-1092-E811-AC99-008CFA197A88.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/CE85C9E7-2392-E811-9C79-008CFA110C6C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/CA5E8EF6-F891-E811-A6E8-008CFA197A20.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/C2125A46-0992-E811-AD73-008CFA197B6C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/B84FC3A0-1292-E811-A93C-008CFA11125C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/B2178BA3-1292-E811-817C-008CFA197CF0.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/9E3A8BA3-1292-E811-95C4-008CFA197CF0.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/944C6A2E-0A92-E811-8C16-008CFA197DF8.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/8E6287A3-1292-E811-87D0-008CFA11125C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/7A2E5CA0-1092-E811-9B1C-008CFA1979B0.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/68CB8AA3-1292-E811-8288-008CFA197AEC.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/4ACC96BE-1292-E811-9CA7-008CFA56D64C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/2E942839-8292-E811-9338-008CFA110C6C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/22310DDF-1B92-E811-8C40-008CFA110C84.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/1CA2A6A2-1292-E811-B90F-008CFA197E74.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/16C9A8A2-1292-E811-AC1E-008CFA197E74.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/162B54C2-0D92-E811-8EEF-008CFA165F40.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90011/12C3B1A3-1292-E811-9193-008CFA197CF0.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/ECE86EF1-F891-E811-A3E7-008CFA197454.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/E6E75087-D292-E811-9948-008CFA197A90.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/E27DF6FE-0592-E811-8E78-008CFA197904.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/D4D5A67D-8792-E811-9EB0-008CFA1974B4.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/D010C9F4-F891-E811-AAF3-008CFA110AE8.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/BC436FDC-0F92-E811-9871-008CFA165F28.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/B27B35E8-0F92-E811-B609-008CFA197B80.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/AA07D15C-F991-E811-831B-008CFA197E0C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/A0BC4208-D692-E811-8BA7-008CFA197900.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/96A862F9-CE92-E811-B736-008CFA197D74.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/62478D5D-F991-E811-B634-008CFA11138C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/5C447145-D192-E811-84AB-008CFA111154.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/529CA971-CE92-E811-AA7D-008CFA110AEC.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/4C5615F6-F891-E811-B683-008CFA1660A8.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/4C4468DA-0F92-E811-B91C-008CFA197B54.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/4456BF0D-0892-E811-9317-008CFA11120C.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/382ECEDA-0F92-E811-9ADB-008CFA197B14.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/281351C2-CF92-E811-89A5-008CFA111210.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/2035A0F4-F891-E811-B467-008CFA197A90.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/1A6F15F6-F891-E811-8FCF-008CFA1660A8.root',
    '/store/mc/RunIIFall18GS/MinBias_TuneCP5_13TeV-pythia8/GEN-SIM/102X_upgrade2018_realistic_v9-v1/90010/0628AA45-D392-E811-A640-008CFA11125C.root',
)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62) 
process.mix.input.nbPileupEvents.probValue = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571,0.028571)
process.simHcalDigis.markAndPass = cms.bool(True)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
