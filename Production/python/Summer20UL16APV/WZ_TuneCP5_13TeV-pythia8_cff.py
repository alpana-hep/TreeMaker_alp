import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/026318C0-FDBD-134A-BED8-343FA39758DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/2F78A981-40B2-424A-8B65-91BBD52A4469.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/425458DB-C01A-C845-8F24-EDDB2E0D8204.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/60E71CCC-4D18-5449-A910-8342343B7221.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E4E01CCD-10FE-BB44-BDE7-A312219D0C8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E9A18819-BA58-5647-9FA8-75F7CDC11CC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/16176244-A470-214B-88CA-55C5BEAFF0B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2DB7EAB6-080E-624D-8313-8C37A0B2620D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/34D281CD-959B-D047-BBC9-B31DB933374E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/367C2256-D882-924F-9614-600B2FDDF84A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/69B3608E-C601-F043-A1CE-748C1F9A4E9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/74191E05-0197-3247-A808-FF6628DE03D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/76375BE9-500A-464C-9BFB-0301DEB60600.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8C7759C9-978B-2E4C-A300-5F32DCA9E48E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/97F92DFF-D2D4-5646-BE4B-BFB6005F934C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/09EB2895-D639-AF42-8BA3-D7862104CF87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0A6B0BF2-FF88-604F-AA0C-49E9C7319473.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/12289360-91EE-174A-8A94-BDCADC9C6FE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/129E74A9-A0B0-D546-B360-9EF62CE4B204.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/12A27004-3F28-6B41-9395-CC3B5F362D17.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/18E85D1B-56D7-C045-A29B-4043ED3C6465.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/1C127F0B-5DB1-604B-B36C-69A9D646B583.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/211D150B-6FB9-E642-A92B-8965B8B475BE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/256281C2-137F-264C-A724-39DF5E1901EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2CD444BB-1D2D-0F42-8917-FBCB8C436395.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/314610E8-8820-9446-A861-B48813822405.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/37151D89-A04C-F941-9D06-1218F7C63A3E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4F7EE3FB-A3FB-DB40-B7D7-15110CC0A45A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5598A43A-AAA6-884D-A700-0AC1382B3153.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5BEFC593-9FC9-8D41-946F-0FEC60A92DC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5C6EC8FB-1847-0D41-B9F5-510E0173B5D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6234F6CC-D8CE-E740-BFDA-47E2B7308B2D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/64D8C296-4F2C-9447-B596-88E48173C508.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6670406F-98D8-934F-BD70-AB6B84B922B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6675ABA1-8602-2F4D-80F4-A3D2056EF9CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/69458A83-D3B2-C34D-99C1-1FFF57F0E703.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/6E94EAE6-F92D-574E-80E1-54132AC88CB4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/77475444-0238-C940-A720-3BC1CBCB6D1F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/817611A8-6B33-0545-AA44-C032B4B2B5BE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8A000785-F7C9-C844-B16E-800F25D01904.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8C8B9998-832E-4144-B98F-4C45A077CCC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8DCDB6BC-AAE4-8C45-948A-26B884077A75.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/902A7F45-1164-9E42-BD88-B57FCB169530.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/910C461A-EBBF-DF4B-8D26-E22925195D70.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/91F0B151-450B-DE46-842B-8D9BBC9714DD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/9381F57E-8DED-604C-92A6-AE566598C1FD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/98AB84A3-C05B-9345-B25F-F08071D97EED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A15BAF47-FBF8-8341-B7A0-E20D4518C839.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A720BE08-B4AC-EA47-AA89-8171BD54ACA1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A7A99DB4-4D34-9741-B4CD-50E40E8CC8C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B2DB1E94-5F5E-2845-9C2D-E58ECC2D1062.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B2E4BBE1-98BA-064A-B0FB-1256A73D7CC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BBC252A3-7859-C245-8362-023EDFB6B47F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BDC56816-7BC5-7142-ADA3-08C7E83F728A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BF7D004B-627D-034E-84E4-2385D37722AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C26D8036-23F9-4542-865D-F04B7A033EE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D292ABEE-463D-3149-B0E1-0ADDEF546511.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD3A1FA7-3EEA-E74A-A3AD-348013BEB866.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD52F228-915B-6A49-A1BF-523B77B10B10.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DDA015A7-57CA-4F4E-BF4F-F12643932CD0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E23341FD-A1EA-5E4A-811A-9A4A6EA62F2F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E28B453E-7A81-4B48-BAF3-9B1A04D4E9BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E4B0E2A7-0A68-E646-ADD8-3C7EEE5AA2BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EAC029F8-90F0-6347-9A22-756EFDDDC7AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EC356F86-E8A8-2442-B59B-5B230EA03706.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F4414E05-1E4B-8446-A0D8-844F9301C322.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F4FDDEAE-B167-FC4B-B432-D5AA924F3B82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F70FFF9D-EFC5-6241-9BAF-832C9F59F9EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/FFE02FAD-845D-6845-ACD1-41E3B67D4A19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/029FDB44-D1B6-1E42-979B-9170D395401C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/12344948-E6BD-F44A-9001-56969726E7E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/23D27724-F28D-734F-B47F-016939525C72.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/254DD762-E73D-0B41-8C93-055868212F16.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/25BDD99D-97DF-6F46-B604-03F54A278722.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/26D8439C-7D5D-7645-B176-71A4839CE1E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/27666B61-ABE1-884C-B057-8ED579790B72.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/28C73BC9-B9A9-864D-933D-39569EA332C6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/28F8A0B9-C6F6-9941-A00A-6982B93AF3FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/49445A8F-6B94-D24C-81D1-9F15F35D0739.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5DD59708-EA70-B648-85EE-061B6BCDD3D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5FD9963B-AF05-244E-B811-13A5224ADB28.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6068F251-836E-374A-9EE2-A0811F5F8E73.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/72D941AE-BF3C-7B47-85DD-5473C8DBC17A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7496E585-9606-114E-9B81-9B624056AF53.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/751834F8-42D3-F442-80E6-4504C4DF737B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7F675E2F-5A35-6E4E-B420-868DD290CD5A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/86A0BC51-A4BC-024F-A66C-8FEAC1BB8F41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/95285655-DB98-DA46-834C-453E15406D26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AC4D33DE-1647-5247-9DF3-EA2B87BEE461.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AD414E12-B8CA-8441-B5F3-AAFD041512F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AF216009-7C53-904F-AAF2-0F8C4F9F6284.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AFE70CB1-F534-6C4B-969D-41154CCE8761.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B7578000-39FA-3046-865E-A6772721F32E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C28735C3-2750-0240-A664-8AD8B08BD1E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C44D82E9-D420-DA4A-A5DF-FF75BB158431.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C7757450-BFF1-B049-9FE4-D8ECCA743B46.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D24C4E4E-E4CE-9E4C-B3ED-4A8DBE62CBF9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D2DA7053-B25C-9A44-BEE2-EB8DB64819A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E9A6692A-CA08-2B45-B9BA-F36051D5B56D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EBCC33F8-FAA4-AF4C-812C-228C3C5AC5E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/ED74C8B9-B529-CF49-924F-B18FD3C6E531.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EE60B11A-AFEC-4D4B-BC23-F5E93E632004.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZ_TuneCP5_13TeV-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F3A55A3F-4470-894F-9097-278714F47E9A.root',
] )
