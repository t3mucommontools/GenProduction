#!/usr/bin/env python




from __future__ import print_function
import ROOT
import argparse
import numpy as np
from time import time
from datetime import datetime, timedelta
from array import array
from glob import glob
from collections import OrderedDict
from scipy.constants import c as speed_of_light
from DataFormats.FWLite import Events, Handle
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
# https://pypi.org/project/particle/

parser = argparse.ArgumentParser(description='')
parser.add_argument('--files_per_job', dest='files_per_job', default=2    , type=int)
parser.add_argument('--jobid'        , dest='jobid'        , default=0    , type=int)
parser.add_argument('--verbose'      , dest='verbose'      , action='store_true' )
parser.add_argument('--destination'  , dest='destination'  , default='.'  , type=str)
parser.add_argument('--maxevents'    , dest='maxevents'    , default=-1   , type=int)
args = parser.parse_args()


files_per_job = args.files_per_job
jobid         = args.jobid
verbose       = args.verbose
destination   = args.destination
maxevents     = args.maxevents

diquarks = [
    1103,
    2101,
    2103,
    2203,
    3101,
    3103,
    3201,
    3203,
    3303,
    4101,
    4103,
    4201,
    4203,
    4301,
    4303,
    4403,
    5101,
    5103,
    5201,
    5203,
    5301,
    5303,
    5401,
    5403,
    5503,
]

def isAncestor(a, p):
    if a == p :
        return True
    for i in xrange(0,p.numberOfMothers()):
        if isAncestor(a,p.mother(i)):
            return True
    return False


    
handles = OrderedDict()
handles['genp'   ] = ('genParticles', Handle('std::vector<reco::GenParticle>'))
handles['genInfo'] = ('generator'   , Handle('GenEventInfoProduct'           ))
# handles['lhe'    ] = ('source'      , Handle('LHEEventProduct'               ))

# with open('Hb_v1_gen_sim_files.txt') as fp: 
#     lines = fp.readlines()
#     files = ['root://cms-xrd-global.cern.ch/%s' %line.rstrip() for line in lines]
# events = Events(files[:10])

# files = glob('/pnfs/psi.ch/cms/trivcat/store/user/manzoni/RJPsi_Bc_GEN_30nov20_v1/RJpsi-BcToXToJpsiMuMuSelected-RunIISummer19UL18GEN_*.root')
# files = glob('/pnfs/psi.ch/cms/trivcat/store/user/manzoni/RJPsi_Bc_GEN_NO_FILTER_3dec20_v2/RJpsi-BcToXToJpsiMuMuSelected-RunIISummer19UL18GEN_*.root')
# files = glob('/pnfs/psi.ch/cms/trivcat/store/user/manzoni/RJPsi_Bc_GEN_WITH_FILTER_3dec20_v3/RJpsi-BcToXToJpsiMuMuSelected-RunIISummer19UL18GEN_*.root')
# files.sort()
# files_to_process = list(list(zip(*[iter(files)]*files_per_job))[jobid])

events = Events('DMuNuRho_Omega_EvtGen_GEN_2018.root')
#events = Events('DsMuNuEtaMuMuGamma_EvtGen_EvtGen_GEN_2018.root')


branches = [
    'run',
    'lumi',
    'event',

    'qscale',
#     'ctau',
#     'ct',
    'min_bq_pt',
    'max_bq_eta',

    'mu1_pt',
    'mu1_eta',
    'mu1_y',
    'mu1_phi',
    'mu1_q',

    'mu2_pt',
    'mu2_eta',
    'mu2_y',
    'mu2_phi',
    'mu2_q',

    'Ds_pt',
    'Ds_eta',
    'Ds_y',
    'Ds_phi',
    'Ds_m',
    'Ds_status',

    'bhad_pt',
    'bhad_eta',
    'bhad_y',
    'bhad_phi',
    'bhad_m',
    'bhad_q',
    'bhad_pdgid',

    'mmm_pt',
    'mmm_eta',
    'mmm_y',
    'mmm_phi',
    'mmm_m',
    'mmm_q',

    'm2_miss',
    'pt_miss_sca',
    'pt_miss_vec',
    'q2',
    'e_star_mu3',
    'e_hash_mu3',
    'ptvar',
    
    'mu3_pt',
    'mu3_eta',
    'mu3_y',
    'mu3_phi',
    'mu3_q',
    
    'dr_Ds_m',

    'is3m',

    'is_Ds_mu'  ,
    'is_psi2s_mu' ,
    'is_chic0_mu' ,
    'is_chic1_mu' ,
    'is_chic2_mu' ,
    'is_hc_mu'    ,
    'is_Ds_tau' ,
    'is_psi2s_tau',
    'is_Ds_pi'  ,
    'is_Ds_k'   ,
    'is_Ds_3pi' ,
    'is_Ds_hc'  ,

    'pv_x'  ,
    'pv_y'  ,
    'pv_z'  ,

    'sv_x'  ,
    'sv_y'  ,
    'sv_z'  ,

    'lxyz'  ,
    'beta'  ,
    'gamma' ,

    'n_extra_mu',
    'n_Ds',
    
    'weight',

#     'ctau_weight_central',
#     'ctau_weight_up',
#     'ctau_weight_down',
# 
#     'ctau_weight_central_lhe',
#     'ctau_weight_up_lhe',
#     'ctau_weight_down_lhe',
]

