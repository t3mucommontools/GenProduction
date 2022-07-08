import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'WeakSingleBoson:ffbar2gmZ = on',
            '22:onMode = off',
            '23:onMode = off',
            '22:onIfAny = 15',
            '23:onIfAny = 15',
            #'15:AddChannel = on 0.00001 0 13 13 -13',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        ),
    ),

    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table            = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays     = cms.vstring(
                'Mytau+'           ,
                'Mytau-'           ,
            ),        
            operates_on_particles  = cms.vint32([15, -15]),    
            convertPythiaCodes     = cms.untracked.bool(False),
            user_decay_file        = cms.vstring(
"""
Alias      Mytau+       tau+
Alias      Mytau-       tau-
ChargeConj Mytau+       Mytau-


Decay Mytau+
1.0000000 mu+ mu+ mu- PHSP;
Enddecay
CDecay Mytau-

End

"""

            ),
        ),
        parameterSets = cms.vstring('EvtGen130'),
    ),

)

ztt_tau3mu_filter = cms.EDFilter("PythiaFilterMultiAncestor",
    ParticleID      = cms.untracked.int32(15),
    MinPt           = cms.untracked.double(-1.),
    MinEta          = cms.untracked.double(-1.e4),
    MaxEta          = cms.untracked.double( 1.e4),
    MotherIDs       = cms.untracked.vint32([22]),
    DaughterIDs     = cms.untracked.vint32([13, 13, 13]),
    DaughterMinPts  = cms.untracked.vdouble([-1., -1., -1.]),
    DaughterMaxPts  = cms.untracked.vdouble([ 1.e6,  1.e6,  1.e6]),
    DaughterMinEtas = cms.untracked.vdouble([-1.e4, -1.e4, -1.e4]),
    DaughterMaxEtas = cms.untracked.vdouble([ 1.e4,  1.e4,  1.e4]),
)

z_mass_filter = cms.EDFilter("MCParticlePairFilter",
    MaxInvMass = cms.untracked.double(120.0),
    MinInvMass = cms.untracked.double(60.0),
    ParticleCharge = cms.untracked.int32(-3),
    ParticleID1 = cms.untracked.vint32(15),
    ParticleID2 = cms.untracked.vint32(15)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision$'),
    name = cms.untracked.string('\$Source$'),
    annotation = cms.untracked.string(
        'WeakSingleBoson Z production, '\
        'Z to tau tau (no kin cuts), '\
        'one tau to 3mu, '\
        '13 TeV, '\
        'TuneCP5'
    )
)

#ProductionFilterSequence = cms.Sequence(generator*ztt_tau3mu_filter*z_mass_filter)
ProductionFilterSequence = cms.Sequence(generator*z_mass_filter)

