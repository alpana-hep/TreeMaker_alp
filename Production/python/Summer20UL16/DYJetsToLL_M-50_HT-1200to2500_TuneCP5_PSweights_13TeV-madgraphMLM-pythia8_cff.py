import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/2A834599-DF59-6E49-B4C9-024BD3AAAB10.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2430000/8B8565CD-8008-1543-98E9-8640C5A47DD0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/250000/0177398B-4447-5F43-A1D7-1253653383FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/055B2DEA-7DE8-B444-A23E-C44CB1FCFDBC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/0B094445-0021-FC47-8209-EDA727BAF62F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/0DC363C6-2ACC-5846-8FE2-9A1CC4E8C599.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/174E4026-13C2-F34F-87B8-B72E700E2381.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/1806A801-C497-A14B-8D0D-6201CE21A9DC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/1EF0152E-B3FE-CA44-B1BE-74BAF1FC807F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/212ED062-81E4-2046-BBA2-33245D9BD355.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/25284F40-AC39-E046-82CE-F838A3BAB653.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/32D198F1-109A-4D4B-A33E-2AA982C0E6A7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/3F977508-D2B4-9142-910E-30649CE53AF9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/4631E034-13E5-0C48-B022-FA07156ECAB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/48314143-296E-3D47-A220-04F84DD2829C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/4A95D784-F7DB-4244-B241-3315715AF638.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/5766D657-670D-6448-8CAF-EC5D9C042A72.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/59166BA8-170E-A449-91CB-82F0A050C6BE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/5B68C7E4-B0A1-BD48-AE8D-A193E56A5C3C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/5C6764CB-8841-EE4A-A812-4FDF573A8E39.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/6A47B9AF-2117-FD44-BBD0-B338AF13B2DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/73BDC9E6-880C-1640-A649-ACDEDBC76BF9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/7BF544DC-C469-7148-8B4B-71A835D9E815.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/7FE8C1F1-8EF4-1642-971B-A586E8AD2F49.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/8D93A390-FB38-D841-8820-3EE8E1886BD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/90FAF523-DB3A-2841-8DD6-84DAB4038F1F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/93B812AE-E71E-BA41-BF53-1541693A2D79.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/99AB76A5-0A38-A84D-B013-700159B878E4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/9A884615-B781-1449-8541-ECF3F6042E9F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/9EBAF9FF-4C0F-2142-BA1B-4AF0470D8EB7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/BFED1FFC-5797-4D4C-962D-278296A2CDD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/C16C3F92-6903-EC48-825A-8996D6C1D8A2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/C9C6EFE8-0A8E-504B-8685-135F7FE47AB3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/CB415CD7-BBC8-A048-8591-A2391414351F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/CC911CD5-F2D5-6946-99DD-A3DBD9966498.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/CC9348A3-2CAC-5E45-A9A9-BD81C691447C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/D0A0BBFB-B386-864C-8E91-4197CF3102D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/D1D4A466-9EBF-5D43-B9B1-0D546DA21FEA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/E1E765D3-D04F-AE49-8A34-421742D64F89.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/E2D783D0-E5D1-C34C-A7CD-F4E8DE7646B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/F039FCFA-F1BA-AC45-94E1-6AC6C4F70127.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2510000/F46C8EFB-279E-BE49-B7D9-ADC60032AC9B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/CECE9115-552F-C94E-9634-81253551EA2F.root',
] )