fout = ROOT.TFile('%s/flat_tree_bc_chunk%d.root' %(destination, jobid), 'recreate')
ntuple = ROOT.TNtuple('tree', 'tree', ':'.join(branches))
tofill = OrderedDict(zip(branches, [np.nan]*len(branches)))

start = time()
maxevents = maxevents if maxevents>=0 else events.size() # total number of events in the files

for i, event in enumerate(events):
    print("event ---- ", i)
    if (i+1)>maxevents:
        break
        
    if i%1000==0:
        percentage = float(i)/maxevents*100.
        speed = float(i)/(time()-start)
        eta = datetime.now() + timedelta(seconds=(maxevents-i) / max(0.1, speed))
        print('\t===> processing %d / %d event \t completed %.1f%s \t %.1f ev/s \t ETA %s s' %(i, maxevents, percentage, '%', speed, eta.strftime('%Y-%m-%d %H:%M:%S')))
# 
# 
#         print('\t===> processing %d / %d event \t completed %.1f%s' %(i, events.size(), percentage, '%'))

    # access the handles
    for k, v in handles.iteritems():
        event.getByLabel(v[0], v[1])
        setattr(event, k, v[1].product())

#     hepup = event.lhe.hepeup()
#     ctaus = [hepup.VTIMUP.at(ictau) for ictau in xrange(hepup.VTIMUP.size()) if hepup.VTIMUP.at(ictau)>0.] # in [mm]
    
    event.qscale = event.genInfo.qScale()
   
    if verbose: print('=========>')
    
    Ds_mesons = [ip for ip in event.genp if abs(ip.pdgId())==411]
    D_mesons = [ip for ip in event.genp if abs(ip.pdgId())==411]
    Omegas = [ip for ip in event.genp if abs(ip.pdgId())==223]
    Rhos = [ip for ip in event.genp if abs(ip.pdgId())==113]
    Etas = [ip for ip in event.genp if abs(ip.pdgId())==221]
    
#     bs =  [ip for ip in event.genp if abs(ip.pdgId())==511]
    bs =  [ip for ip in event.genp if (abs(ip.pdgId())>500 and abs(ip.pdgId())<600) or (abs(ip.pdgId())>5000 and abs(ip.pdgId())<6000)]
    muons =  [ip for ip in event.genp if abs(ip.pdgId())==13 and ip.status()==1]
    bq = [ip for ip in event.genp if abs(ip.pdgId())==5 and ip.isHardProcess()]
    

    for omega in Omegas:
        daus = [omega.daughter(idau).pdgId() for idau in range(omega.numberOfDaughters())]
        print( " omega daugthers  ", daus)


    for rho in Rhos:
        daus = [rho.daughter(idau).pdgId() for idau in range(rho.numberOfDaughters())]
        print( " rho daugthers  ", daus)


    for eta in Etas:
        daus = [eta.daughter(idau).pdgId() for idau in range(eta.numberOfDaughters())]
        print( " eta daugthers  ", daus)



    for Ds in Ds_mesons:
        
        for k, v in tofill.items(): 
            tofill[k] = np.nan

        tofill['min_bq_pt' ] = min([ip.pt() for ip in bq]) if len(bq) else np.nan
        tofill['max_bq_eta'] = max([abs(ip.eta()) for ip in bq]) if len(bq) else np.nan

        tofill['n_ds'] = len(Ds_mesons)

        daus = [Ds.daughter(idau).pdgId() for idau in range(Ds.numberOfDaughters())]
        print( " D daugthers  ", daus)

