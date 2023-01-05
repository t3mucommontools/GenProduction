ifeq ($(strip $(GeneratorInterface/ExternalDecays)),)
ALL_COMMONRULES += src_GeneratorInterface_ExternalDecays_src
src_GeneratorInterface_ExternalDecays_src_parent := GeneratorInterface/ExternalDecays
src_GeneratorInterface_ExternalDecays_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_GeneratorInterface_ExternalDecays_src,src/GeneratorInterface/ExternalDecays/src,LIBRARY))
GeneratorInterfaceExternalDecays := self/GeneratorInterface/ExternalDecays
GeneratorInterface/ExternalDecays := GeneratorInterfaceExternalDecays
GeneratorInterfaceExternalDecays_files := $(patsubst src/GeneratorInterface/ExternalDecays/src/%,%,$(wildcard $(foreach dir,src/GeneratorInterface/ExternalDecays/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
GeneratorInterfaceExternalDecays_BuildFile    := $(WORKINGDIR)/cache/bf/src/GeneratorInterface/ExternalDecays/BuildFile
GeneratorInterfaceExternalDecays_LOC_USE := self cmssw FWCore/Concurrency FWCore/ParameterSet FWCore/Utilities FWCore/Framework FWCore/PluginManager heppdt SimGeneral/HepPDTRecord clhep hepmc GeneratorInterface/Core GeneratorInterface/LHEInterface GeneratorInterface/EvtGenInterface GeneratorInterface/PhotosInterface GeneratorInterface/TauolaInterface
GeneratorInterfaceExternalDecays_EX_LIB   := GeneratorInterfaceExternalDecays
GeneratorInterfaceExternalDecays_EX_USE   := $(foreach d,$(GeneratorInterfaceExternalDecays_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
GeneratorInterfaceExternalDecays_PACKAGE := self/src/GeneratorInterface/ExternalDecays/src
ALL_PRODS += GeneratorInterfaceExternalDecays
GeneratorInterfaceExternalDecays_CLASS := LIBRARY
GeneratorInterface/ExternalDecays_forbigobj+=GeneratorInterfaceExternalDecays
GeneratorInterfaceExternalDecays_INIT_FUNC        += $$(eval $$(call Library,GeneratorInterfaceExternalDecays,src/GeneratorInterface/ExternalDecays/src,src_GeneratorInterface_ExternalDecays_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS),))
endif
