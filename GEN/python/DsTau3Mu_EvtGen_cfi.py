import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


process = cms.Process('GEN')
process.load('GeneratorInterface.genFilters.customthreemufilter_cfi')



generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'SoftQCD:singleDiffractive = on',
            'SoftQCD:doubleDiffractive = on',
            '431:onMode = off',
            '431:onIfAny = 15',
            '15:addChannel = on .01 0 13 13 -13',
            '15:onMode = off',
            '15:onIfMatch = 13 13 13',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    )
)

DsFilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(431)  #D_s
)

MuFilter = cms.EDFilter("MCParticlePairFilter",
    MinP = cms.untracked.vdouble(2.5, 2.5),
    MaxEta = cms.untracked.vdouble(3.0, 3.0),
    MinEta = cms.untracked.vdouble(-3.0, -3.0),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)


threemufilter = cms.EDFilter("CustomThreeMuFilter",
                                        NumRequired = cms.int32(3),
                                        AcceptMore = cms.bool(True),
                                        ParticleID = cms.vint32(13,13,13),
                                        PtMin = cms.vdouble(1.5, 1.5, 1.5),
                                        EtaMax = cms.vdouble(2.45, 2.45, 2.45),
#                                        PtMin = cms.vdouble(2.9, 2.9, 2.7),
#                                        EtaMax = cms.vdouble(2.45, 2.45, 2.45),
                                        Status          = cms.vint32(1,1,1),
                                        invMassMin      = cms.double(0),
                                        invMassMax      = cms.double(222222),
                                        maxDr           = cms.double(2.5)
)




#ProductionFilterSequence = cms.Sequence(generator * DsFilter * MuFilter)
ProductionFilterSequence = cms.Sequence(generator * DsFilter * threemufilter)
