import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
process = cms.Process('GEN')
process.load('GeneratorInterface.genFilters.customthreemufilter_cfi')






twomufilter = cms.EDFilter("CustomThreeMuFilter",
                                        NumRequired = cms.int32(2),
                                        ParticleID = cms.vint32(13,13),
                                        PtMin = cms.vdouble(3, 3),
                                        EtaMax = cms.vdouble(2.45, 2.45),
                                        Status = cms.vint32(1,1),
                                        invMassMin = cms.double(0.2),
                                        invMassMax = cms.double(1.7),
                                        maxDr = cms.double(0.8)
)



generator = cms.EDFilter("Pythia8GeneratorFilter",

                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'SoftQCD:nonDiffractive = on',
                                 'SoftQCD:singleDiffractive = on',
                                 'SoftQCD:doubleDiffractive = on',
                                 'PTFilter:filter = on', 
                                 'PTFilter:quarkToFilter = 5', 
                                 'PTFilter:scaleToFilter = 1.0'
                             ),
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                                         'pythia8CUEP8M1Settings',
                                                         'processParameters',
                                                     )
                         ),
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         pythiaPylistVerbosity = cms.untracked.int32(1)
)



ProductionFilterSequence = cms.Sequence(generator+twomufilter)




