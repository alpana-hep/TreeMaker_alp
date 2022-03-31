import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL17
Summer20UL17samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 3609634),
    MCSample('WWG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 1736000, 1504408),
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 171000, 154830),
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 178000, 161398),
    MCSample('WW_TuneCP5_13TeV-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 15634000),
    MCSample('WZG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 1400000, 1234846),
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 298000, 268438),
    MCSample('WZ_TuneCP5_13TeV-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 7889000),
    MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 40839000),
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 178000, 158612),
    MCSample('ZZ_TuneCP5_13TeV-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 2706000),
    MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 13882000, 9037288),
    MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 8433998),
    MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 8507203),
    MCSample('tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 9530000, 2578040),
    MCSample('TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 249133364, 90379032),
    MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 14196000, 6990534),
    MCSample('TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4292000, 2146996),
    MCSample('TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 6596000, 3323040),
    MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 13982000, 6946010),
    MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 7460671, 4044869),
    MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 655018, 359006),
    MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 3534208, 1261452),
    MCSample('TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 10018000),
    MCSample('TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 10697000),
    MCSample('TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 19066000),
    MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 350000),
    MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 360000),
    MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 698000),
    MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 350000),
    MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 327000),
    MCSample('TTTJ_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 354000),
    MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 360000),
    MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 10351000, 4526556),
    MCSample('TTTW_TuneCP5_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 360000),
    MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 9883355, 3251105),
    MCSample('TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 9565099),
    MCSample('TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 14094979),
    MCSample('TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 12181705),
    MCSample('TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 15594718),
    MCSample('TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 10410425),
    MCSample('TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 2039938),
    MCSample('TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 981339),
    MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 19781000),
    MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 28896000),
    MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 10994000),
    MCSample('QCD_Pt_15to30_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 19742000),
    MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 29811000),
    MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 5488000),
    MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 2997000),
    MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 55690000),
    MCSample('QCD_Pt_30to50_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 19829000),
    MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 1000000),
    MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 50885000),
    MCSample('QCD_Pt_50to80_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 19997000),
    MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 67379000),
    MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 36890000),
    MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 29403000),
    MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 18955253),
    MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4802716),
    MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 12513057),
    MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 1480047),
    MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 5543804),
    MCSample('DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 5278417),
    MCSample('DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 12205958),
    MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4506887),
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 205238822), # subtotal = 103344974
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9_ext1-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 205238822), # subtotal = 101893848
    MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 10034997),
    MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 33884844),
    MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 9022800),
    MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 8330226),
    MCSample('ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 18983897),
    MCSample('ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 267125),
    MCSample('ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 17349597),
    MCSample('ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 176201),
    MCSample('ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 13963690),
    MCSample('ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4418971),
    MCSample('ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 1513585),
    MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 47424468),
    MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4955636),
    MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42602407),
    MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 1185699),
    MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 5468473),
    MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 5545298),
    MCSample('WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 44736228),
    MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 5088483),
    MCSample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 78981243),
    MCSample('WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 15968057),
    MCSample('WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 9927793),
    MCSample('WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 14667933),
    MCSample('WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 14722417),
    MCSample('QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 10256089),
    MCSample('QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 54760426),
    MCSample('QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 7701876),
    MCSample('QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 4112573),
    MCSample('QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42714435),
    MCSample('QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 43589739),
    MCSample('QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 36194860),
    MCSample('QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 26243010),
    MCSample('QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 34051754),
    MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 106724000),
    MCSample('TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42752000),
    MCSample('TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 39445000),
    MCSample('TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42842000),
    MCSample('TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 40630000),
    MCSample('TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 40292000),
    MCSample('TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 39412000),
    MCSample('TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 41048000),
    MCSample('TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 41404000),
    MCSample('TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42742000),
    MCSample('TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 42362000),
    MCSample('TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 41233000),
    MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 355332000),
    MCSample('TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 127442000),
    MCSample('TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 135034000),
    MCSample('TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 139108000),
    MCSample('TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 134315999),
    MCSample('TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 132984000),
    MCSample('TTToSemiLeptonic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 133000000),
    MCSample('TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 138001000),
    MCSample('TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 132664000),
    MCSample('TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 140284000),
    MCSample('TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 133926000),
    MCSample('TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 131182000),
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v2', 'RunIISummer20UL17MiniAODv2', 'Constant', 235719999),
    MCSample('TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 90270000),
    MCSample('TTToHadronic_TuneCP5down_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 97159000),
    MCSample('TTToHadronic_TuneCP5up_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 96275999),
    MCSample('TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 95446000),
    MCSample('TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 99480000),
    MCSample('TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 97198000),
    MCSample('TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 90427000),
    MCSample('TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 97807000),
    MCSample('TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 91129000),
    MCSample('TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 99154000),
    MCSample('TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mc2017_realistic_v9-v1', 'RunIISummer20UL17MiniAODv2', 'Constant', 96307000),
]
