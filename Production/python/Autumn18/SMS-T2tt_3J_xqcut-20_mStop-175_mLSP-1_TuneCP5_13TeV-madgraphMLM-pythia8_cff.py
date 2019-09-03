import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/137DA94B-B69C-A648-B45A-C0B7E2659E7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/1837748D-8664-B84F-A729-D9369E00EFA4.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/21AE9E76-41E3-7A4F-9912-26E0A4B2BA6C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/27A6A5EA-A670-C94A-8DCD-E61E33722EA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/285E5484-8642-7849-832B-1713D1BB2174.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/2ED73969-CABE-E24B-AD59-323700A05C5C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/363A0F24-732E-E24F-B758-58357B9B9138.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/3934A89A-8CAA-3E46-83F2-FE5AC9306B17.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/43FBE9A6-32E4-B649-941A-6D91D9524C3E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/44636FEA-53B6-CD40-A92E-46B50DF8E357.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/490EE74D-7760-8D42-9EAE-2CBC385FDA79.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/4BEE338E-B9C8-6644-A352-45FEA3E6CBF9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/4DBAF1CC-9291-874D-94C1-412C45D5DC7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/4DE5AFBB-1BC5-9F48-B632-7FBABA3CF1C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/54C3C56A-B166-5044-8489-B039A0B32F95.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/5510E803-562D-F64D-A67D-4F2551E8DF7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/5C255E2A-7518-4947-8ECA-D317978C792A.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/633D3BFB-4B33-C742-8F16-11453F986A7C.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/63D9C843-2EB3-E846-9A46-AD27FF219CEA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6720512A-C1A9-6148-A49E-168EE0554153.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/68E5CFC3-CF60-9A45-ABDA-4ADAA3686344.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6E48EEF3-B0B8-EC4B-A32F-2A0ADA6E1A94.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/6EA76B9C-CC78-0B42-B8F5-D8177588A6DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/700AEA57-A014-6B46-B133-88FAD740AE19.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/7177A518-3CDE-4540-A976-AF21A6C555FF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/7286F396-AFDE-954A-BD89-03B8C65D64CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/73F37BD9-0ECC-2146-BD72-3CB2326FF8C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/8263CFC7-2BC5-D841-9A34-0F27FA6BA635.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/86BF90AB-2700-E54A-9383-4615B05F5593.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A135E8CA-C061-5C40-8065-04E462A10917.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A293EB2A-683E-154E-A55C-20E2D9203456.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A29B4C10-FF37-0B4E-94AF-0E396F3E9614.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A3A23B60-65F5-DB46-BFA5-B28DE6BA24BF.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/A9F0D7DC-671D-314E-9C73-914B09FCAE40.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/AAB2AB7A-2E8A-CD48-8CF0-456B6F2FEE66.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/C058B96D-E44B-9A4A-B8F6-E8C88DE73A2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/C777A362-6F5C-4240-A971-D90C9179C7D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/C815FB4E-CBB3-0D47-8DD1-32632894F1A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/D3B81EE1-FF57-474D-A27D-6ED69AD1FB7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/D9D556BA-C9DC-794A-8D3F-5A1BEBD36E81.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/E479B03F-5124-1C40-9C18-0961BD6E1138.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/E5018F5C-D744-6B49-94D9-52E3AA327829.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/E54E7CAA-AF3E-7F47-9687-289929AC4D73.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/E6F35584-5616-5B48-8EF4-069B912E57D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/E9CADE80-0C9A-AF48-9389-0539EBBD2D21.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/ECEDE015-BF60-9A46-B48E-B097F83E22CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/F7CF2799-98E9-4F45-B75F-BC9613B34FAA.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/FDE8BEC6-2992-0F47-9A34-16732C05F3C6.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/130000/3D618791-B6FB-DF45-A5B5-FA7768AFB13F.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/130000/459AFA94-726E-244C-911E-41BEB58D5715.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/130000/5881F2FA-FCFC-8640-9B32-0B4AC8506F1D.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/130000/B6DCDA70-554F-094F-9519-654D07D872D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/130000/C076C0CA-DC56-4349-8F41-A5FD73FC4F12.root',
] )
