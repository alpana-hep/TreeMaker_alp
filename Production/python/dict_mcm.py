from collections import OrderedDict

datasets = OrderedDict([
("TTJets_Tune*madgraphMLM-pythia8",[0]),
("TTJets_SingleLeptFromT_Tune",[0,1]),
("TTJets_SingleLeptFromTbar_Tune",[0,1]),
("TTJets_DiLept_Tune",[0,1]),
("TTJets_SingleLeptFromT_genMET-150_Tune",[0,1]),
("TTJets_SingleLeptFromTbar_genMET-150_Tune",[0,1]),
("TTJets_DiLept_genMET-150_Tune",[0,1]),
("TTJets_HT-600to800",[0,1]),
("TTJets_HT-800to1200",[0,1]),
("TTJets_HT-1200to2500",[0,1]),
("TTJets_HT-2500toInf",[0,1]),
("TT_Tune",[0,1]),
("TTTo2L2Nu_Tune*powheg-pythia8",[0]),
("TTToHadronic_Tune*powheg-pythia8",[0]),
("TTToSemiLeptonic_Tune*powheg-pythia8",[0]),
("WJetsToLNu_Tune",[0,1,2]),
("WJetsToLNu_HT-70To100",[0,1,2]), # Needed for 2016, but won't be there 2017
("WJetsToLNu_HT-100To200",[0,1,2]),
("WJetsToLNu_HT-200To400",[0,1,2]),
("WJetsToLNu_HT-400To600",[0,1]),
("WJetsToLNu_HT-600To800",[0,1]),
("WJetsToLNu_HT-800To1200",[0,1]),
("WJetsToLNu_HT-1200To2500",[0,1]),
("WJetsToLNu_HT-2500ToInf",[0,1]),
("QCD_Pt_80to120_Tune",[0,1]),
("QCD_Pt_120to170_Tune",[0,1]),
("QCD_Pt_170to300_Tune",[0,1]),
("QCD_Pt_300to470_Tune",[0,1]),
("QCD_Pt_470to600_Tune",[0,1]),
("QCD_Pt_600to800_Tune",[0,1]),
("QCD_Pt_800to1000_Tune",[0,1]),
("QCD_Pt_1000to1400_Tune",[0,1]),
("QCD_Pt_1400to1800_Tune",[0,1]),
("QCD_Pt_1800to2400_Tune",[0,1]),
("QCD_Pt_2400to3200_Tune",[0,1]),
("QCD_Pt_3200toInf_Tune",[0,1]),
("QCD_Pt-15to20_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-20to30_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-30to50_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-50to80_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-80to120_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-120to170_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-170to300_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-300to470_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-470to600_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-600to800_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-800to1000_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-1000toInf_MuEnrichedPt5_Tune",[0]),
("QCD_Pt-15to7000_Tune*_Flat2018_13TeV_pythia8",[0,1]),
("QCD_HT200to300_Tune",[0,1]),
("QCD_HT300to500_Tune",[0,1]),
("QCD_HT500to700_Tune",[0,1]),
("QCD_HT700to1000_Tune",[0,1]),
("QCD_HT1000to1500_Tune",[0,1]),
("QCD_HT1500to2000_Tune",[0,1]),
("QCD_HT2000toInf_Tune",[0,1]),
("DYJetsToLL_M-50_HT-100to200",[0,1]),
("DYJetsToLL_M-50_HT-200to400",[0,1]),
("DYJetsToLL_M-50_HT-400to600",[0,1]),
("DYJetsToLL_M-50_HT-600to800",[0,1]),
("DYJetsToLL_M-50_HT-800to1200",[0,1]),
("DYJetsToLL_M-50_HT-1200to2500",[0,1]),
("DYJetsToLL_M-50_HT-2500toInf",[0,1]),
("DYJetsToLL_M-50_Tune*madgraphMLM-pythia8",[0,1]),
("ZJetsToNuNu_HT-100To200",[0,1]),
("ZJetsToNuNu_HT-200To400",[0,1]),
("ZJetsToNuNu_HT-400To600",[0,1]),
("ZJetsToNuNu_HT-600To800",[0,1]),
("ZJetsToNuNu_HT-800To1200",[0,1]),
("ZJetsToNuNu_HT-1200To2500",[0,1]),
("ZJetsToNuNu_HT-2500ToInf",[0,1]),
("GJets_HT-100To200",[0,1]),
("GJets_HT-200To400",[0,1]),
("GJets_HT-400To600",[0,1]),
("GJets_HT-600ToInf",[0,1]),
("GJets_DR-0p4_HT-100To200",[0]),
("GJets_DR-0p4_HT-200To400",[0]),
("GJets_DR-0p4_HT-400To600",[0]),
("GJets_DR-0p4_HT-600ToInf",[0]),
("ST_s-channel_4f_leptonDecays",[0,1]),
("ST_s-channel_4f_InclusiveDecays",[0,1]),
("ST_t-channel_top_4f_inclusiveDecays",[0,1]),
("ST_t-channel_antitop_4f_inclusiveDecays",[0,1]),
("ST_tW_antitop_5f_NoFullyHadronicDecays",[0,1,2]),
("ST_tW_top_5f_NoFullyHadronicDecays",[0,1,2]),
("ST_tW_antitop_5f_inclusiveDecays",[0,1]),
("ST_tW_top_5f_inclusiveDecays",[0,1]),
("tZq_W_lept_Z_hadron_4f_ckm_NLO",[0]),
("WGJets_MonoPhoton_PtG-40to130_Tune",[0]),
("WGJets_MonoPhoton_PtG-130_Tune",[0]),
("WWTo2L2Nu_13TeV-powheg",[0]),
("WWTo1L1Nu2Q_13TeV_amcatnloFXFX",[0]),
("WZTo1L1Nu2Q_13TeV_amcatnloFXFX",[0]),
("WZTo1L3Nu_13TeV_amcatnloFXFX",[0]),
("ZGTo2NuG_Tune*_13TeV-amcatnloFXFX",[0]),
("ZZTo2L2Q_13TeV_amcatnloFXFX",[0]),
("ZZTo2Q2Nu_13TeV_amcatnloFXFX",[0]),
("TTZToLLNuNu_M-10_Tune*_13TeV-amcatnlo",[0,1,2]),
("TTZToQQ_Tune*_13TeV-amcatnlo",[0]),
("TTWJetsToLNu_Tune*_13TeV-amcatnloFXFX",[0,1,2]),
("TTWJetsToQQ_Tune*_13TeV-amcatnloFXFX",[0]),
("TTGJets_Tune*_13TeV-amcatnloFXFX",[0,1]),
("ttHJetToNonbb_M125",[0,1]),
("ttHJetTobb_M125",[0,1]),
("TTGamma_SingleLeptFromT_Tune",[0]),
("TTGamma_SingleLeptFromTbar_Tune",[0]),
("TTGamma_Dilept_Tune",[0]),
("TTTT_Tune*_13TeV-amcatnlo",[0]),
("TTHH_Tune*_13TeV",[0]),
("TTTW_Tune*_13TeV",[0]),
("TTWH_Tune*_13TeV",[0]),
("TTWW_Tune*_13TeV",[0,1]),
("TTWZ_Tune*_13TeV",[0]),
("TTZH_Tune*_13TeV",[0]),
("TTZZ_Tune*_13TeV",[0]),
("TTTJ_Tune*_13TeV",[0]),
("WWWW_Tune*_13TeV",[0]), # For V17
("WWW_*_13TeV-amcatnlo",[0]),
("WWZ_*_13TeV-amcatnlo",[0]),
("WZZ_Tune*_13TeV-amcatnlo",[0]),
("ZZZ_Tune*_13TeV-amcatnlo",[0]),
("SMS-T1tttt_mGluino-*_mLSP-*",[0]),
("SMS-T1qqqq_mGluino-*_mLSP-*",[0]),
("SMS-T1bbbb_mGluino-*_mLSP-*",[0]),
("SMS-T2tt_mStop-*_mLSP-*",[0]),
("SMS-T5qqqqZH-mGluino*",[0]),
("SMS-T5qqqqWW-mGluino*",[0]),
("SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1",[0]),
("SMS-TChiWZ_ZToLL_mZMin-0p1",[0]),
("SMS-TChiHH_HToBB_HToBB",[0]),
("RPV_2t6j_mStop-*_mN1-100",[0]),
("StealthSYY_2t6j_mStop-*_mSo-100",[0]),
("StealthSYY_2t6j_mStop-*_mN1-100",[0]), #Needed for Summer16MiniAODv3 because of a name mixup
("StealthSHH_2t4b_mStop-*_mSo-100",[0]),
])
