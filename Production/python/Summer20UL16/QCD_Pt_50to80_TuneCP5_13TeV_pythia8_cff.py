import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/3ACD8019-C218-0D41-A65A-E7D59BBDF616.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/3027FC5A-3F02-0440-8BEC-F42EEA867099.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/FD73E0E9-F62C-C840-AF79-165CB2591836.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/01BA26F0-B7F1-3A44-8532-6C4EA4A2DEF1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/020F84BB-F151-924C-AC1F-B5655C726A04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/03221DF2-71FE-A740-95E7-2CBAFEE32645.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/037ED1EE-E6AD-1E4A-AB6C-1F138F8DC80A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0499AD23-AEC6-0B49-898A-25B5059BF446.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0925500A-92A5-584F-9796-5C0657452C0F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0ABFC171-6D29-0241-9E1F-8723CDA62373.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0E301365-70F1-5A43-8C10-A67555A5F813.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0F501D92-9578-9940-87D5-A7779B34AC5B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/0F689B73-4F3F-474F-8248-D166F247A964.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/1199C04F-8720-6B47-842C-6E82D39F3E8C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/14121C04-1F5F-7544-9C46-460F4DD092E5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/18EA8121-7A6D-D14D-9691-5952E848EC58.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/19D52C7F-9EF3-AB4C-AB42-AC6DC65DE7C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/1B8FA187-CC21-974E-91AD-59E234D1B956.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/1FB5919A-700F-494A-B129-A7EFEC068700.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/1FEEBE12-3E3E-6248-BBD5-0C12179032B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/272EA19D-9CDB-934A-B4C8-7B81FB6D3E84.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/2B2AA56F-ABA7-5749-AB4E-ACA6295E86A4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/2D93C178-55A2-654E-8932-35985F6A02FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/2DCF0529-276B-F940-B034-5D083D94E56B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/2E05B00A-AA71-9347-BB2C-25472714E50A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/30071666-F484-2E4F-ADDC-22DD168CEA0C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/30703E34-6AEB-9848-869E-95F5F30E22FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/32907F81-BFA9-9B4E-B6F1-3EEF7A107FD6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/3493E0FC-8E18-064A-9658-BF84983670DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/38B8C061-9542-2D40-9445-A6E2FC695A47.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/398D2C77-4227-CD4A-A932-DE6710DC2DD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/39D70981-259A-7441-841C-8E2F5D91E516.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/3DABD0D4-4FFC-564D-995B-406EFF786294.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/40D43C91-F36F-9B4F-A5C5-831074C95EF1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/45D85028-5D03-2144-9B88-021ED069AFC6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/50C6F4D4-4D56-C549-95BC-37ED7A072BB5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/5B88A36B-2BAF-454C-8F26-9F98D2F2A594.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/5D01CB6F-82B7-C74E-97E0-C8E2ACE2DEDA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/5F46C7F8-94CA-074A-8000-196537F06406.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/5F6D6BEF-B466-8849-B57C-7781608DDA41.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/62D1AF07-AF75-D141-A648-37B1CA904116.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/69816AEE-9A09-A34C-A999-544BE5F30239.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/6CC46747-39CD-4F48-8F9E-013DFA4A4A6D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/6E5CC207-1CDE-2049-9DF2-5AA5D1367E4E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/70320F3D-1A86-5446-AD62-6EB1B3B2B451.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/74C10B45-991E-8543-BFD1-76ED26662F81.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/77BE754B-3B26-8549-BF02-1A790D42FCD9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7A7B9361-229D-D648-B0A9-D006A6327A1F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7B5EAAEA-9EEA-244F-BB72-D967973E7B33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7CABFACB-20A4-3C47-8F42-9BA2AE24B89E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7E24D0A3-AD7E-D541-AF7E-085BF599BC29.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/81B56D7C-5F91-3D4E-B0B5-7E7ABD2DC64F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/88185E34-D64A-5F40-9994-61381A709BA3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/89294A4A-5257-A54C-9512-DAF26DE84E60.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/8C28FCFA-2EE0-EA49-B87F-523FC7F2251F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/8FEEDBE5-D48B-6F49-AF4D-D97F0238A142.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/92431867-7C98-984D-A99D-E7F0E9C314A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/943810CC-49A5-6349-BA0C-0C8F0A8EA637.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/9BEEAD3C-3CA5-B34E-8446-F4BDC8ECB6CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/9FE318E8-A738-E342-87BE-F0A5F7F00B0C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A08A8F77-98DC-B841-B0C5-00B5552009E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A27074ED-B5A7-1041-9D72-BDC10777E986.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A37B7904-46A7-0D45-8158-7AAE96B7666E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A61D93EE-F810-3846-BE9B-4ED3EE052322.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A6DC993C-125F-CC4E-8015-948641C3F0F3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A6F0C03B-E8A0-F64A-9938-474500BF0A2F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A911282D-43A2-124B-880D-7497DEB92F7B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/ABD353BF-E56F-8842-B85E-546C240126E4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/B84FCF61-324A-5849-8CF6-2248E936E94C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/B8B35F02-B023-1740-8D33-43D5185DBAC2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/BB02C45A-1A50-B544-A1B6-DCCD4500A89E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/BB32FF7D-F24E-324E-91CA-6A589953C7DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/BB36E657-4C9C-9541-BE91-888B6493E715.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/BBBE87B2-654B-3B40-98A6-ADA68DE787C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/BD41B186-8AAA-7649-9C33-F178C5E3652B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/CB4D62ED-30CC-C543-8944-182A36894250.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/CF7F11A0-98F7-A04C-8709-BDAB1A901DEC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/D3E005A6-7617-B94D-9A11-91B6C15A04A1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/D4B40B6F-E862-C741-833D-2B3DB98388DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/DA6A3739-82F5-544E-B3B9-26BA97E7419E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/DB6C399E-9CC1-C140-892B-4645E48F6333.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/E91FDA74-4884-694F-A379-6823696DBF8E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/EC91BE1C-96E1-A640-A94C-FC1C653B7A39.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/F0D6D038-0176-D34B-94DE-9D23CDCA54E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/F15E731E-306D-6742-8736-2DA1D9F349A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/F317958A-F6CD-BF44-8EDF-29264FC43274.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/F53B2418-DE43-1344-A8B4-3346F374A215.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/FA31B8C3-DDBF-704B-B252-26AC47E91FC9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/FBD61CCA-184F-0C42-BE79-88E5FE56BB51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/FE3302D4-2FF6-F14D-9876-2A8EC45F18AE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/FF600BB7-6788-8142-A87B-0BF587C37EA5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/02C8980D-172B-2348-8C1F-465F4C0F355A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/083F822E-FF3E-074A-856A-D224098C9F8B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0AB24C09-F2E0-5441-8E93-A944B6AA35EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1778A4A4-8D5A-A64B-B599-F8178258B338.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1AF0B27D-5AF3-7644-8172-00713B5B00F0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1C1EB89B-3CB3-7B4E-9DCC-C238684ABCB7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1FD8D78E-04DA-CD49-8C6B-33A29532B46E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/24A2B09E-9821-8B48-A3EB-47EA5D04A553.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/24D3A749-DB4C-7445-90F7-5A61768C8DB2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/2A990252-82D8-C643-AEA5-40E991381A1D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/2ABD0225-6F3E-6C41-AD3F-9027781A3FE8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/2AC8F00E-1F83-3B49-A05A-119E477C8FB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/2E747C16-3D61-C540-9F5C-409B770FECC0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/331F2969-63D7-3149-9B5B-4C14076CD4A1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/389D61E6-AF81-9B41-BA4B-C6BDE1A5B625.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3AC1CB0F-7D10-CD4B-9817-1A888A75D9C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3E6D65F5-6750-8646-87AD-A20D4AB48882.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/400C22F8-F483-1642-BDA5-0AACBC5186F0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/410C087F-1372-684B-B93D-438C0F1A05DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/435769A9-6FCA-8443-BF66-E4A706A20C13.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/46E9CF3E-CF79-B74E-9A0B-80F192BF2802.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4874F976-CC3E-D846-9134-C74513C570E8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4E60DC3A-026F-E240-8A91-C10DE55190FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/52354B1E-F877-8844-9BD1-233073879707.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/5731AF10-0775-BB4A-8ACE-19D380AB0694.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/599AB359-03A5-2340-960A-28614699479C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/5C60E0B0-DD65-C445-B072-41ED2D21178F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/5E191B1F-88D7-3E4D-83D2-F9CABD4891A5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/611150C4-B848-8B40-9140-B2DBBBEDFA0E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/6249F2F1-43AD-C944-B249-5A0556ADABED.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/68AA3C6F-740E-5941-97B6-6E2C230A3B5F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7113A140-1A46-D147-A277-501F3AD2C8D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/749D8B7D-4672-084C-AF93-856EC859C321.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/75099800-F14B-954A-9EE8-F84FD83F7BF3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7578BFA5-EF88-E046-8472-734B45D66C95.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7A602FE7-FF4A-0B45-A0FC-E0C0E71DD008.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7DBAA6F6-20B1-A446-B05D-C72586C40131.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7EEB063E-C262-2445-BBC4-C0649D37072E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/81A34A36-910F-B848-9BD3-143D629B8B6E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8503BDF7-DD23-854E-9CCD-D59A6644C4D0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8BB6E35C-A8BD-014E-97F5-1B96EF5D2225.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8C133032-628D-1B4B-A687-7D860C3BE30C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/8FFB2610-3C97-7640-8B15-89FA860D3725.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9179868E-0F2E-1244-A992-8DEE9F6F7EEC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/93B27EC0-2273-CA43-9B6F-E4DD128FA6E4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9E8CF6A8-00E9-8C4A-B2BC-A9DB15B7E407.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9F00ADD4-3452-D34E-A23C-9CF7CE1ECFF0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B0E6AF9D-3714-FC42-9DDF-A98849B0DBD4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B59A5B6E-EF2B-E245-9B69-50FE61966E08.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B6480D83-FF57-D04F-B7A4-EFD9E2887088.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B70A9B3B-A9CC-E34A-A71D-5A2C8750912C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BA07DFC9-7E34-4D40-9811-3220014D9BB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BA5C7750-A06E-7040-BF33-E40DC846D126.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C309FE54-228E-834B-A7BB-305A8CFD9553.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C8968973-22B8-5E43-ADDA-B52305F84309.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/CCCD0F62-4C71-974F-9B08-E552284561BA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D2E45A3F-221A-0C4F-B32B-7E5911B2B20F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D4E0665C-67B9-FD4D-BFCA-31A4B6667129.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D60BBF0D-D60E-6249-967A-FD3E5229C0CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D6482591-061E-7344-B5B9-91C120A73962.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/E5173133-30A7-574A-B8FC-A00C69E8C584.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EB21A113-F1FB-DE47-B7BF-BE70BCEC767F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EC1E7F7B-6D21-8546-B3B1-7A7B0F04DFF3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F0990855-51B8-FD45-BE6D-74B902E7657C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F298C222-4F00-764E-B2DC-1A158F1ABACF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F6FFA9FC-996C-024B-8802-0B1DF0D8E4A8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/FA76CA2C-E19B-AB4E-8F02-C61A41A6833E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/FCFD3D2F-252D-B048-9D54-230826AB0FC6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/066393D7-A97B-1A4C-ACA6-E5F320F9FC33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0849D85C-F672-DA48-B38C-9CB71999C451.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0D7CDC4F-111A-FB4F-9B44-CF3E0BB10E45.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/125B3D3F-6989-6245-BF16-F8312BA4D443.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/14214F1D-FEA9-AA46-9661-F9E8FD8D7EF8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/145CC37A-6954-6D4B-8098-86878F8FD95C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/15DBCF8D-675F-2F45-B240-E3D8ACCEA75C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/17B523A9-21CA-AC4C-885E-B133C8EC2A58.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/25154026-89F4-914D-BBC2-486363C3A017.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2C7EB9FE-1052-4B44-B536-040C20BD941F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/2E8230A2-ABC7-DE40-92B2-3E5FAFF2D5D5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/40D0964C-31FF-9C43-85B8-D8BF5C9B5FE6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4436F767-F606-A447-9A3B-59CBEEDEA8F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/470009E2-21B4-A04E-8107-AFEC8DEE0FD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4CBB6E87-47D5-4A44-84C4-A5D812EC86F7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4D90D68E-F735-3D4E-AA1C-BB3272FE8265.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/509D5081-52CE-FC49-8191-7501D958E82C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/58B36AB1-E69D-3E49-9A97-1F881431CB79.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/5C9DCBEF-211F-0742-B330-9EC4F947A482.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/629C9422-4F30-F642-9680-B62B2462AE6B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6789BC5A-8996-F24A-BED3-B5F8005673C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6D3A87B1-BDE9-9E48-848C-06A701844531.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6FE0B351-EF84-4047-8BC7-4019AA892A89.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/7448ACBE-0339-1647-B758-742817B5E55F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/75049098-C6FF-6C4E-87E4-4DC8F34A5975.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/75A94CC8-8309-0F4A-82A3-97365A5621D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/770BE323-9E1A-8842-A820-E851D9A5397C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/79547A6F-8468-8A4A-A5D0-F9B7C207F8C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/7AB335C3-36AB-0540-B597-53A96C445F92.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/851C99B5-705F-E24F-B714-EB404BE7DCEA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/870BB419-2150-6742-B5CB-F3E8A3581D31.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/87696E8D-D98A-A740-B61E-00BAEAD84F94.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/88CA4F64-4970-F942-B219-7ECB0C4719BC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8958081D-37CC-9549-92B0-27248FFC0B9B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8A2119B1-65DC-CF41-92F3-4F0EEA17D243.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8A29C9D2-9BAB-8748-9367-716BAEEC80C2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/8F9CE6AF-6D32-7248-B479-7880E71AE4BD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/989FFB9D-78A7-9041-BDF1-125B5D833890.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9AB97EE1-D7C2-BE4C-AE91-207F9FA8A347.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9D05972A-8211-3D4E-92D6-1C5496D04198.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A2F261C1-6C02-4946-B6A1-0AFD1BF01B5E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A7E80411-D26F-5548-96CD-7C4BC7C6F15A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A9138AFA-FFB4-244B-A063-19388C6294EA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B105636B-64C4-D24E-8180-0EC2D1560BA7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B41B3415-1AC2-F34D-BFFC-FA5E557A81DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/BAD9A789-B260-274D-91E7-A931B09F62CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/CBEFDC2B-0FD2-0046-B511-0732AFC9625F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D0D8F478-57C0-BD45-A0FC-33B55573475B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D1A8517F-9F2F-C54E-9866-03D03D21E31E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D3F55188-65F2-4E4A-8B0D-CE5F7A05BF43.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E5048798-2746-7E40-B674-B31B3BACA628.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E6E4EC29-9D21-0A4F-8191-2CB35A5A9B7B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/EA879BDC-5672-D44A-82B0-78D258FEFAE4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/EEE7ECA6-D03E-3246-BADE-721D34307F6B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F410E20C-7068-C146-8D83-777B07B2F4FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F440C2C1-EFF4-CD48-B08B-FDB3AE5D13AB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/FC48E69C-A42A-934E-9D04-297FFB8B29E6.root',
] )
