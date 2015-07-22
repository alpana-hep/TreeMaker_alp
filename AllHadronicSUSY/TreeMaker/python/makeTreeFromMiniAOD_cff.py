# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outFileName,
reportEveryEvt=10,
testFileName="",
Global_Tag="",
numProcessedEvt=1000,
lostlepton=False,
hadtau=False,
tagandprobe=False,
applybaseline=False,
doZinv=False,
debugtracks=False,
geninfo=True,
tagname="PAT",
jsonfile="",
applyjec=False,
):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = Global_Tag

    # CMSSW version sniffing
    CMSSWVER = os.getenv("CMSSW_VERSION")
    CMSSWVER_parts = CMSSWVER.split("_")
    is74X = False
    if int(CMSSWVER_parts[1])==7 and int(CMSSWVER_parts[2])>=4:
        is74X = True
        print "Configuring for 74X"

    # define if mt cut should be applied and the value (less than 0 means no cut)
    mtcut = cms.double(100)
    if tagandprobe:
        mtcut=-100
        print "Doing tagandprobe"
    print "Calulation with mtcut: "+ str(mtcut)

    # log output
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = reportEveryEvt
    process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
    )

    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numProcessedEvt)
    )
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(testFileName)
    )
    if len(jsonfile)>0: process.source.lumisToProcess = LumiList.LumiList(filename = jsonfile).getVLuminosityBlockRange()

    # output file
    process.TFileService = cms.Service("TFileService",
        fileName = cms.string(outFileName+".root")
    )
    # branches for treemaker
    RecoCandVector       = cms.vstring() 
    VarsDouble           = cms.vstring()
    VarsInt              = cms.vstring()
    VarsBool             = cms.vstring()
    VectorTLorentzVector = cms.vstring()
    VectorDouble         = cms.vstring()
    VectorString         = cms.vstring()
    VectorInt            = cms.vstring()
    
    # sequence for baseline producers
    process.Baseline = cms.Sequence()

    # configure treemaker
    from AllHadronicSUSY.TreeMaker.treeMaker import TreeMaker
    process.TreeMaker2 = TreeMaker.clone(
        TreeName             = cms.string("PreSelection"),
        VarsRecoCand         = RecoCandVector, 
        VarsDouble           = VarsDouble,
        VarsInt              = VarsInt,
        VarsBool             = VarsBool,
        VectorTLorentzVector = VectorTLorentzVector,
        VectorDouble         = VectorDouble,
        VectorInt            = VectorInt,
        VectorString         = VectorString,
    )

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Standard producers
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.WeightProducer.getWeightProducer_cff import getWeightProducer
    process.WeightProducer = getWeightProducer(testFileName)
    process.WeightProducer.Lumi                       = cms.double(4000)
    process.WeightProducer.PU                         = cms.int32(0) # PU S10 3 for S10 2 for S7
    process.WeightProducer.FileNamePUDataDistribution = cms.string("NONE")
    process.Baseline += process.WeightProducer
    VarsDouble.extend(['WeightProducer:weight(Weight)'])

    ## ----------------------------------------------------------------------------------------------
    ## PrimaryVertices
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.primaryvertices_cfi import primaryvertices
    process.NVtx = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    if geninfo :
        process.genParticles = cms.EDProducer("genParticlesProducer",
            genCollection = cms.untracked.InputTag("prunedGenParticles"),
            debug = cms.untracked.bool(False)
        )
        process.Baseline += process.genParticles
        VectorTLorentzVector.append("genParticles(genParticles)")
        VectorInt.append("genParticles:PDGid(genParticles_PDGid)")
        #VectorInt.append("genParticles:parent(genParticles_parent)")

    ## ----------------------------------------------------------------------------------------------
    ## IsoTracks
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationCounter

    process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2),
        pdgId               = cms.int32(11),
        mTCut               = mtcut,
    )

    process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(5.0),
        isoCut              = cms.double(0.2), 
        pdgId               = cms.int32(13),
        mTCut               = mtcut,
    )

    process.IsolatedPionTracksVeto = trackIsolationFilter.clone(
        doTrkIsoVeto        = False,
        vertexInputTag      = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pfCandidatesTag     = cms.InputTag("packedPFCandidates"),
        dR_ConeSize         = cms.double(0.3),
        dz_CutValue         = cms.double(0.1),
        minPt_PFCandidate   = cms.double(10.0),
        isoCut              = cms.double(0.1),
        pdgId               = cms.int32(211),
        mTCut               = mtcut,
    )

    process.Baseline += process.IsolatedElectronTracksVeto
    process.Baseline += process.IsolatedMuonTracksVeto
    process.Baseline += process.IsolatedPionTracksVeto

    VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

    if debugtracks:
        #NB: this increases the runtime and size of ntuples by ~10x
        #do not turn on unless you really want to save all the isotrack quantities!!!
        #just store the full set of isotrack quantities once
        process.IsolatedPionTracksVeto.debug = cms.bool(True)
        VarsBool.extend(['IsolatedPionTracksVeto:GoodVtx(GoodVtx)'])
        VectorTLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(pfcands)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(pfcands_trkiso)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(pfcands_dzpv)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(pfcands_mT)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(pfcands_chg)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(pfcands_id)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## Electrons/Muons
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.leptonproducer_cfi import leptonproducer

    process.LeptonsNew = leptonproducer.clone(
        MuonTag          = cms.InputTag('slimmedMuons'),
        ElectronTag      = cms.InputTag('slimmedElectrons'),
        PrimaryVertex    = cms.InputTag('offlineSlimmedPrimaryVertices'),
        minElecPt        = cms.double(10),
        maxElecEta       = cms.double(2.5),
        minMuPt          = cms.double(10),
        maxMuEta         = cms.double(2.4),
        UseMiniIsolation = cms.bool(True),
        muIsoValue       = cms.double(0.2),
        elecIsoValue     = cms.double(0.1), # only has an effect when used with miniIsolation
        METTag           = cms.InputTag('slimmedMETs'), 
    )
    process.Baseline += process.LeptonsNew
    VarsInt.extend(['LeptonsNew(Leptons)'])
    RecoCandVector.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])

    process.LeptonsNewTag = leptonproducer.clone(
        MuonTag          = cms.InputTag('slimmedMuons'),
        ElectronTag      = cms.InputTag('slimmedElectrons'),
        PrimaryVertex    = cms.InputTag('offlineSlimmedPrimaryVertices'),
        minElecPt        = cms.double(20),
        maxElecEta       = cms.double(2.5),
        minMuPt          = cms.double(20),
        maxMuEta         = cms.double(2.4),
        UseMiniIsolation = cms.bool(True),
        muIsoValue       = cms.double(0.2),
        elecIsoValue     = cms.double(0.1), # only has an effect when used with miniIsolation
        METTag           = cms.InputTag('slimmedMETs'), 
    )
    process.Baseline += process.LeptonsNewTag
    VarsInt.extend(['LeptonsNewTag(TagLeptonHighPT)'])

    ## ----------------------------------------------------------------------------------------------
    ## Photons
    ## ----------------------------------------------------------------------------------------------
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
        photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
        electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",tagname),
        beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot","","RECO"),
        ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
        debug                  = cms.untracked.bool(False)
    )
    process.Baseline += process.goodPhotons
    # good photon tag is InputTag('goodPhotons','bestPhoton')
    RecoCandVector.append("goodPhotons:bestPhoton")
    VarsInt.append("goodPhotons:NumPhotons")
    
    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------
    
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    JetTag = cms.InputTag('slimmedJets')
    if applyjec:
        JECPatch = cms.string('sqlite_file:PHYS14_V4_MC.db')
        if os.getenv('GC_CONF'): 
            JECPatch = cms.string('sqlite_file:../src/PHYS14_V4_MC.db')

        process.load("CondCore.DBCommon.CondDBCommon_cfi")
        from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
        process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
            connect = JECPatch,
            toGet   = cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_PHYS14_V4_MC_AK4PFchs"),
                    label  = cms.untracked.string("AK4PFchs")
                )
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
        
        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
        process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
            src     = cms.InputTag("slimmedJets"),
            levels  = ['L1FastJet',
                      'L2Relative',
                      'L3Absolute'],
            payload = 'AK4PFchs' # Make sure to choose the appropriate levels and payload here!
        )
        
        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
        process.patJetsReapplyJEC = patJetsUpdated.clone(
            jetSource = cms.InputTag("slimmedJets"),
            jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
        )
        
        process.Baseline += process.patJetCorrFactorsReapplyJEC
        process.Baseline += process.patJetsReapplyJEC
        
        JetTag = cms.InputTag('patJetsReapplyJEC')

    ## ----------------------------------------------------------------------------------------------
    ## GoodJets
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
        TagMode                   = cms.bool(True),
        JetTag                    = JetTag,
        maxJetEta                 = cms.double(5.0),
        maxMuFraction             = cms.double(2),
        minNConstituents          = cms.double(2),
        maxNeutralFraction        = cms.double(0.90),
        maxPhotonFraction         = cms.double(0.95),
        minChargedMultiplicity    = cms.double(0),
        minChargedFraction        = cms.double(0),
        maxChargedEMFraction      = cms.double(0.99),
        jetPtFilter               = cms.double(30),
        ExcludeLepIsoTrackPhotons = cms.bool(True),
        JetConeSize               = cms.double(0.04),
        MuonTag                   = cms.InputTag('LeptonsNew:IdIsoMuon'),
        ElecTag                   = cms.InputTag('LeptonsNew:IdIsoElectron'),
        IsoElectronTrackTag       = cms.InputTag('IsolatedElectronTracksVeto'),
        IsoMuonTrackTag           = cms.InputTag('IsolatedMuonTracksVeto'),
        IsoPionTrackTag           = cms.InputTag('IsolatedPionTracksVeto'),
        PhotonTag                 = cms.InputTag('goodPhotons','bestPhoton'),
    )
    process.Baseline += process.GoodJets
    VarsBool.extend(['GoodJets(JetID)'])

    ## ----------------------------------------------------------------------------------------------
    ## MET Filters
    ## ----------------------------------------------------------------------------------------------
    
    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree

    from AllHadronicSUSY.Utils.filterdecisionproducer_cfi import filterDecisionProducer
    process.METFilters = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(''),
        filterName  = cms.string("Flag_METFilters"),
    )
    process.Baseline += process.METFilters
    VarsInt.extend(['METFilters'])

    process.CSCTightHaloFilter = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(''),
        filterName  = cms.string("Flag_CSCTightHaloFilter"),
    )
    process.Baseline += process.CSCTightHaloFilter
    VarsInt.extend(['CSCTightHaloFilter'])

    process.HBHENoiseFilter = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(''),
        filterName  = cms.string("Flag_HBHENoiseFilter"),
    )
    process.Baseline += process.HBHENoiseFilter
    VarsInt.extend(['HBHENoiseFilter'])

    process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
        trigTagArg1 = cms.string('TriggerResults'),
        trigTagArg2 = cms.string(''),
        trigTagArg3 = cms.string(''),
        filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
    )
    process.Baseline += process.EcalDeadCellTriggerPrimitiveFilter
    VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])

    ## ----------------------------------------------------------------------------------------------
    ## Triggers
    ## ----------------------------------------------------------------------------------------------

    # The trigger results are saved to the tree as a vector
    # Two vectors are saved:
    # 1) names of the triggers
    # 2) trigger results
    # the indexing of these two vectors must match
    # If the version number of the input trigger name is omitted,
    # any matching trigger will be included (default behavior)

    from AllHadronicSUSY.Utils.triggerproducer_cfi import triggerProducer
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        triggerNameList = cms.vstring( # list of trigger names
            'HLT_PFHT350_PFMET100_NoiseCleaned_v',
            'HLT_PFMET170_NoiseCleaned_v',
            'HLT_PFMET170_NoiseCleaned_v',
            'HLT_PFHT350_v',
            'HLT_PFHT800_v',
            'HLT_PFHT900_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v',
            'HLT_IsoMu17_eta2p1_v',
            'HLT_PFHT350_PFMET120_NoiseCleaned_v',
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Photon75_v',
            'HLT_Photon90_v',
            'HLT_Photon90_CaloIdL_PFHT500_v',
            'HLT_DoubleEle8_CaloIdM_Mass8_PFHT300_v',
            'HLT_Ele27_eta2p1_WP85_Gsf_v',
            'HLT_IsoMu20_eta2p1_IterTrk02_v',
            'HLT_DoubleMu8_Mass8_PFHT300_v',
        )
    )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:PassTrigger'])
    VectorString.extend(['TriggerProducer:TriggerNames'])

    ## ----------------------------------------------------------------------------------------------
    ## HT
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
    process.HTJets = SubJetSelection.clone(
        JetTag = cms.InputTag('GoodJets'),
        MinPt  = cms.double(30),
        MaxEta = cms.double(2.4),
    )
    process.Baseline += process.HTJets
    
    from AllHadronicSUSY.Utils.htdouble_cfi import htdouble
    process.HT = htdouble.clone(
        JetTag = cms.InputTag('HTJets'),
    )
    process.Baseline += process.HT
    VarsDouble.extend(['HT'])
    
    ## ----------------------------------------------------------------------------------------------
    ## NJets
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.njetint_cfi import njetint
    process.NJets = njetint.clone(
        JetTag = cms.InputTag('HTJets'),
    )
    process.Baseline += process.NJets
    VarsInt.extend(['NJets'])
    
    ## ----------------------------------------------------------------------------------------------
    ## BTags
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.btagint_cfi import btagint
    process.BTags = btagint.clone(
        JetTag       = cms.InputTag('HTJets'),
        BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
        BTagCutValue = cms.double(0.814)
    )
    if is74X: process.BTags.BTagInputTag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.Baseline += process.BTags
    VarsInt.extend(['BTags'])
    
    ## ----------------------------------------------------------------------------------------------
    ## MHT
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
    process.MHTJets = SubJetSelection.clone(
        JetTag = cms.InputTag('GoodJets'),
        MinPt  = cms.double(30),
        MaxEta = cms.double(5.0),
    )
    process.Baseline += process.MHTJets
    
    from AllHadronicSUSY.Utils.mhtdouble_cfi import mhtdouble
    process.MHT = mhtdouble.clone(
        JetTag  = cms.InputTag('MHTJets'),
    )
    process.Baseline += process.MHT
    VarsDouble.extend(['MHT:Pt(MHT)','MHT:Phi(MHT_Phi)'])
    
    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('HT'),
        CutValue  = cms.double('500'),
    )
    process.MHTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('MHT:Pt'),
        CutValue  = cms.double('200'),
    )
    if applybaseline:
        process.Baseline += process.HTFilter
        #process.Baseline += process.MHTFilter

    ## ----------------------------------------------------------------------------------------------
    ## DeltaPhi
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.deltaphidouble_cfi import deltaphidouble
    process.DeltaPhi = deltaphidouble.clone(
        DeltaPhiJets = cms.InputTag('HTJets'),
        MHTJets      = cms.InputTag("MHTJets"),
    )
    process.Baseline += process.DeltaPhi
    VarsDouble.extend(['DeltaPhi:DeltaPhi1','DeltaPhi:DeltaPhi2','DeltaPhi:DeltaPhi3'])
    
    ## ----------------------------------------------------------------------------------------------
    ## MET
    ## ----------------------------------------------------------------------------------------------
    from AllHadronicSUSY.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = cms.InputTag("slimmedMETs"),
        JetTag = cms.InputTag('HTJets'),
    )
    process.Baseline += process.MET
    VarsDouble.extend(['MET:minDeltaPhiN','MET:DeltaPhiN1','MET:DeltaPhiN2','MET:DeltaPhiN3','MET:Pt(METPt)','MET:Phi(METPhi)'])

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    # sequence for optional producers
    process.AdditionalSequence = cms.Sequence()
    
    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------
    if hadtau:
        from AllHadronicSUSY.TreeMaker.doHadTauBkg import doHadTauBkg
        process = doHadTauBkg(process,is74X,geninfo)
    
    ## ----------------------------------------------------------------------------------------------
    ## Shared processes for lost lepton, tag and probe
    ## ----------------------------------------------------------------------------------------------
    if lostlepton or tagandprobe:
        from AllHadronicSUSY.TreeMaker.doProcessesForLLTP import doProcessesForLLTP
        process = doProcessesForLLTP(process,is74X,geninfo)
    
    ## ----------------------------------------------------------------------------------------------
    ## Tag And Probe
    ## ----------------------------------------------------------------------------------------------
    if tagandprobe:
        from AllHadronicSUSY.TreeMaker.doTagAndProbe import doTagAndProbe
        process = doTagAndProbe(process,geninfo)

    ## ----------------------------------------------------------------------------------------------
    ## Lost Lepton Background
    ## ----------------------------------------------------------------------------------------------
    if lostlepton:
        from AllHadronicSUSY.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
        process = doLostLeptonBkg(process,geninfo)

    ## ----------------------------------------------------------------------------------------------
    ## Zinv Background
    ## ----------------------------------------------------------------------------------------------
    if doZinv:
        from AllHadronicSUSY.TreeMaker.doZinvBkg import doZinvBkg
        process = doZinvBkg(process,is74X)

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Final steps
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # create the process path
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.WriteTree = cms.Path(
        process.Baseline *
        process.AdditionalSequence *
#        process.dump *
        process.TreeMaker2
    )

