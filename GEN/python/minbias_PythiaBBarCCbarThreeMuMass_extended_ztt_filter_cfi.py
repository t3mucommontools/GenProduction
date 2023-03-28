import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
process = cms.Process('GEN')
process.load('GeneratorInterface.genFilters.threemuonssameoriginextended_ztt_taumu_cfi')




mugenfilter = cms.EDFilter("MCParticlePairFilter",
    MinPt = cms.untracked.vdouble(4.0, 4.0),
    MaxEta = cms.untracked.vdouble(2.45, 2.45),
    MinEta = cms.untracked.vdouble(-2.45, -2.45),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)



multimugenfilter = cms.EDFilter("MCMultiParticleFilter",
                                        NumRequired = cms.int32(3),
                                        ParticleID = cms.vint32(13,13,13),
                                        PtMin = cms.vdouble(2.9, 2.9, 1.9),
                                        EtaMax = cms.vdouble(2.45, 2.45, 2.45),
                                        Status = cms.vint32(1,1,1)

)

#  here is the tune of the ThreeMuonsSameOrigin  filter
threemufilter = cms.EDFilter("ThreeMuonsSameOrigin_ztt_taumu_Extended",
                                        NumRequired = cms.int32(3),
                                        ParticleID = cms.vint32(13,13,13),
                                        PtMin = cms.vdouble(3.0,3.0,2.0),
                                        EtaMax = cms.vdouble(2.4,2.4,2.4),
                                        Status = cms.vint32(1,1,1),
                                        invMassMin      = cms.double(1.4),
                                        invMassMax      = cms.double(2.1),
                                        maxDr           = cms.double(0.3)
)




generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters'
        ),
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
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:ecmPow=0.03344',
            'PDF:pSet=20',
            'MultipartonInteractions:bProfile=2',
            'MultipartonInteractions:pT0Ref=1.41',
            'MultipartonInteractions:coreRadius=0.7634',
            'MultipartonInteractions:coreFraction=0.63',
            'ColourReconnection:range=5.176',
            'SigmaTotal:zeroAXB=off',
            'SpaceShower:alphaSorder=2',
            'SpaceShower:alphaSvalue=0.118',
            'SigmaProcess:alphaSvalue=0.118',
            'SigmaProcess:alphaSorder=2',
            'MultipartonInteractions:alphaSvalue=0.118',
            'MultipartonInteractions:alphaSorder=2',
            'TimeShower:alphaSorder=2',
            'TimeShower:alphaSvalue=0.118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2',
            'Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',
            'SLHA:keepSM = on',
            'SLHA:minMassSM = 1000.',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10',
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(999),
#    filterEfficiency = cms.untracked.double(0.0001),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    nRepeat = cms.int32(10000), #  number of Redecays
    Status = cms.vint32(1,1),  #  list of particles to re-Decay
    ParticlesIDtoRedecay = cms.vint32(511, 521, 513, 523, 531, 533,  541, 5122, 411, 421, 413, 423, 431, 433,  415, 10411),
    ReDecayConditions = cms.string("ThreeMuMass") # or "ThreeMuMass"
)


#ProductionFilterSequence = cms.Sequence(generator*mugenfilter)
#ProductionFilterSequence = cms.Sequence(generator*threemufilter)

ProductionFilterSequence = cms.Sequence(generator*threemufilter)


