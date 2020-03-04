


import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing



options = VarParsing('analysis')
options.parseArguments()

process = cms.Process('VIEW')

process.source = cms.Source('PoolSource',
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))





process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("genParticles"),                                                                 
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(True),
                                   printVertex = cms.untracked.bool(False),
                                   printStatus = cms.untracked.bool(True),
                                   printIndex = cms.untracked.bool(False),
#                                   status = cms.untracked.vint32( 2 )
                                   )

process.p = cms.Path( process.printTree)



