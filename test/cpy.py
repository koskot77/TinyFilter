import FWCore.ParameterSet.Config as cms

process = cms.Process("Copy")

#process.MessageLogger = cms.Service("MessageLogger",
#    cerr = cms.untracked.PSet(
#        threshold = cms.untracked.string('ERROR')
#    ),
#    debugModules = cms.untracked.vstring('*'),
#    cout = cms.untracked.PSet(
#        threshold = cms.untracked.string('WARNING')
#    ),
#    destinations = cms.untracked.vstring('cout',
#        'cerr')
#)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string('INFO')
process.MessageLogger.debugModules = cms.untracked.vstring('*')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(21)
)

process.source = cms.Source ("PoolSource",
  fileNames = cms.untracked.vstring(
#"file:/tmp/kkotov/143657_517106802.root",
#"file:/tmp/kkotov/143833_813702229.root",
#"file:/tmp/kkotov/143961_87538283.root",
#"file:/tmp/kkotov/144112_418839543.root",
#"file:/tmp/kkotov/146644_352104961.root",
#"file:/tmp/kkotov/146804_270023381.root",
#"file:/tmp/kkotov/147219_163266923.root",
#"file:/tmp/kkotov/147222_230562567.root",
#"file:/tmp/kkotov/147284_213049028.root",
#"file:/tmp/kkotov/147284_262943463.root",
#"file:/tmp/kkotov/147390_564394453.root",
#"file:/tmp/kkotov/147927_139268964.root",
#"file:/tmp/kkotov/148032_124501662.root",
#"file:/tmp/kkotov/148829_114608339.root",
#"file:/tmp/kkotov/148862_854558112.root",
#"file:/tmp/kkotov/148952_241708509.root",
#"file:/tmp/kkotov/149011_781834399.root",
#"file:/tmp/kkotov/149181_1407263787.root",
#"file:/tmp/kkotov/149181_1476872240.root",
#"file:/tmp/kkotov/149181_647771023.root",
#"file:/tmp/kkotov/149291_274782070.root"
"file:/tmp/kkotov/146589_120477286.root",
"file:/tmp/kkotov/146804_347701870.root",
"file:/tmp/kkotov/146944_180111440.root",
"file:/tmp/kkotov/147048_172773368.root",
"file:/tmp/kkotov/147114_623466180.root",
"file:/tmp/kkotov/147196_77887568.root",
"file:/tmp/kkotov/147219_14588205.root",
"file:/tmp/kkotov/147926_323505790.root",
"file:/tmp/kkotov/147926_368148849.root",
"file:/tmp/kkotov/148032_65702338.root",
"file:/tmp/kkotov/148822_148569956.root",
"file:/tmp/kkotov/148862_58243174.root",
"file:/tmp/kkotov/148864_505003177.root",
"file:/tmp/kkotov/149011_279220263.root",
"file:/tmp/kkotov/149011_492051113.root",
"file:/tmp/kkotov/149063_117418165.root",
"file:/tmp/kkotov/149291_433988284.root",
)#,
#  eventsToProcess = cms.untracked.VEventRange('133875:6290')
)

process.FEVT = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string("/tmp/kkotov/highMassBumpSkim2.root"),
        outputCommands = cms.untracked.vstring("keep *")
)

process.outpath = cms.EndPath(process.FEVT)

