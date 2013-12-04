import FWCore.ParameterSet.Config as cms

process = cms.Process("Skim")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
#process.MessageLogger.cout.threshold = cms.untracked.string('INFO')
#process.MessageLogger.debugModules = cms.untracked.vstring('*')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source ("PoolSource",
  fileNames = cms.untracked.vstring(
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_10_3_Ghm.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_11_1_wA4.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_1_1_9dF.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_12_1_4G9.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_13_3_hPw.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_14_3_oRw.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_15_2_det.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_16_2_puD.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_17_2_sX2.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_18_3_G1X.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_19_1_Hpo.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_20_1_s4C.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_21_2_0pW.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_2_1_KAL.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_22_3_5zy.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_23_2_7Ou.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_24_1_ZcP.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_25_2_Os8.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_26_2_MfZ.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_27_2_rbW.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_28_2_UpN.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_29_1_afc.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_30_2_MVi.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_31_2_aZu.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_3_1_QGJ.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_32_2_qZ3.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_33_2_oYt.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_34_3_Zbj.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_35_2_3kU.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_36_2_0gU.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_37_2_oFc.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_38_2_jYt.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_39_1_0Pl.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_40_2_co8.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_41_2_Rqg.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_4_1_FLU.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_42_3_r0U.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_43_2_Ykt.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_44_2_Tfv.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_45_2_3gf.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_46_2_tqq.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_47_2_Pq7.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_48_3_0wy.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_49_1_VON.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_50_1_YdV.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_51_2_4tD.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_5_1_wTt.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_52_3_Y6H.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_53_2_n78.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_54_3_jyA.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_55_2_iGe.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_56_1_flS.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_57_3_P7R.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_58_1_CV4.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_59_2_xam.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_60_3_0nz.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_61_2_2wK.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_62_2_mbG.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_6_2_cJh.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_63_2_7iD.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_64_2_f9o.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_65_2_LwI.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_66_3_Zik.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_67_1_WIs.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_68_1_Jf7.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_69_2_lCX.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_70_3_18G.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_71_3_uYp.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_7_1_c95.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_72_1_DVq.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_73_1_17n.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_74_1_4TL.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_8_3_Jak.root",
"file:/raid5/digiovan/root/CMSSW_3_9_7/SkimsDATAMuRun2010B-Dec22ReReco_v1/Run2010B-Dec22ReReco_v1_9_1_7xY.root"
)#,
#  eventsToProcess = cms.untracked.VEventRange(
#'143833:813702229',
#'144112:418839543',
#'146644:352104961',
#'146804:270023381',
#'147219:163266923',
#'147222:238019483',
#'147284:213049028',
#'147390:564394453',
#'147927:139268964',
#'148032:124501662',
#'148862:854558112',
#'148952:241708509',
#'149181:647771023',
#'149182:257337642')
)

process.filter = cms.EDFilter("TinyFilter",
   events = cms.vstring(
'143833:813702229','144112:418839543','146644:352104961',
'146804:270023381','147219:163266923','147222:238019483',
'147284:213049028','147390:564394453','147927:139268964',
'148032:124501662','148862:854558112','148952:241708509',
'149181:647771023','149182:257337642')
)	

process.filterPath = cms.Path(process.filter)

#process.FEVT = cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string("/tmp/kkotov/highMassBumpSkim.root"),
#        outputCommands = cms.untracked.vstring("keep *"),
#        SelectEvents = cms.untracked.PSet(
#            SelectEvents = cms.vstring('filterPath')
#        ),
#        dropMetaData = cms.untracked.string("ALL"),
#        maxSize = cms.untracked.int32(50)
#)
#
#process.outpath = cms.EndPath(process.FEVT)