#        if verbose: print('\t%s %s pt %3.2f,\t genealogy: ' %(Particle.from_pdgid(Ds.pdgId()), str(daus), Ds.pt()), end='')
        ancestors = []
#        if verbose: print('\t', printAncestors(Ds, ancestors, verbose=True))
#        else: printAncestors(Ds, ancestors, verbose=False)
        
        # only save Ds->mumu
        if sum([abs(dau)==13 for dau in daus])<2: continue
                
        if len(ancestors)==0: continue
        
        first_ancestor = ancestors[-1]
        if first_ancestor.pdgId() in diquarks:
            first_ancestor = ancestors[-2]
              
        # compute the distance between primary and secondary vtx
        sv = Ds.vertex()
        pv = first_ancestor.vertex()
        
        lxyz = np.sqrt((sv.x()-pv.x())**2 + (sv.y()-pv.y())**2 + (sv.z()-pv.z())**2) # in [cm]
        
        # lorentz boost of the B
        beta = first_ancestor.p4().Beta()
        gamma = first_ancestor.p4().Gamma()
        
        # now, lifetime L = beta * gamma * c * t ===> t = (L)/(beta*gamma*c)
        ct = lxyz / (beta * gamma)
        
        tofill['run'        ] = event.eventAuxiliary().run()
        tofill['lumi'       ] = event.eventAuxiliary().luminosityBlock()
        tofill['event'      ] = event.eventAuxiliary().event()
        tofill['qscale'     ] = event.qscale
#         tofill['ctau'       ] = ctaus[0]
#         tofill['ct'         ] = ct*10. # convert cm to mm
        tofill['lxyz'       ] = lxyz
        tofill['beta'       ] = beta
        tofill['gamma'      ] = gamma
        tofill['pv_x'       ] = pv.x()
        tofill['pv_y'       ] = pv.y()
        tofill['pv_z'       ] = pv.z()
        tofill['sv_x'       ] = sv.x()
        tofill['sv_y'       ] = sv.y()
        tofill['sv_z'       ] = sv.z()
        tofill['Ds_pt'    ] = Ds.pt()
        tofill['Ds_eta'   ] = Ds.eta()        
        tofill['Ds_y'     ] = Ds.y()
        tofill['Ds_phi'   ] = Ds.phi()
        tofill['Ds_m'     ] = Ds.mass()
        tofill['Ds_status'] = Ds.status()
        tofill['bhad_pt'    ] = first_ancestor.pt()
        tofill['bhad_eta'   ] = first_ancestor.eta()
        tofill['bhad_y'     ] = first_ancestor.y()
        tofill['bhad_phi'   ] = first_ancestor.phi()
        tofill['bhad_m'     ] = first_ancestor.mass()
        tofill['bhad_q'     ] = first_ancestor.charge()
        tofill['bhad_pdgid' ] = first_ancestor.pdgId()

        # use mm everywhere
