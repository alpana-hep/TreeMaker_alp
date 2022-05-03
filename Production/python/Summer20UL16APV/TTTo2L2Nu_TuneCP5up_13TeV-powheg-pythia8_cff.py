import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/099E451E-3A51-D84B-A2FA-662A90F480A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/0A78E26A-FFAC-014F-9CFB-8E003F590AC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/2ADD648A-714A-714D-994F-65B34B70E28F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/2C52BA70-68C2-674C-B07B-9FF01181DE5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/37974B5C-05FC-D542-83B4-7BF81F02E208.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/3A3CD3B8-601E-C640-A684-D310ACE9767E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/3DA6CA48-DCA0-0744-8581-5BCE3A805654.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/3E3B4950-3BFA-454A-8750-3CFBCE07EF8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/479BDE31-FE3F-5B41-8410-1B34CB77924A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/4AF89CF6-DCDC-754C-AE33-5DAD947EB45B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/50DB47B6-4ED3-A44F-9B66-916121037AC9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/5764CB2A-D3A1-B645-9EF8-420A220BDDE1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/580073C3-8589-AF4E-98B0-2B3932089372.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/635D4BFE-3BFB-CD49-8BE2-F482F8D5D517.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/6EC56394-4784-D04E-8549-12AE08C7E8AA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/70672DA1-8251-6C42-AEFA-FE2F8B4B9530.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/72C1A7B8-4F66-9947-8A47-049BEA2CD5ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/7B85375E-ED2E-D549-BF1E-44073B92ADC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/83C8AAA8-0435-DA44-9568-15D77A24B66A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/8A146A2A-4D84-064C-8C5E-FA9EDAA14DBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/8BC8C51F-2BB7-5649-BEFD-FB507C84E26E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/8EC93037-F87B-6341-A1EE-B0C109ECDF4A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/8EEB0555-61A5-2C43-B936-43F03A1F6BCF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/97A7531E-EFFF-3A47-A673-CC638CB7313E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/A4AB1A0F-9A0D-B64E-B991-A085F8752689.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/A94E9E71-BF3F-8549-9E16-23F7853C8C64.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/AEE66C1A-644D-EC47-9ECF-2F60D44D4B40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/AF6893BA-8F14-FC4A-B142-E50937212803.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/B1E5855A-E45D-DB42-81D7-666F02DEDE13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/B4B24A63-FA62-5140-83B2-B105D59AA629.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/B6368991-429F-E744-B98A-B023061F4ED2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/B8E63637-8CE9-7E45-B426-874625A8EBA4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/BFCA3A15-776B-1D4C-9BE0-A5898A643CC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/C82021D1-86A7-FA4A-A052-56C5A5D14B57.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/C85BF903-062D-8147-B6E2-ECD626137358.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/C9236DFA-A79E-924E-9B26-BF21FF2C5EDA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/D112B4CC-5582-EF48-99BC-BFAF58C4C9F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/D51E29FB-EFF9-8046-8FC8-33F4CF67FEBE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/DE59DF9F-2C57-984A-9D10-E9287FE41A03.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/E3F830C4-5B6D-8644-8B2D-0F2C4DB6F97F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/E4853F79-80BB-F24C-8197-D07562A70B38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/E4D78F8E-1E43-C644-BC07-2DE9103519A8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/E637EC9B-8214-4F4E-8DC1-CF0A9E98E3BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/EABC761E-3F53-DF4C-9D64-38CF1A235E24.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/FD213E8D-4AEB-4445-8B12-A2996049A9EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/FDF867C0-ECA3-284E-8FAF-566DD9DF6349.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2540000/FE6866E3-F73C-D14E-8800-D002B49E8131.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/291E9C5B-88DC-F542-BD82-690AA3790685.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/2C1301A7-46CB-2B49-A6E9-82FCBA2CB005.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/527D795F-99E4-2A44-8782-FE754A114957.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/73279A6D-C4E9-3146-B399-1E93D0551C6A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/B6E1D5F0-8EEE-934D-BD23-A646A02632CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/BE285B99-DBFE-C040-8E14-CA01DD2A995C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/E1599677-2C1A-7242-8BE1-11B207D985B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2550000/EC7F1DB1-6FE3-A346-BC1A-FF3D22105B1A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/0500801D-75B1-244C-BD02-EB9A3AD89498.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/0573BD11-FAB5-924F-B376-BB34FEBCECD5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/08BBF4B5-3AA1-CC4F-BA20-DF56C4DFC52D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/0A636B53-3267-4A4A-9EC5-3B9A2C797D71.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/0A85145A-4E5B-C246-915F-E3B9AB660E9A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/0C31F7B5-1CB1-5145-8704-087716240092.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/1611AF91-93BF-2A40-B888-1D58328D6053.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/17056534-32FB-F74F-AD87-BB59DB310984.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/1F3E6B48-3198-AE4A-B3D3-819AB2FEED1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/23CF93BC-E7CD-0945-A33D-4E5E74877184.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/2806F25F-3644-1548-8AB2-6A0E2B1C654F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/32740CB8-F640-E342-8592-B70AA08FC289.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/3654396C-2FA8-D84D-B695-98C06A645AE5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/39C0BFBF-3D8C-3342-856B-CEB4B5C7F416.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/48ED8BE1-028B-1C4A-99A0-AF7C116E0C3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/4A12F895-9512-4F48-A940-2AB9565D4774.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/4B04478B-5E73-B745-BB94-F43E802B873F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/4E62779C-44A4-FB4D-99DE-7102B08A3B7B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/507109E4-632E-9141-BBF8-B1C9140E6877.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/524D7ABF-1411-4046-8126-A9062B4C1484.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/55142D25-30FB-5C4D-AE5A-6109785669A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/57449A39-079D-F046-A4FC-1C94D403FC8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/5C6D7658-119C-FD40-A5D5-B6A897461E51.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/64A4CAEF-28BC-6848-8DF2-E656D43FD3AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/6773EF7D-8B0D-7349-A624-A9921B594BF0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/6ABB65EC-6C10-8E4A-B004-CC731DB52EF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/773049FB-3D50-D440-BC34-E9B7C1C32280.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/7BAA1BC2-469F-D548-B264-044751348E8B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/83C0DBCD-EEB1-0D4A-BB67-289D9BB9253A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/8428DFE2-6FCD-6945-9B4E-20F2FE9CCE88.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/87F51599-6BF4-1F45-9037-1870A3F61151.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/921589AB-69AF-624C-A50E-EF1A1FE8719E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/930D6EDB-5CFE-9241-A119-DA7F081137B6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/96036196-FA6F-824E-958F-1F83932E2C22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/9E8DB937-255E-B843-B6F4-0B1D92B11506.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/A0F6F789-9BD0-4C49-A51E-8DB390675A31.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/A1A7EC8D-CCF2-9042-92BE-DD6CD568871D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/A722507A-0D29-984D-A6B0-8823761BFE9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/B01AD378-0DC0-E34E-921E-E6959B267823.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/B691C6ED-713B-FA4A-B68B-BE11D8698136.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/B89BAFF3-B47E-4F46-AD50-C8A5186544B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/BBEB8992-524E-CE4E-B38F-A682D1A3453E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/BC0286A8-E97C-C748-8FE8-01F5E5D58CAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/C2C5A0D7-8F62-0042-808D-C4B68BA228CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/C5747A97-4799-0A45-A337-E0D6685F80B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/CFAF2076-17EC-8D4B-8092-562C4C9733B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/E14F1691-61B9-F540-A8C0-DD7EAAD61FD7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/F24B2E86-C8F4-C842-A4AA-176BA65EE29A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/F38D8E91-6045-D945-8063-060EF3543556.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/FAE06F86-A4A9-6441-BE77-7C08E6B969A1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/FD37E669-D07A-6A49-B23B-A861F290E93C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/30000/FD4EEB0B-0E79-C346-9BF2-B2861E7A82D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/00B59BFC-F819-3548-BF73-4589A861D95E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/02661A4A-8F0A-CC46-9F5B-2FEAAE4911FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/037516A5-F342-724A-8787-0833E4296CE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/0514ABDE-4932-1540-90CB-FBE047367FB0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/08027C9B-7D02-2741-AFB3-E3D767FBC108.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/0ABFD2B9-919F-BB45-8388-09FEE34E2E27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/1482D47A-F019-C940-AA6D-A49B52AF900E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/18BFB9D8-C2B8-3B41-A7E1-8613DCEA407A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/1B5E347C-331A-B647-9194-08DB8B50F1C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/1F126E49-2185-B54C-8FA5-2457405C7A59.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/1F26056B-2D3E-3D4B-9960-FE233FBB4148.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/25DE4A44-A7A7-A944-8904-298AFABEF22F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/29B2809D-8AF7-9847-919F-3C187D26D0CD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/2B4F840F-E822-0543-B945-23AE3698F9EA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/31AFE1B9-4079-E04F-94FE-9AE18B17EA67.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/39FF7FC7-A20C-FD4A-B0FA-54DAA1EF9264.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/3A263D34-18B1-244F-865C-EE48069F5556.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/3ABDF24B-C6D6-9B41-82CE-245629B2B199.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/4119A824-DD6F-D741-8612-FE5B56589675.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/4356655A-D196-4B4B-826E-802EFCFBBFC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/4576096E-7D51-2747-B9E7-9EC000AAAD3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/479FD9BD-9001-0441-9373-4F15D5730C08.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/48C2848D-53AD-1144-8142-6F1D209234AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/4BF8BFDD-0114-AD48-B59F-2F0BFB9C342F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/503BF0C1-03D3-6F46-8FCC-CAFB7BC38F81.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/51D59D94-1ECE-084C-8259-E0F8C2F4AB3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/52AFF848-A33C-7E47-A3A4-CDB37EC59F29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/539CB8B5-9405-F348-ABAD-4B0BDD59DC97.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/562A4C9C-7D90-9D4E-9E7D-597CE2763B52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/5892A6EB-4274-7F47-B288-56E625DA13C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/5FA21EDF-8909-4E4A-90AB-4D48A78B952F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/631E892C-05DA-9448-AD61-B686C91463A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/636B490F-E5FC-AC4A-8615-1DC422D3970C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/64166975-4C99-DD44-B997-8C21A9AACACB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/68DD0CA6-C8B4-6A4C-BDD7-FCE1872AB585.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/709F345D-1EF0-1440-A51E-6DCC6F071622.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/74BD12FC-FF19-2140-ACA2-4BC9B16A6501.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/759B0752-2F9E-A24E-8EF1-A674F9A08B61.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/75C36A0F-1394-C947-B20F-2FE57F3097D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/7DFDF8A0-C8A9-B640-A52D-6789DDFB45D8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/8A10E18F-8545-3047-8143-8A803B63CC01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/8DE6DD5B-B787-BE45-BED6-BBB9EAC1C6D1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/90903865-805A-CF49-8E75-E3BABA25E461.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/96F058F8-6F05-4F48-86B6-78FDDB539A63.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/97523ECA-1876-2B44-A99F-603734BDF72A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/9D9FAB86-774E-2F48-B1A6-64261DD0EDBD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/9ECB6165-21AD-0C4E-92FA-0725F47FFF9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/A5A05252-0F63-634B-9AB0-A33C143159E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/A7C43290-E052-A646-B9B9-69ED37671498.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/A8EB3703-D004-6542-A166-B156BC16E1E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/B1A3F2B4-1F6B-304E-A707-49673C37D5C4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/B5467C94-168F-F443-B5E8-8B4F8A0FCB4B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/B722C172-11D7-324D-9829-65A0A52DBEDF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/BB74E23B-1EC4-A24B-89F6-456D51AD2E65.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/C12708F7-9DCB-D843-966C-5981F781F8A8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/C7E9C429-245C-E840-BD31-5C16CC0651DF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/D60BC53D-57E1-1B49-906E-89F08C0C7EF2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/D7120C3F-3AAA-4A41-9817-A67C8CC18010.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/D9993523-22F3-D848-926C-52F6B94D27A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/DA6F7701-605E-3F4A-A689-CA94F32E329E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/E4243FA0-DCD0-A242-8D2C-EC8F2028CF4B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/ED6DF69B-AFCE-3A4D-9350-B7BE0CDA9300.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/F202DF8A-30AB-5A4C-A80B-420136D07C38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/F4BC3B42-946D-7044-A839-21E2A243C90A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/F6FFEEE3-C20B-BC48-9CFD-AA9B3E1474B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/F727EA90-87F8-CA4F-A3D1-A5D3A1A04DD7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/80000/FC17B227-AE48-A84A-9088-C1F85431134A.root',
] )