import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/042B5C8A-971F-3940-BFC9-83F0278CE1A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/04742A9D-DED6-C84B-B6C1-26893B24E002.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/06A70860-376A-304E-9F5B-54510F03C68B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/0C47F822-FA19-E440-AAA5-AE0B3D540CD2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/0DF49582-12E5-644B-84E9-55C4776D66CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/1FABFF57-A735-854F-A041-F679A531633D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/252ACBD9-46B0-C641-B464-110A2C25CE72.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/361B6A10-5AB6-D040-9513-776EF287B63A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/3AD248B1-B272-154F-9FA5-214B41CEF9AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/3B3A7E8A-389D-4246-B044-8A5069DD12F5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/3E62F5C4-8D7D-A849-AB4E-A9FF7D968F63.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/47559115-FE7A-3047-AFAC-61072176AD9F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/48979D10-4AF2-5E4E-AC64-84F169D9825C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/4FA05763-7A66-ED44-862F-26678E3BDC52.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/55D36407-C560-2A4E-911A-D5E94E771473.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5750C8E9-03A1-3447-98E8-58B04AC1A58B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5C46644F-9AF9-E647-844B-05B8E1D7A93D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/5D988A19-3A82-074B-810B-F62AF49F995D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/698BD0E0-887A-5042-8D9A-25F103E59B9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/6DC65D2F-D53C-774E-9DD9-CD9F01749238.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/77ED345F-D67E-FA4D-BA51-0C487D8EF052.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/78D9CD91-0762-FB4F-9B51-121D22007B3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/7CB038AA-1520-B14C-8A5F-0DFB86D651CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/80FF265A-56EC-A541-8736-6E332431A0D5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/811B300A-CAB8-1D43-ADD2-A74DB3BD69B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/827CAF1A-A3FF-C94B-9FBD-A53D48A7D715.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/8C8AAAF5-C6FF-CC4F-BD22-45E18027B16E.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/98A1BF60-4142-4247-BC9E-8D2D9AA99C3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9B67AEB2-37DD-9E44-B514-89D40A6ED96B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9B8793A8-59C3-2A40-A043-3A1D54CD2241.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/9FDFB7B3-41DA-CB4C-AF50-1A4E49F92328.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/AB43A891-CB21-D74E-A86B-170309E369FC.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/AFE0D517-2129-8E4B-88EA-C4214DD426EA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C11F6FFE-8A20-6A4E-8B94-21A00D01530C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C1FCBE03-6E0D-6240-B956-A4256F872B85.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/C921E3AA-2506-F542-B2DE-7017125ED2CB.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CA20F3E9-34D8-F746-B938-8FB9CF010D0A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CCCA6FF9-B361-354F-9F11-12C8A622BF2A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CFA5CD6B-72B5-8A46-ABF0-4DE29CDEC8CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/D85FB272-C323-8644-9ED7-A1EB489BB591.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/DCEB7525-9864-1149-AD98-04B5B46D34C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/DED35E12-0CF7-284F-839B-3570570ADB05.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/E8E81D51-CA6F-3B46-BC52-77443CDE0EA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/EAFAEE9D-0856-6440-8C5E-913726F2252C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/EEA8F7FF-C00F-A742-B1A1-1AA0D972C968.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F06A71EC-CB04-7B49-BE97-F3E7A5E33A71.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F18C1991-99F5-194C-A8EC-690A12CD9271.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/F43B2920-8F60-3047-B42D-496553BAEF4A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/1A23F78F-CB82-604D-A250-19681F2A1964.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/211C25D2-1EE4-754E-9F77-C135C5EA9872.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/110000/2D134213-72BE-3246-9001-04C66C4A9E82.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/035A0D32-85E1-BD4E-92EC-315F91B9BED2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/0454ECD9-63E7-CD4B-8B6F-F71A68886238.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/05A56536-B442-1D46-86D6-049DC10ECA7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/0765A770-0382-6F41-A7B5-EB50DCA4E3A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/0A80A6E2-C2E6-AE4A-B167-58170E56B278.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/0FBFB658-1F9D-8A4A-9F93-2038AEECB87C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/120C49AB-77DF-F646-BDF5-DF5B94CB8088.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/14C06B90-6563-0145-9DD0-D4AAB333984A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/1EC1A256-A17C-B34B-9CB3-49188AFFF731.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/208B327F-DF28-FE48-86E0-D3944C4768AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/25A60359-3604-E245-BA16-F59A13A083F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/260806BD-2A49-EC4F-945E-8C42A60C9CC6.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/2D90A891-A714-0545-8289-D4C356124716.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3099716A-5D8B-D246-B237-156A285A6C98.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3223DAF6-A8C8-4445-B2BA-1F33C599FE14.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/33B811BD-1D5E-114D-AF85-31B41C2C56A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3720BD82-F72B-5D49-BE66-7BE4AA9CAD08.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3C312851-116F-774E-815E-8222296CB8C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3DF71ACE-2DB2-A642-8B89-B9C2512F3DBA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3F07EDCE-237B-2B4C-B108-7D0F3B514889.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/3FF83795-8F03-E24E-B8BE-8328DAAA4DDF.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/426B5357-8721-814F-B8E3-BCA07D7B50FC.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/4331D3A4-3735-7943-AA38-7F41ED794B72.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/47165ECA-321F-EA46-881F-2BA6395581C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/4843AE92-215F-B245-AC2B-BF6E7023D9A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/4A4EC21F-A8F2-834A-ACE1-517F81BF0524.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/4EA7A810-A76E-1D48-A173-5D59B1FF63FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/57851C95-BE55-B34B-8DEE-D6B134C301C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/5A8324AB-48A3-0649-85D9-CCA91AE1793D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/5D344ED7-B968-BF4F-84E9-1C9960EABCB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/5E2E0091-7668-5644-99E3-47A941454675.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/5E8E645E-AA09-2B4F-9E8B-F28C9ACCD6A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/60302096-0246-1C46-9172-B61C81867174.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6A39E29C-3981-0A4A-ACCF-376D92ADE393.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6B065FBC-EBEC-5941-8A8E-087DC3B33980.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6B7438E4-5256-D348-9E49-C4431F8C101C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6D1C73FD-5CEB-A642-8B05-4F7076DD57ED.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6E99E458-42BD-974A-A8B3-CEC178223661.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/6EA8C997-6F96-4C45-99FF-9403F7D06C82.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/72D43D5D-E44E-A742-B438-73CEFAC43F57.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/745E8D73-3C35-D24F-8A42-F3403121884C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/74B254A3-7FC5-3E4C-96DF-F4C0DD3AA017.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/7765DE0B-622D-F54F-91E8-1E566D48FB1F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/7AA31DD1-AB8D-D641-8225-31B1ABE07EE5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/7F0A6C04-1C5B-8241-9DA4-521D594B0F98.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/7F799B68-E0E3-DD44-A6BD-FF32B80C4BA4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/8017E2F3-BBDF-6344-A692-17DF88D9719A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/873A49E5-F484-FE43-8CAA-00C43E76D6D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/8C2EACC5-22AE-7F45-BE97-EDBD961B233F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/8DFF70F5-2CB3-494D-A453-EC9F546ECC4A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/8FB3B5E8-7210-7340-A5E2-F7D0D1136213.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/915EAEA6-27BB-2341-8272-8ED76403105D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/92F0DDB0-E0D2-C14E-AC3B-F12FD2DC91F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/93534E43-30BD-A945-9567-EA7C9A8272C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/93DBEEA5-2256-CD48-A735-731DBFBE2A83.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/9961026D-1D18-794D-A61B-01B6887B2FD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/9965FE96-B2EC-9544-8F4A-78462826E820.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/9DAC801B-BD4C-1A49-8DFC-EDD689FFB847.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A5D54C99-6461-094E-A994-33B49D300D33.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A6B66DE5-8993-C548-A21B-7887F2CE9884.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A6D4F231-28BE-3545-9C02-5B3A2645454D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A7BD9C3B-37B1-BE4D-B8E2-9322E3B1CBA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A8E23300-8125-0F40-A93F-BF7F0EC51CCA.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/A98D687C-1767-7840-8A3B-D308915A67E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/AA9BD86A-6916-DB4D-9A42-475B8803B793.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/AE9E1674-BFA9-9C41-9DA4-D762DD7C680F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/B1269E24-FADB-8444-910B-39B816E68EC6.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/B28A6EB5-89DF-184F-8113-2175BC22AA75.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/B3B9FDD7-7A8B-9B46-BFF0-BDD15240C620.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/BA78BAFA-7BCD-2C43-B79C-C57FF02E70A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/BC023CB0-0D67-EC42-B809-9379CD1F16F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/BCA683BD-A230-4A43-8E1F-8BC86E6771F1.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/C38688A2-C4D9-F341-9783-F55BE130D12F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/C58E190A-5845-9949-B9F6-FAAF2B6CE8E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/CA82D31B-00E0-8A47-AFCD-1EECB8978E7D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/CD774F62-D0E3-074A-A643-D6379BA7C232.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/CDE9FD0B-D031-114A-9C87-B3D138FFB69A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D025C2D2-E35B-154E-889D-A900AD8C4BD2.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D1B2C220-9D96-1840-86D6-66B342EFD27D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D1D1388E-B278-134A-9921-9ABDCF84A59A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D37E312A-97AB-364E-8968-0579F4F27746.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D4DBA90C-21FB-EF49-B34C-035900298322.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D61141B4-361A-A545-975D-2F71E1E10FBB.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D69ECD5F-205E-6646-913D-8C7283948FA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/D7408950-2270-2F42-A878-3666DC826D83.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/DF61B2B3-E47F-7A4F-B82D-1BBB83F2AB0C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/E2B74625-3118-1E42-B372-E7B0B120AB90.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/E34BCF99-0BA3-124B-818F-005B97E676FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/E996C3DC-A05F-E24B-BF10-849A6889CC88.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/EC4F3998-392C-FE43-B7C5-D6ED929E230C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/ED55ECCC-2333-BB42-8D40-57A265ADAD18.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/EF4D5CB5-713E-744D-B643-8E6ED873137A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/F09663DB-FAA6-684D-AEE8-3E5AA36FCB7B.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/F68D3FB3-D465-AA48-861F-B46BFD1D7D81.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/F7723520-BEB7-C64A-80CB-CA0A41C4715D.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/F7DCD426-31F1-5B46-B0D6-2DEAA62C0E2F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/FB550FE0-7160-814D-9A78-F21E91FDD5A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/WGJets_MonoPhoton_PtG-130_TuneCP5_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/60000/FCD94984-4A04-6442-A654-87C1D7A215B8.root',
] )
