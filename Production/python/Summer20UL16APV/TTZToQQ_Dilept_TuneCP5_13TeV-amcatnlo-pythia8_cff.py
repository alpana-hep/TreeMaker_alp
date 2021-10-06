import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/02D7DAEC-CB8E-AD48-865C-A3137C90F418.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0A832233-B75A-6D4B-ADCA-17016191084C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0B5D1A7C-1D46-FF46-8DB8-78460AD5424C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/0BD0ED99-F006-F54B-B6BF-160790874922.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/216D6DB4-1EA7-BA43-9B06-38634C450944.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/26884C4E-1C3E-D14C-AF08-EA14FE153D1E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2ABD0187-E393-174A-91DD-66AC37F46463.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/2FE34E21-79DA-2742-B4C4-267ED41602B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/301BBE81-A7E2-334F-BFCC-76BEE9715DF8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/32F24FAB-81AD-4245-A76A-C3043EB84DAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/33340A2A-F667-9A44-820B-C73FC4402C9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/383F207A-55B3-A441-9DD5-762F2B35CCE3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3DCDDE5E-9FE3-7144-94E3-B02CB4DA941A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3DF11E24-FAF5-7343-A2A3-D5A57D82438C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3E4532C8-6BA6-5B47-9EE9-202CB61BA9F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/44D67313-D030-3248-BD39-D59522D621B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/48D94C2A-0068-5249-AEC6-16DBE7D5FD74.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/600D8B43-6A16-9247-8A06-2AA260711424.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/61E28523-F426-0642-A4FC-463F4636D022.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/65765A7F-FB7C-8D49-B88D-02B92DF56D7B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/66548EB2-B46B-7D44-9EF2-5F537883A665.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/775B6175-7FAC-944A-B904-B67CF4782809.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/799B05BE-A6F9-B24F-8EA9-9FD8CF36D57C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/81B30068-8824-E44E-B182-1B8B86D1C5EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/85B30E0D-4AB4-7144-A651-43931F540964.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/870E79BC-DA85-E840-995A-61AB7BC78497.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/890CBD8B-85DD-724F-8E05-206DCAF35658.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/91012778-16F7-9B49-9200-97ECC025D51C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/983306B6-7ADE-4849-BE4D-3F1D2BDCF4DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9886186D-EEB3-524F-9AB6-DA05E3570732.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9C8B54E9-CEED-F843-8A5B-C8C3365223D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A0548E2F-737C-DE44-BC90-47DE09E73075.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B4E03CD3-A145-FB4D-A9EB-72AAAB890761.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B77661CB-EA67-FD42-BF06-809155D226C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/BE70BAFB-140E-0B4A-85E4-3081AC29C044.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C5655AF9-7028-134D-9336-F1CB29E49F4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C5B60EC1-1387-DE43-8993-53C2DB1ADC16.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C9DB88FC-4743-5F4B-A1F0-C47AFC6DEC30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/DABD8C34-C6DB-FC42-A4C3-6FA55547EC48.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E7A9D177-49AB-314C-B0CE-310FA9287B68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EC172C3B-9413-854E-9A12-FF6EDE253CDE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/EDDAB884-78CD-5641-B4E8-5276CB98F0C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/AB274952-7B7D-1240-9FE8-D76A141F713E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E222ED59-4C76-0549-8302-4FE045D25D70.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B92D5812-B925-CA48-AC22-7AA025FAD1A3.root',
] )