#         tofill['ctau_weight_central'] = weight_to_new_ctau(ctau_actual, ctau_pdg , ct*10.)
#         tofill['ctau_weight_up'     ] = weight_to_new_ctau(ctau_actual, ctau_up  , ct*10.)
#         tofill['ctau_weight_down'   ] = weight_to_new_ctau(ctau_actual, ctau_down, ct*10.)
# 
#         tofill['ctau_weight_central_lhe'] = weight_to_new_ctau(ctaus[0], ctau_pdg , ct*10.)
#         tofill['ctau_weight_up_lhe'     ] = weight_to_new_ctau(ctaus[0], ctau_up  , ct*10.)
#         tofill['ctau_weight_down_lhe'   ] = weight_to_new_ctau(ctaus[0], ctau_down, ct*10.)
                
        final_state_muons = [ip for ip in event.genp if abs(ip.pdgId())==13 and ip.status()==1]
        tofill['is3m'      ] = len(final_state_muons)>=3

        Ds_muons = [imu for imu in final_state_muons if isAncestor(Ds, imu)]
        Ds_muons.sort(key = lambda x : x.pt(), reverse = True)
        if len(Ds_muons)<2:
            continue

        tofill['mu1_pt' ] = Ds_muons[0].pt()
        tofill['mu1_eta'] = Ds_muons[0].eta()
        tofill['mu1_y'  ] = Ds_muons[0].y()
        tofill['mu1_phi'] = Ds_muons[0].phi()
        tofill['mu1_q'  ] = Ds_muons[0].charge()
        tofill['mu2_pt' ] = Ds_muons[1].pt()
        tofill['mu2_eta'] = Ds_muons[1].eta()
        tofill['mu2_y'  ] = Ds_muons[1].y()
        tofill['mu2_phi'] = Ds_muons[1].phi()
        tofill['mu2_q'  ] = Ds_muons[1].charge()
                
        if abs(first_ancestor.pdgId()) in [521, 523]:
            final_daus = []
            if abs(Ds.mother(0).pdgId())==521:
                the_b = Ds.mother(0)
                its_a_b = True
            else:    
                the_b = Ds.mother(0).mother(0)
                its_a_b = False

            for ii in range(the_b.numberOfDaughters()): 
                #print(Particle.from_pdgid(Ds.mother(0).daughter(ii).pdgId()).name)
                if the_b.daughter(ii).pdgId() not in [22, 521]:
                    final_daus.append(abs(the_b.daughter(ii).pdgId()))
                        
            final_daus.sort()
    
            tofill['is_Ds_mu'  ] = (final_daus==[13, 14, 443       ]) 
            tofill['is_psi2s_mu' ] = (final_daus==[13, 14, 100443    ]) 
            tofill['is_chic0_mu' ] = (final_daus==[13, 14, 10441     ]) 
            tofill['is_chic1_mu' ] = (final_daus==[13, 14, 20443     ]) 
            tofill['is_chic2_mu' ] = (final_daus==[13, 14, 445       ]) 
            tofill['is_hc_mu'    ] = (final_daus==[13, 14, 10443     ]) 
            tofill['is_Ds_tau' ] = (final_daus==[15, 16, 443       ]) 
            tofill['is_psi2s_tau'] = (final_daus==[15, 16, 100443    ]) 
            tofill['is_Ds_pi'  ] = (final_daus==[211, 443          ]) 
            tofill['is_Ds_k'   ] = (final_daus==[321, 443          ]) 
            tofill['is_Ds_3pi' ] = (final_daus==[211, 211, 211, 443]) 
            tofill['is_Ds_hc'  ] = ((final_daus==[431, 443]) or (final_daus==[433, 443])) 
            
