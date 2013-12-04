#ifndef TinyFilter_h
#define TinyFilter_h

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <set> 
#include <utility>

class TinyFilter : public edm::EDFilter {
private:
        virtual void beginJob(void){}
        virtual bool filter(edm::Event&, const edm::EventSetup&);
        virtual void endJob(void){}

public:
	explicit TinyFilter(const edm::ParameterSet&){}
	~TinyFilter(void){}
};

#endif
