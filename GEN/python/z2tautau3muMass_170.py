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
            '23:onIfMatch = 15 999015',  # Z ? tau TauM195
            '999015:tau0 = 8.7119688e-02',  # 87.1 mm decay length
            '999015:isResonance = false',
            '999015:m0 = 1.950',
            '999015:mayDecay = on',
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
            #operates_on_particles  = cms.vint32([15, -15]),    
            operates_on_particles  = cms.vint32([999015, -999015]), 
            convertPythiaCodes     = cms.untracked.bool(False),
            user_decay_embedded    = cms.vstring(
"""
Alias      Mytau-       TauM195-
Alias      Mytau+       TauM195+
ChargeConj Mytau+       Mytau-

Decay Mytau-
1.000 mu+ mu+ mu- PHSP;
Enddecay
CDecay Mytau+

End

"""

            ),
        ),
        parameterSets = cms.vstring('EvtGen130'),
    ),
    nRepeat = cms.int32(0), #  number of Redecays
    crossSection = cms.untracked.double(999),
    ParticlesIDtoRedecay = cms.vint32(99999),
    ReDecayConditions = cms.string("ThreeMuMass"), # or "ThreeMuMass"

)

z_mass_filter = cms.EDFilter("MCParticlePairFilter",
    MaxInvMass = cms.untracked.double(120.0),
    MinInvMass = cms.untracked.double(60.0),
    ParticleCharge = cms.untracked.int32(-3),
    ParticleID1 = cms.untracked.vint32(15),
    ParticleID2 = cms.untracked.vint32(999015)
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