#             if not(its_a_b):
#                 print(final_daus)
#                 import pdb ; pdb.set_trace()
            
        if   tofill['is_Ds_mu'  ]: tofill['weight'] = 1.
        elif tofill['is_psi2s_mu' ]: tofill['weight'] = 0.5474 # Psi(2S) -> J/Psi X BR, forced decay at generation
        elif tofill['is_chic0_mu' ]: tofill['weight'] = 0.0116
        elif tofill['is_chic1_mu' ]: tofill['weight'] = 0.3440
        elif tofill['is_chic2_mu' ]: tofill['weight'] = 0.1950
        elif tofill['is_hc_mu'    ]: tofill['weight'] = 0.01
        elif tofill['is_Ds_tau' ]: tofill['weight'] = 1. 
        elif tofill['is_psi2s_tau']: tofill['weight'] = 0.5474
        elif tofill['is_Ds_pi'  ]: tofill['weight'] = 1.
        elif tofill['is_Ds_k'   ]: tofill['weight'] = 1.
        elif tofill['is_Ds_3pi' ]: tofill['weight'] = 1.
        elif tofill['is_Ds_hc'  ]: tofill['weight'] = 1.
        else                       : tofill['weight'] = -1.

        if len(final_state_muons)>=3:
            final_state_muons_non_Ds = [imu for imu in final_state_muons if imu not in Ds_muons]
            final_state_muons_non_Ds.sort(key = lambda x : x.pt(), reverse = True)
            
            extra_mu = final_state_muons_non_Ds[0]
 
            tofill['mu3_pt' ] = extra_mu.pt()
            tofill['mu3_eta'] = extra_mu.eta()
            tofill['mu3_y'  ] = extra_mu.y()
            tofill['mu3_phi'] = extra_mu.phi()
            tofill['mu3_q'  ] = extra_mu.charge()
           
            three_mu_p4 = extra_mu.p4() + Ds_muons[0].p4() + Ds_muons[1].p4()
            b_scaled_p4 = three_mu_p4 * (6.275/three_mu_p4.mass())

            tofill['mmm_pt' ] = three_mu_p4.pt()
            tofill['mmm_eta'] = three_mu_p4.eta()
            tofill['mmm_y'  ] = three_mu_p4.y()
            tofill['mmm_phi'] = three_mu_p4.phi()
            tofill['mmm_m'  ] = three_mu_p4.mass()
            tofill['mmm_q'  ] = extra_mu.charge()
            
            tofill['dr_Ds_m'] = deltaR(extra_mu, Ds)

            tofill['n_extra_mu'] = len(final_state_muons_non_Ds)

            # how the hell does one boost LorentzVectors back and forth?!
            # using TLorentzVectors of course... shit.
            three_mu_p4_tlv = ROOT.TLorentzVector() ; three_mu_p4_tlv.SetPtEtaPhiE(three_mu_p4.pt(), three_mu_p4.eta(), three_mu_p4.phi(), three_mu_p4.energy())
            b_scaled_p4_tlv = ROOT.TLorentzVector() ; b_scaled_p4_tlv.SetPtEtaPhiE(b_scaled_p4.pt(), b_scaled_p4.eta(), b_scaled_p4.phi(), b_scaled_p4.energy())
            Ds_p4_tlv     = ROOT.TLorentzVector() ; Ds_p4_tlv    .SetPtEtaPhiE(Ds.p4()  .pt(), Ds.p4()  .eta(), Ds.p4()  .phi(), Ds.p4()  .energy())
            extra_mu_p4_tlv = ROOT.TLorentzVector() ; extra_mu_p4_tlv.SetPtEtaPhiE(extra_mu   .pt(), extra_mu   .eta(), extra_mu   .phi(), extra_mu   .energy())

            three_mu_p4_boost = three_mu_p4_tlv.BoostVector()
            b_scaled_p4_boost = b_scaled_p4_tlv.BoostVector()
            Ds_p4_boost     = Ds_p4_tlv    .BoostVector()
            
            extra_mu_p4_in_b_rf    = extra_mu_p4_tlv.Clone(); extra_mu_p4_in_b_rf   .Boost(-b_scaled_p4_boost)
            extra_mu_p4_in_Ds_rf = extra_mu_p4_tlv.Clone(); extra_mu_p4_in_Ds_rf.Boost(-Ds_p4_boost    )
            
            tofill['m2_miss'    ] = (b_scaled_p4 - extra_mu.p4() - Ds_muons[0].p4() - Ds_muons[1].p4()).mass2()
            tofill['pt_miss_sca'] = b_scaled_p4.pt() - extra_mu.pt() - Ds_muons[0].pt() - Ds_muons[1].pt()
            tofill['pt_miss_vec'] = (b_scaled_p4 - extra_mu.p4() - Ds_muons[0].p4() - Ds_muons[1].p4()).pt()
            tofill['q2'         ] = (b_scaled_p4- Ds.p4()).mass2()
            # tofill['e_star_mu3' ] = extra_mu.p4().E() * np.cosh(extra_mu.p4().Rapidity() - b_scaled_p4.Rapidity())
            # tofill['e_hash_mu3' ] = extra_mu.p4().E() * np.cosh(extra_mu.p4().Rapidity() - Ds.p4().Rapidity())
            tofill['e_star_mu3' ] = extra_mu_p4_in_b_rf   .E()
            tofill['e_hash_mu3' ] = extra_mu_p4_in_Ds_rf.E()
            tofill['ptvar'      ] = Ds.pt() - extra_mu.pt()

        # fill only if it comes from  a Bc
        if abs(first_ancestor.pdgId()) in [521, 523]:
            ntuple.Fill(array('f', tofill.values()))

    if verbose:
        if len(bs)>1: # and len(Dss)>1:
            print('--> b hadrons')
            for aa, ib in enumerate(bs):
                try:
                    print('---->', Particle.from_pdgid(ib.pdgId()))
                except:
                    print('---->', ib.pdgId())
                for idau in range(ib.numberOfDaughters()):
                    try: 
                        print('\t\t %d]-th B\t'%aa, Particle.from_pdgid(ib.daughter(idau).pdgId()))
                    except: 
                        print('\t\t %d]-th B\t'%aa, ib.daughter(idau).pdgId())
        if len(muons)<3:
            print('--> muons')
        if len(Ds_mesons)>1:
            print('--> Ds_mesons')
            for ij in Ds_mesons:
                if abs(ij.daughter(0).pdgId())!=13:
                  pass
    
fout.cd()
ntuple.Write()
fout.Close()
    
