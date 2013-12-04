import re

f   = open('bump.txt', 'r')
log = open('l.txt',    'r')

file2event = {}
run2event  = {}
rec2event  = {}

for line in log.readlines():
    m = re.search("Successfully opened file file:(/raid5/digiovan/root/CMSSW_3_9_7/[\.\-\w\/]+)", line)
    if m != None :
       new_file = m.group(1)

    m = re.match(r"Begin processing the (?P<record>\d+)\w+ record. Run (?P<run>\d+), Event (?P<event>\d+), .*", line)
    if m != None :
       if new_file != file :
          first_record = m.group('record')
          file = new_file
       if m.group('event') in file2event :
          print "Karaul: " + m.group('event') + " found in more than one file: " + file2event[m.group('event')] + " and " + file
       else :
          run2event [m.group('event')] = m.group('run')
          file2event[m.group('event')] = file
          rec2event [m.group('event')] = m.group('record') + "-" + first_record + "+1"
#          print m.group('event') + " in run " + m.group('run') + " in file " + file

log.close()

for line in f.readlines():
    parsed_line = re.search('run # (\d+) event # (\d+) .*', line)
    run   = parsed_line.group(1)
    event = parsed_line.group(2)
    if event in run2event :
       if run == run2event[event] :
          print "Found " + event + " in " + file2event[event]
          
       else :
          print "Karaul2!"
    else :
       print "Karaul3: missing " + event

    config = "\n\
import FWCore.ParameterSet.Config as cms\n\
\n\
process = cms.Process(\"Skim\")\n\
\n\
process.load(\"FWCore.MessageLogger.MessageLogger_cfi\")\n\
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)\n\
process.MessageLogger.cout.threshold = cms.untracked.string('INFO')\n\
process.MessageLogger.debugModules = cms.untracked.vstring('*')\n\
\n\
process.maxEvents = cms.untracked.PSet(\n\
    input = cms.untracked.int32("
    config += rec2event[event]
    config += ")\n\
)\n\
\n\
process.source = cms.Source (\"PoolSource\",\n\
  fileNames = cms.untracked.vstring(\n\
\"file:"
    config += file2event[event]
    config += "\"),\n\
firstEvent = cms.untracked.uint32("
    config += rec2event[event]
    config += ")\n\
)\n\
\n\
process.filter = cms.EDFilter(\"TinyFilter\",\n\
   events = cms.vstring('"

    config += run2event[event] + ":" + event
    config += "')\n\
)\n\
\n\
process.filterPath = cms.Path(process.filter)\n\
\n\
process.FEVT = cms.OutputModule(\"PoolOutputModule\",\n\
        fileName = cms.untracked.string(\"/tmp/kkotov/"
    config += run2event[event] + "_" + event + ".root"
    config += "\"),\n\
        outputCommands = cms.untracked.vstring(\"keep *\"),\n\
        SelectEvents = cms.untracked.PSet(\n\
            SelectEvents = cms.vstring('filterPath')\n\
        ),\n\
        dropMetaData = cms.untracked.string(\"ALL\"),\n\
        maxSize = cms.untracked.int32(50)\n\
)\n\
\n\
process.outpath = cms.EndPath(process.FEVT)\n\
"
    fileName = run2event[event] + "_" + event + ".py"
    out = open(fileName, 'w')
    out.write(config);
    out.close();

f.close()
