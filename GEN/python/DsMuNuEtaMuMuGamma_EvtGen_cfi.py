import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


process = cms.Process('GEN')
process.load('GeneratorInterface.genFilters.customthreemufilter_cfi')



generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.0),
                         ##crossSection = cms.untracked.double(54000000000), # Given by PYTHIA after running
                         ##filterEfficiency = cms.untracked.double(0.004), # Given by PYTHIA after running
                         maxEventsToPrint = cms.untracked.int32(2),
                         ExternalDecays = cms.PSet(
                          EvtGen130 = cms.untracked.PSet(
                           decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                           particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
                           user_decay_file = cms.vstring('GenProduction/GEN/data/DsMuNuEta_MuMuGamma.dec'),
                           list_forced_decays = cms.vstring('MyDs+','MyDs-'),
                           convertPythiaCodes = cms.untracked.bool(False),
                           operates_on_particles = cms.vint32()
                          ),
                          parameterSets = cms.vstring('EvtGen130')
                         ),

                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'ParticleDecays:limitTau0 = off',
                                 'ParticleDecays:limitCylinder = on',
                                 'ParticleDecays:xyMax = 2000',
                                 'ParticleDecays:zMax = 4000',
                                 #'HardQCD:all = on',
                                 'HardQCD:hardccbar = on',
                                 'HardQCD:hardbbbar = on',
                                 'PhaseSpace:pTHatMin = 15',
                                 'PhaseSpace:pTHatMax = 1000',
                                 '130:mayDecay = on',
                                 '211:mayDecay = on',
                                 '321:mayDecay = on'
                             ),
                          parameterSets = cms.vstring('pythia8CommonSettings',
                                                      'pythia8CUEP8M1Settings',
                                                      'processParameters',
                                                     )
                         )
)



DsFilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(431)  #D_plus
)







MuFilter = cms.EDFilter("MCParticlePairFilter",
    MinPt = cms.untracked.vdouble(3, 3),
    MaxEta = cms.untracked.vdouble(2.45, 2.45),
    MinEta = cms.untracked.vdouble(-2.45, -2.45),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)





threemufilter = cms.EDFilter("CustomThreeMuFilter",
                                        NumRequired = cms.int32(3),
                                        ParticleID = cms.vint32(13,13,13),
                                        PtMin = cms.vdouble(2.8, 2.8, 1.8),
                                        EtaMax = cms.vdouble(2.41, 2.41, 2.41),
                                        Status          = cms.vint32(1,1,1),
                                        invMassMin      = cms.double(1.58),
                                        invMassMax      = cms.double(2.2),
                                        maxDr           = cms.double(0.8)
)


multimugenfilter = cms.EDFilter("MCMultiParticleFilter",
                                        NumRequired = cms.int32(3),
                                        AcceptMore = cms.bool(True),
                                        ParticleID = cms.vint32(13,13,13),
                                        PtMin = cms.vdouble(3, 3, 2),
                                        EtaMax = cms.vdouble(2.5, 2.5, 2.5),
                                        Status = cms.vint32(1,1,1)
)





#ProductionFilterSequence = cms.Sequence(generator * DsFilter * multimugenfilter)
ProductionFilterSequence = cms.Sequence(generator * DsFilter * threemufilter)


