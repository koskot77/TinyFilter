#include "TinyFilter.h"
#include <stdlib.h>
#include <iostream>
#include "Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.C"

using namespace std;

bool TinyFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup){
   int run   = (int)iEvent.id().run();
   int lumi  = (int)iEvent.luminosityBlock();
   return isGood(run,lumi);
}
