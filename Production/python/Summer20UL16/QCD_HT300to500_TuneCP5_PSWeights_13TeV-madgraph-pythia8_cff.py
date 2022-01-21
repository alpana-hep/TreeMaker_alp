import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/0D6A071A-42CD-304E-8120-113F900BFD7A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/0D80DDB3-4CFB-D54F-BA11-B786A129C5C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/1768C2FA-DAEF-B448-913A-022C7A3AB7C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/1AD1BE8B-1C8C-4046-A7F0-65EF5237E914.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/1F1802AE-7F12-A84B-91C9-47691A78F18A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/214D0EC3-BEE9-8640-A5EE-8554016EE6C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/23776DDB-1EFE-2B47-ABF5-71328752C538.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/33413CBA-4DEB-804D-ADF2-8851A20D168C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/3E86CA7F-024E-734C-B48A-7E7B74320481.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/49A56D33-03FB-3043-8613-3028BC8198D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/4A4D33C2-C076-494E-8140-03E6D918BB68.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/683F1000-6B3A-B641-AD63-F4969CF1A26F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/6842746A-0E7D-4D40-82D4-0F2645CFDEBD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/6CD75210-3DD3-B040-A589-15DAAB549680.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/72B1E639-B1F1-6D45-9D4A-6E12273F7BB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/73737D35-7036-A74B-A384-9BB2E485BECF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/75870BCE-B695-374C-9EB6-49803C471D71.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/75D84447-5187-F340-A0E6-1FA31EBE416C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/80868715-7B94-A149-B79D-95A8BD0022B8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/83E5AF37-D896-9943-BAD5-63AF7DDA82E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/93FA0C1C-7E3F-3A44-A611-71AF4DE40CD5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/9C381A06-F65E-C84C-B8BA-8C0903240673.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/ACB9ACA4-3363-6940-A953-4C73FAE1F416.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/C637B98A-3B5E-8B4D-9F74-A2548027422F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/D671C15D-882D-6245-AEC4-DEB84D3AB672.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/F4D2EC4E-50D1-0244-9459-87B0ECEE1FAB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/00B601EC-44C6-0441-AF15-03D378CCB063.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0253B886-452E-DA41-8FBE-8D52D8CB60FD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/037D69E8-73EB-4D44-AF3A-7131F590FB19.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/041761C0-B371-4C45-A065-93C94C62D511.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/07B3DECB-AE01-ED40-8AC9-0775735FE530.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/07F4F00D-D366-EE4C-974D-CEC8DDDCDE71.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/09777C4E-0FE2-194E-A4DC-B8B027C70D92.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0A972BDA-660E-1B45-8C3B-238CE477D54E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0C93667E-67FD-074B-9E26-A15126F55FB0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0D76B2AA-F17B-EF4B-AB1C-E2EEFA2CE9B6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0F3FAF6D-B038-5A46-8A93-03D31B178453.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1030BA72-E740-BE48-A496-9EFC09649486.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/10E2FF4D-0142-B142-9009-4B8C29A40387.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/11A7A735-52BE-B747-A263-8B09BC0CCFFB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/11E21025-EF19-2647-99B6-0E50238EB2FD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/12670F13-712A-444D-90BA-12AD123B2CC7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/12D7943B-BC3A-E44A-B255-873F0FF26097.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/15981198-05B1-2544-9D53-80BA6FE3E281.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/16C05F33-1B8F-2243-8744-0AACBFF1C30F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1BE1643E-F1F7-F542-8848-1F5711086286.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1D43480C-8EE9-1246-84DB-B594D536EEB9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1DB6F87E-5F17-8445-8457-DE7560F1D6C9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/21C77232-7C40-7F42-B056-4204A54A57EB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/21E3F153-C8B1-D24A-9D76-66CAAAF3BE2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/236B5608-2E66-3940-854B-4A8503CE625E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/254853ED-030A-664E-AE37-6CE0D4E4CFC3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2703EB5F-57B2-694B-9C93-D899024CC2E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/28067E17-857E-2344-84E9-1E57ACD36229.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/288C8F43-E407-F848-A8B1-EBD8D0A99C52.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/29B1A84D-9E91-B943-85CA-8D7496DA3B33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2B169288-5F1C-9D42-91E5-2A1F658402AD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2CE669C7-16F7-EF4C-A79A-D5CAE869DD21.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2D66D29B-CBEB-A649-A5CC-2DD24320D93A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2F1481B6-A924-8947-AACF-1358B9A7E40F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2F7A3CDE-3395-4B45-8A08-0E919B0D8765.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2FB3C2E5-74BB-8041-B870-AB5990D323E7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2FE23500-4A9C-5143-90B9-D32FF0BC60E6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3251922F-1DA7-A149-94DD-EB19D65FD212.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/33CD71C6-F728-2742-A4F5-02A77AE6E8A7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/34095B59-B324-D94A-B6A7-317A99F6E1A1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/34B5908E-01BA-B445-B8B3-1A4C371F5AA4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3598F697-ED63-0F44-BEDC-7A529DB5D6B9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/36678655-2DD9-034A-954D-76FFDA6D46C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/366F6531-F58D-3C49-B1C4-826E91B581D1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/36ADDD4B-37C0-0F46-AC07-B0ED18CD521A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/36B06C80-4BF1-5145-A8EF-A0735737BB98.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/37328CC9-017D-424F-A795-25D670C8313F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3A836FF3-5CC0-DE4B-9433-4D2E040255C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3B0CC19E-79A5-0E48-981D-380CBD8AA32D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3D166C84-395B-4049-B15B-6F450DC3662C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3E3EC6CA-AA30-FA4E-AF47-809DB3630C42.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4213095A-4DD0-6143-8B09-15D18EAAB6F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/42903520-AA0E-2640-AEB6-8A7979B9C17D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/438034FC-72E4-B34D-A812-99F104D901C0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4390AECD-7364-B346-88FA-4AC7DC6E04FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/44E5D71E-D801-7141-9D8A-D78D522E895E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/45397411-1074-B34F-B722-B34C19C3F797.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/458103B3-39F9-9542-A53F-4272B35432EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/46050567-8B7A-A84B-8EF6-DBF12CB1AE94.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/486A43C5-C96B-BA48-801E-C42F1AF618FD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4C4C09F5-2AEB-3145-8465-B86249C4E180.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4EDB96AC-F335-2649-92A5-F43CDDE452EB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4F728F63-4D04-8A4F-B91B-D17CE90AB91B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/4F89C9CF-FE47-C84F-97FB-D95E73BC1EA1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/56DD0EA3-621B-C948-8F20-9F5E7A5D942D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5AD7869A-18B4-1D43-AB0F-B8FEADBE0366.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5B51F5C3-0688-B448-8359-483F3DF3AB62.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5B9BF9D1-BF7E-5D47-BE3E-E1E439F8D959.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5C3B11AF-9C17-AC41-A6FC-F355359F8FA8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5E147B1D-509E-AD45-B75F-3833C703635B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/5F0B3B38-B394-F14C-A4D0-A9B8CDE18F82.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/62A87B9A-4341-AE46-BB40-93F9C8588E0F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/658E898C-3182-994B-A2F9-6CE4EB342AB9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/65E87447-A42B-7D4C-BD09-B37177B0FA36.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/6678A77B-5C73-2B49-8E8A-D5798A78FC61.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/6726D837-2B28-494C-9257-809C6EE87E4E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/6E613EFD-4107-534E-9543-E6A3370F1D54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/6FB9C5C3-B152-944E-A487-A7A990692A2A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7083EF09-EA29-CB41-93CF-E4AA52399378.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/709D7ECE-4BED-B044-A10D-3FFB24994F78.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/73AD9AB3-37E3-DF45-B532-1554487BA47D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/75384707-1AA2-C444-8699-6EF0660D4B15.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7558A2C3-5D9F-DB44-BEE6-BB091D65D956.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7741E88C-87B8-9644-AC6A-20DF16CDC537.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7A04B9F6-D735-7B4A-9651-C0EA4BFE7820.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7A04D453-016D-0D43-882F-0CBA25EAAD6D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7AC25934-2396-C847-8F23-39BF84106965.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7CDE1D3D-9D1A-EF42-B2A3-13BC4CE18FF8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7E8D8CAF-AF33-9442-8264-78208AAA1E33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/80754345-67A6-0D4B-A6AD-D64DBE1570EA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/843C63EC-467B-1D48-B9E7-72D5528F9D62.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/85E57DAE-EBE7-7B49-8348-929FE5021F14.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/86EE6F60-7EB3-7D48-98C6-E734A88C52BA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/87D23933-F7A7-4D43-855C-1BAF57A0C11F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/8ECCD7EA-B147-EB44-B307-880A852C76B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/917D79EC-D2E5-3A4D-BAB6-F215FF7D3427.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9224CEA8-458F-714E-AE38-9238978AD896.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/932164FD-2B63-B645-AAB9-2DF207C1C0D9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/95101F85-E267-A940-B328-08E8F7EF8B42.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/960D65E9-CC76-BA46-9EF4-7558D26E2244.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/960D89E4-234A-124B-8A9C-F35B1FB69169.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9CA9B56B-A1D9-5342-80F5-2A63DB74827F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9D83C6AC-7B56-0F42-8307-C8B354FA10E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9E1C9930-A178-2E4F-A6D0-44D8D6EBE50B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9E225190-F780-D142-A58F-A55B46F37403.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9FA52515-B266-E043-ACDA-0DD8C8AAE083.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A1868EF6-60F2-8F4D-BA59-B20C2EDABDDA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A1B08E3C-A96B-A743-8A4E-86E48D318EDC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A3D8392D-5195-EE42-9643-8B196251FBF0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A4027A90-0715-7347-90C6-A48B79637E7A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A430E7CD-569F-DE45-8842-4D2D8AB8F8FD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A43B0D5E-F84D-1242-831A-A76212C3DFD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A5E46ED8-DC8B-5D4D-960B-ACD52430F628.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A77D8240-27E6-1F44-A18D-1017B00FFD92.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AADE35FD-4409-2C42-8961-7D7ED2F20948.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AC13522D-F528-4746-ADFD-CB112AA6AB9A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/ACAA4B72-6C6D-C24E-BA2E-25665566A3D7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AEC76D3C-3EBC-E24E-A432-2BB2007F7262.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AF219981-0A86-444D-8909-C5C45BA86C04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B18C48BC-2631-C44A-AFDD-1514CBF31B7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B28FB3AF-3D25-0C43-A53D-01DF6738FD34.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B3BBBB48-51DF-204A-9C24-2597FF5A4B04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B4C2ADF4-0C2F-C042-BACB-594E7CC961F3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B51EC194-DA38-EE40-8197-B8BFA129F089.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B55627ED-F0FD-3D47-B5A8-EC9E900E9866.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B6017973-5EFE-334F-AF73-8D2E313D9489.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B7E0BF34-4E59-6948-B691-010BE0075BC1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B8C237B8-9AB9-7942-B77C-D361CEA42380.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B9538A82-75FD-8B47-B153-395028F15CDF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B9B3FAB1-EE7F-2245-BCDD-970F0D73DE2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BBB7C125-24C1-914A-94CA-12B5C28C9784.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BE9F3CB4-D2D0-9B4C-9F4A-0E0134640EC7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BEEA5C6C-4C4E-2D4E-AD60-EB98F2F16C95.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BF8D2DC6-8F6F-6C40-B4C5-453624AF53F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C09AC15F-8761-414B-95DB-78E0B5A64FFD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C1FD5E56-9220-8642-89DF-E3200CC15BBD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C4C28DAE-6810-274D-ACBA-C4FDBB43E856.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C53A5945-1DDF-864B-B333-C767610162AB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C5AE8A75-9E19-DE45-AFBA-4D7F0698A2E0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C6E6E5DB-9EAC-DF4A-AD12-309D0F24AA84.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C92FE2AC-448E-D74D-888D-AFB0C2004A6D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CB7FFDDB-551C-0B40-8459-03F67570A39B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CC6BCB5F-E6B9-9844-8EFE-CAC18C02B80B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CD9394DE-3CF5-3B4B-90E1-CF8EDB3BA546.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CDBDD868-ECA4-0644-A17A-16BE0C5CA036.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CE325CC2-6791-5348-AAC2-74E4C8FDBF00.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D0AC45A3-622C-F74D-AD72-AB5512DE38C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D1074C02-D015-E14B-B7D3-34920284D56C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D2282C64-97DF-2045-967C-61E7B9603C72.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D2A0A0F1-74E2-3B47-B2CD-3ED61779D0C1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D3C83C23-EB16-FB47-A37A-D28C0C3B9769.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D84D6A58-4D08-EB4D-9A21-869D6162E881.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DC18EFD4-3D06-CD42-B72A-096EA82BCCBD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DCBFD6D6-9E08-8144-BC95-1FED2129463B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DD5D874E-ED34-F54C-975B-457E1261FA0D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DF9FF4B4-1512-6546-B9A2-399B899DD733.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E2187A3A-34E5-F943-AEB1-C6E28AE4B9E5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E41E9BDD-AFE8-7942-A531-A22E071CAFC1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E4836943-F823-F94C-9DC2-8D9247D4B77F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E88124A6-BA64-3D47-A927-46D625961D40.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E8B0CE01-459B-6247-9BE5-5DD41C03099B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E9189EE7-53C6-3340-8B2C-84DEC3696314.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E97F1B27-EFD2-224C-B7EC-DA99480E085B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EA5E892D-7A98-2C49-8012-0287BFFC3065.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EC0A8C65-110D-A247-9839-7C2EECFE203B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EE7AA1E9-DE36-B643-8F80-458C7E459867.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EF50F303-00C5-BF4C-BE43-398B4168BDBB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EFC0BADE-26B9-0F48-A5E8-2E55597D03F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F3400E40-87B2-5143-85D8-4727637EAE8D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F3B65B43-C87C-7943-83DB-6B4BD3031928.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F4FE3D01-2FB8-B141-B2AD-9CA6ED2313F4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F63AABD5-1FE1-F04C-8C64-BA9B8C493E48.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F8E4C47A-9C8D-2F42-9CEB-DC65C150DF2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/FAEFBBCB-C87E-BC48-AE23-B86CDCFAF347.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/FCF0CD67-E2D1-1343-B2B9-5077BCE2C721.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/FD26F360-1D78-9B4B-8BD9-CBCC7DFECB9D.root',
] )