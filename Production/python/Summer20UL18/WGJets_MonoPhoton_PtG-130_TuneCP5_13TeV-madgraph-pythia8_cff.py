import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/100000/4DD52D90-FD6D-414C-BB06-EA9E5D09026C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/15853DFB-FA16-804C-9FBE-1A229E2BBA72.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/1BCBB7E6-C61C-FF4B-B84A-5B47623D4375.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/4D6B0B2D-1EC5-E340-9581-9D7AA7C99B06.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/4F20C630-66EA-9740-9F67-A3BFFDA660B9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/60907780-4E21-F646-9928-263200444DA5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/6287A6E9-40B8-BB42-BF2F-FF81A774746F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/6ED6AB42-10A0-CC48-8A87-E6C4D60D191F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/77FE8A78-96FD-8D4C-8BF5-EF0831F18046.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/880936E9-8FCC-7645-94F9-26E342FE424E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/969A1737-FFFF-F041-9DE3-BBD501E9E181.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/D2707FF9-127E-E647-97C4-DDAF5899F03E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/DCFB95C7-30A4-444F-B848-4827E4DF1926.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/DDA3A3BE-39C6-CD40-A13F-E99ED7C1A26C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/110000/FE0FDB4C-5BA1-E94B-A679-595812776B6E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/CCCE9C0E-67A6-B24D-96D7-AC0EF752B47C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/D905D076-0DB3-664E-BFB8-24231137082B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2430000/F5D147BA-BDB3-6E44-969C-3FD630250A40.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/0630A015-F42B-4E49-97A7-71AED8DC8D49.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/07BB35F5-D394-934F-9E9A-7B87BA02173E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/19513C83-7C87-9F4C-933C-2DCEAC641DDB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/243DDF5D-7BA1-6A4D-B79B-205147BF74DA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/29740D97-F6BC-414D-96F3-B6D25DFBE4DA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/41A8B9F3-C468-6248-8A79-E90AF92F9013.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/544221C2-30A9-594C-97B4-C0D950F2C8B9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/56BAFECA-2FA4-B541-B86A-5CEAC98505DB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/632A5D1F-913B-E84B-A908-9FCC50EA5536.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/664560D8-E770-714F-974B-6E5D6D0DB44C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/69EE35A0-1307-A643-B2F4-9D959A2891E2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/86EA758F-E8ED-554C-9315-E3556765617F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/8787E57E-CF9F-F846-84E2-D3D380B1FD69.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/8D8DED8C-DABA-8B44-A5CE-3BC065D1E1FF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/991D7607-7E01-5741-80A5-1981A91B2005.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/A4B9EA48-5792-E641-BE62-250C1DA86DC6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/AEFA9791-F131-FB49-978F-123D9371B490.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/B8784023-39C8-3A42-8B3C-9DF97B68A236.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/BF1BDAE3-07E6-2645-9F77-6BAA59455E4E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/BF276A78-68D4-A146-8D06-978422BE4EEB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/CB109D4D-322E-374B-A456-10C39A1FA113.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/CE4218FB-9E92-D845-A083-78267791DC73.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/D8A99C27-4B2D-CA42-9D46-D892BAC69FDD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/E4D30BF8-8D98-4C43-8CA6-89A515E91CC4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/E7E519E7-5491-E941-B3A0-FDF8FC5D6869.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/E8435DAA-5431-B349-8D40-A0ADFBBB7650.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/E955A6DD-783F-694F-B05E-11BA6B2F2CF2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/E9CCB0FB-E01F-BE48-8F86-B94631A3B674.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/EDB8AC9E-2391-DF41-BEF2-9989BD440B16.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/FD0AA5C5-0828-A848-ADE6-0744C8B52BED.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/051994FE-769D-B44C-9589-15A479A38828.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/0994DFD3-865E-4846-AB9F-C8A5378392D6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/0AD70570-AF59-D946-AE2F-E414D1D4D19F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/17BB5252-A48A-3B46-924A-35FDA7061CEE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/22EA8488-8D03-3A4B-986A-EAB93E31E36D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/2CA2AFC8-DACA-2540-87AC-B8956799E727.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/3622FD37-D011-BD4C-84AA-2462A6D42371.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/36ACA95D-FA29-EE49-AE92-ECF93FAF1954.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/37CEFE65-0792-1540-8EC3-E0D6F64E8E19.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/3D6BF6FA-3E34-6845-AB6C-89127EE0E096.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/4ADA2994-0BE6-3E4A-B7B3-25E44F0DFA01.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/4E5D70D2-BD26-EF43-891F-E8B0E75EC33F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/5A23D0C5-55F7-E64A-98B3-C7CFA1C23980.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/65726786-633E-4948-BF47-DC885F1CF5FC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/660C73F7-2A6D-0941-ADED-A384D86FD5E2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/6EAB9EEF-8248-0347-8157-FEBAE6BAE3F3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/76882A98-104F-FE48-896B-63C1BEF8A243.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/792A8F05-84F1-5D41-8A0F-A1F96E08666A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/7AFFFA76-4D2C-F249-84DE-56F77697DB14.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/8072AC16-3F1C-D94B-B873-5C8D1575F596.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/833D5DDD-24B1-FD4D-9D33-6A2159C17CE0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/835A2BEC-9249-7040-965F-33BECD1088CD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/83F67642-1E13-1D44-A5CB-7EA6B11F1FA8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/88EC943D-E0E9-0B49-AF23-3CB5E698C6FC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/8A071DA8-8AFD-8045-B094-52C107A87CC9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/8AFC8D8E-1F9E-1D43-A684-AD80BE3CF4AD.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/96738A3F-40E4-724D-A17C-ECFA564B4A52.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/9F9131A8-2B45-A34A-84AA-788C00FBD99F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/A877FCEB-A011-3C4C-86DC-7BDE0F44DEC1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/B96CB45F-0785-314A-814F-A86D0F3FF596.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/C4CAAA2D-10A4-2145-8591-EC6DA8A486CF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/CC82D15D-9716-BD4D-B1D3-975FFCC02FD6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/D08C5FE2-CB90-074A-A8B2-7437BD699F26.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/D4C7B874-4479-B64B-9F52-9BF434B9131F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/DCE3737F-E110-5F43-B6E1-3F520751CD14.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/DDD2EE4D-00A4-4B49-91E9-871F4605AA1A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/DE999ED8-7D2D-F448-A4C2-437E64ABC1A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/E1EEB78F-B7A8-5543-92A6-379CAAF2E625.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/E445AC5F-872B-5240-A810-CDFDEBED38D0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/E4776CE6-7336-C34B-A991-6066258DBB5E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/E868E24D-AEB7-8A4A-854C-9332E72D865F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/EDFBDEA0-15B6-BD42-A373-1C254C715709.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/F97F7645-F054-604B-9CDA-CB862A3D629B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/FF116CCB-748B-1544-92C4-23870E9C040C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/0FC65F4E-E22F-C24E-8875-D638FC732684.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/19BBEAF9-1128-FA45-8ECB-88559F2C7F44.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/2CEFDD0B-BFB1-C448-9CBB-4BEDF4D56991.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/2D2D48B5-7E30-8D4B-9391-64A11383C3E4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/3045E430-5756-3141-831E-572191E0E484.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/415F88FF-7DCF-1C4E-8A0C-C8873BFF22A5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/5719C094-D167-AC45-90B0-DEDE11EB7E6B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/595E737F-7B5A-AF44-8121-C23BDDD4F5C3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/6BE37E07-4FE3-1F4B-83DE-66A4FA8F0456.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/8DE34305-D418-A849-86FC-2331FD016B76.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/A8EBBE82-B612-0F46-81B6-4D6C04B7662B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/D6E6F92E-5E98-6842-BA12-19E5493E8EBC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/D76CBD10-F310-D04D-BDB5-3CF787AB45F1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/FA1DE5D8-0860-0F4D-A4AA-0B9E6721CC0D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/8F986358-2277-0547-AA2D-EC1F54164B71.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/70000/486E137F-51CC-B548-8310-A25FF795A368.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/70000/82E981AC-A242-3442-AFED-52C0D60FE476.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/70000/8D66D6E5-15F7-E74F-8FA0-506EBF9AD980.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/70000/CFDE1571-1157-914C-B237-7E25A1B18EFA.root',
] )