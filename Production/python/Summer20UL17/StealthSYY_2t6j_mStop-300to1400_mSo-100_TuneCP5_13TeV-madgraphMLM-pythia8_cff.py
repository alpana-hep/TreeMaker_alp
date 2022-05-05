import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/01DCA1AF-5C24-374D-B351-33B4B581D7E1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/05D74525-4545-1842-A7E4-A5FD94E129D1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/0AB725CD-E246-C245-A918-7E178A9BBAFC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/11891655-6BE1-074A-86CC-C1F87ADAD50C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/16639146-94A9-1F4F-84ED-9E3193B0E41B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/220236F8-5218-9541-A008-73E6187FD263.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/2FB22017-B2D7-3346-825B-A74526655303.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/309C557D-8907-0340-8586-B6A4694F5387.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/38482546-2E16-DF4B-886D-F588DE441D21.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/3EFADB29-1095-1F44-8EBB-D8BA4AA92C53.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/4ABE715B-1538-9D4A-8BC3-2DB99BD0984E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/5A889650-7C42-2A4A-AE35-6B81B8D53CA8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/5ED8E5A2-1EF3-6E47-ACCD-FFF2C82BC6C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/628D638E-5D18-4A45-B9D5-E07E4FB09BA9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/62F0CFD9-A892-9647-AE04-0767A83E5A8E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/6601C537-9708-5B47-9A1D-25A2A13CA140.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/7B952E75-6BF6-7C47-81D0-04B83D084F16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/8364D8C8-5A8E-5D40-A7A3-C524C83CC686.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/8D68FEBD-C773-F847-A4DF-66E732710E07.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/8DBCDB0F-B72E-5544-B1C3-C9E9B9D48785.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/93D346CC-B0D4-FE4E-A3DE-22137E54804F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/960B8732-7424-6545-8E31-84E518999E8B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/9D7FE8E5-920A-6D4A-A737-E84C1BA3724F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/9DBB2584-5AF6-294A-A67E-04499BBB56D7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/9DBC49D6-390B-D644-AFA2-47281EF9EBF0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/A96475F8-B233-FF42-AFB9-0BE454804E72.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/BAEAABB4-7D3F-CB4A-A17D-7ADDE771CFEC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/BD0225DE-0E7C-6340-AFA0-D3EA19192406.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/BDD8D3EA-B864-AC4D-B8AB-B17E507734EC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/C823FE4F-A7C4-A241-809E-E891987D94A9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/E5B72A7D-4985-5D44-8A79-FC114DBA3EEB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/EC9EA10D-110E-C444-94AA-24FEE9176E55.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/2530000/FE6ED70F-2906-464E-B1B3-056232EE775D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/25310000/004C74E9-C6F7-1F47-A426-5478EE0A1D42.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/25310000/1968A357-BFE9-5E45-8E19-C569BDB37899.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/002A0046-249E-3C45-BAF3-C3BD7D45B331.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0152BF81-5BA6-4C41-9FC8-47257E9AB185.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/06BE5A82-5BBD-D149-9969-247B767E7C37.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/07473024-F02B-1D4D-91E6-B41DBCA508F3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/083B3449-1C33-0846-ADFF-D42D3326DECE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/08A6CD7B-9250-BB45-9FCE-03BA704B6F2D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/08E3BA5E-1EC5-1848-BBF9-89BB213BF940.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/0ADDCA0E-DB4F-D74D-A788-53D4E1ED4FD6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1317DFB7-54CB-6841-AAE4-7A1B1C0E2626.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/13C23762-16F1-E146-997D-7677064B78C2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/16C45492-14F3-9442-850B-9C6B64918F1D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/19D055B1-F110-5642-942F-B35E3E5ED6BC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1E78DE2C-438A-0B4C-8431-FFE88507DE8D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/1E879678-0902-E547-8BD3-3E4C9A62BC65.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/275C3427-B8EC-A148-8901-458DF9C22713.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/27A244F2-1696-124F-B9FF-0F6E2C001498.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/28619F88-90B0-2446-8586-D0514F69D44D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/28715DDF-80A2-F34A-8755-B2DBDD8FC67E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/299FF6F6-B151-7547-9E09-638336651687.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/2CD42A1D-E41F-BE4F-AA55-7B78123DDEEC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/300FCEEB-A2B0-8E4F-B675-9E9281FF45BC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/38AF6811-C933-BC42-9FC4-E9CC06E56901.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3B6E603F-89E6-C044-9833-DEFF5A68F58D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3B9DEB2D-718D-2F4A-BF0A-B929465C1CE8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3C367742-FE03-1A4E-94E5-AB6D7EAC7DB0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/3D79504A-309E-134E-9056-882712F019A1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/424B0B9B-7AF9-F242-9409-7F3A3FA8989A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/457B4D93-ECC3-084E-B507-C0BA54EA1A11.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/494C87ED-5267-7E48-A8EA-8F9AB476017E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4AA03AD4-0F74-B14A-B976-62B2DCA6CA79.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4B0676AF-15D1-8547-9055-182687A3210C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4B0EED46-5189-324B-BB76-3EE892A62F38.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4BD6E8C7-4F5C-AA47-BB04-27A31903C9C4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4C8BFC45-F947-F24B-A602-20878055563C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4CF11870-068C-CE4C-8580-032481CB04BE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/4ECCAB80-EFEF-AF45-963D-0A7C7650BBF9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/51C14886-D493-6845-9430-AAEA1F219028.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5876CC39-E91D-0A43-B6A7-51FC631ADB41.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5ACD8389-A119-E04C-A04A-7B85DB8624E4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/5F8B2DDD-69D9-A742-8443-EBCE5336D210.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/60961469-395C-EC40-94C9-1872B3E09DBC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/6BBCB387-26E4-574B-9108-8301914C7117.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/6BCB6EBD-4782-1848-90C9-66A4846C3D16.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/6C06DAB5-849F-3D44-9B5C-83C45B86F84E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/6E3B176B-8E9A-AF46-A39B-A77E86C4C5CA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/6EB0ADCC-F73E-8849-B21C-C0775F52C0FE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/701FC8A3-C0CA-6D44-8190-2C659FBB05D8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/73B769DD-56B3-1A42-A076-5CF8EB60A5FE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7AAAC040-CBF7-D844-B1D2-8FD2C29B4765.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7B191E71-8E39-1C40-B6D6-71A828396AED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7CAAABE8-E95A-5142-80E6-CC5097A81285.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7D142457-11FF-4645-BF57-EED17F4203FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/7D8FE0FA-F0B4-E746-B194-1150FCE69555.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/81EE3465-27F1-884D-A06A-2EA9E1F81FB8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/84BC1333-E76B-444D-A898-DAF54099D0C2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/860BCBBE-80E5-D245-B11A-2DDC6E7EB60D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/871DE2A5-33D3-FE4D-B79C-EE2FD27C6BFA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/92FEC16A-7637-6644-96AF-93C639B4964D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/9443D0DE-BDB4-0743-B25E-EBA3D08EB64E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/97CDDAA7-983C-2A40-8494-126CEDCCC709.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/98007511-B663-0D40-ACE0-0CAD1CF0800E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/9A7E6028-C12C-BA4D-9BA3-3123CA96F11C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/9BFCE287-B210-8647-9241-0E8440245829.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/9CFFA0C9-191E-F14F-87BC-88C53D70451A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A0BE607F-6FC5-B74E-8D73-D54B61DF8C88.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A845456E-923E-3946-AB03-E4F367B1CA46.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/A8CE2E25-2657-D043-8609-E553A380BC1B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/AB951759-45AF-9343-B0DE-DA65F1E503CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/AEDCE3B0-D9ED-2D4E-889F-AC1328D8A8E8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/AFC34EDF-B91F-F04F-8446-7503A046C574.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B1294584-5B49-884C-B781-A49440D332D2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B415AAE4-F81D-014F-897E-0B838FCDD6EF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B4319FFA-CE2B-694B-8A52-D1361CF709A2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/B8396553-4A4D-5B44-85F4-818D415F3512.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/BB056904-1D69-074B-A091-347FEF90B044.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/BB7AF9AA-6368-1844-B727-F997CE497384.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/BE133521-9630-6344-8915-1B2A77065CB8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C0E4117E-0377-B04F-B6D9-184AF3FDC81F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C1949599-F1A8-F148-897E-66D99C222984.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/C21A00AF-E4EF-4D41-BE26-61D97FC35167.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/CB0FFC7E-36EC-CA4D-AD6C-4E8C7BFD7A59.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/CE87F752-5603-B74F-9BE9-241D6391BD00.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D003F542-62C6-2343-8C49-A7EE6E7F23C4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D0494217-3219-C74C-8B95-B6ABEB8EED2E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D3AD6706-A4A5-B147-A4A4-51F452285062.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/D645C88F-581A-AC4D-8835-8F603966398D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DCD8F79B-D45A-BF4E-B225-6722CFF7D9FA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/DEA57451-A674-EF40-9558-4E0FA0A03DF5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E0120B2E-9C52-9343-9A62-386BF06DE57F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E22C9520-8A43-9449-B47B-047162939640.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E6747401-04C5-0744-8246-A1EF0325913D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/E72BF210-3D5F-534B-9374-FC3116207B91.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/EA444111-08FE-F14C-9F64-AC810378569C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/F0B4EB50-956A-DC4B-A952-53D775A26E3C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/F9C990AA-A07B-CB4E-A1FF-69C02F314FF2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FABD9F72-21DB-5547-AA6F-AD432D015086.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FE51B4B7-E545-5E45-A18F-01E5504E7AB9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FFA3B1AE-732B-F44A-94C1-6FBBE148870F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/StealthSYY_2t6j_mStop-300to1400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/40000/FFE39F1E-D3CB-A645-AF93-610B76AE1E35.root',
] )
