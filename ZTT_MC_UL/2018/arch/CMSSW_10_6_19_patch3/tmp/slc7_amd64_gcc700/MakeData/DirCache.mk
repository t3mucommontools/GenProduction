ALL_SUBSYSTEMS+=GeneratorInterface
subdirs_src_GeneratorInterface = src_GeneratorInterface_ExternalDecays
ALL_PACKAGES += GeneratorInterface/ExternalDecays
subdirs_src_GeneratorInterface_ExternalDecays := src_GeneratorInterface_ExternalDecays_python src_GeneratorInterface_ExternalDecays_src src_GeneratorInterface_ExternalDecays_test
ifeq ($(strip $(PyGeneratorInterfaceExternalDecays)),)
PyGeneratorInterfaceExternalDecays := self/src/GeneratorInterface/ExternalDecays/python
src_GeneratorInterface_ExternalDecays_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/GeneratorInterface/ExternalDecays/python)
PyGeneratorInterfaceExternalDecays_files := $(patsubst src/GeneratorInterface/ExternalDecays/python/%,%,$(wildcard $(foreach dir,src/GeneratorInterface/ExternalDecays/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyGeneratorInterfaceExternalDecays_LOC_USE := self cmssw 
PyGeneratorInterfaceExternalDecays_PACKAGE := self/src/GeneratorInterface/ExternalDecays/python
ALL_PRODS += PyGeneratorInterfaceExternalDecays
PyGeneratorInterfaceExternalDecays_INIT_FUNC        += $$(eval $$(call PythonProduct,PyGeneratorInterfaceExternalDecays,src/GeneratorInterface/ExternalDecays/python,src_GeneratorInterface_ExternalDecays_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyGeneratorInterfaceExternalDecays,src/GeneratorInterface/ExternalDecays/python))
endif
ALL_COMMONRULES += src_GeneratorInterface_ExternalDecays_python
src_GeneratorInterface_ExternalDecays_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_GeneratorInterface_ExternalDecays_python,src/GeneratorInterface/ExternalDecays/python,PYTHON))
ifeq ($(strip $(EvtGenTestAnalyzer)),)
EvtGenTestAnalyzer := self/src/GeneratorInterface/ExternalDecays/test
EvtGenTestAnalyzer_files := $(patsubst src/GeneratorInterface/ExternalDecays/test/%,%,$(foreach file,EvtGenTestAnalyzer.cc,$(eval xfile:=$(wildcard src/GeneratorInterface/ExternalDecays/test/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/GeneratorInterface/ExternalDecays/test/$(file). Please fix src/GeneratorInterface/ExternalDecays/test/BuildFile.))))
EvtGenTestAnalyzer_BuildFile    := $(WORKINGDIR)/cache/bf/src/GeneratorInterface/ExternalDecays/test/BuildFile
EvtGenTestAnalyzer_LOC_USE := self cmssw FWCore/Utilities boost hepmc root FWCore/Framework SimDataFormats/GeneratorProducts
EvtGenTestAnalyzer_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,EvtGenTestAnalyzer,EvtGenTestAnalyzer,$(SCRAMSTORENAME_LIB),src/GeneratorInterface/ExternalDecays/test))
EvtGenTestAnalyzer_PACKAGE := self/src/GeneratorInterface/ExternalDecays/test
ALL_PRODS += EvtGenTestAnalyzer
EvtGenTestAnalyzer_INIT_FUNC        += $$(eval $$(call Library,EvtGenTestAnalyzer,src/GeneratorInterface/ExternalDecays/test,src_GeneratorInterface_ExternalDecays_test,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS),edm))
EvtGenTestAnalyzer_CLASS := TEST_LIBRARY
else
$(eval $(call MultipleWarningMsg,EvtGenTestAnalyzer,src/GeneratorInterface/ExternalDecays/test))
endif
ALL_COMMONRULES += src_GeneratorInterface_ExternalDecays_test
src_GeneratorInterface_ExternalDecays_test_parent := GeneratorInterface/ExternalDecays
src_GeneratorInterface_ExternalDecays_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_GeneratorInterface_ExternalDecays_test,src/GeneratorInterface/ExternalDecays/test,TEST))
ALL_SUBSYSTEMS+=Configuration
subdirs_src_Configuration = src_Configuration_GenProduction
ALL_PACKAGES += Configuration/GenProduction
subdirs_src_Configuration_GenProduction := src_Configuration_GenProduction_python
ifeq ($(strip $(PyConfigurationGenProduction)),)
PyConfigurationGenProduction := self/src/Configuration/GenProduction/python
src_Configuration_GenProduction_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/Configuration/GenProduction/python)
PyConfigurationGenProduction_files := $(patsubst src/Configuration/GenProduction/python/%,%,$(wildcard $(foreach dir,src/Configuration/GenProduction/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyConfigurationGenProduction_LOC_USE := self cmssw 
PyConfigurationGenProduction_PACKAGE := self/src/Configuration/GenProduction/python
ALL_PRODS += PyConfigurationGenProduction
PyConfigurationGenProduction_INIT_FUNC        += $$(eval $$(call PythonProduct,PyConfigurationGenProduction,src/Configuration/GenProduction/python,src_Configuration_GenProduction_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyConfigurationGenProduction,src/Configuration/GenProduction/python))
endif
ALL_COMMONRULES += src_Configuration_GenProduction_python
src_Configuration_GenProduction_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_Configuration_GenProduction_python,src/Configuration/GenProduction/python,PYTHON))
ALL_SUBSYSTEMS+=EvtGenInterface
subdirs_src_EvtGenInterface = src_EvtGenInterface_data
ALL_PACKAGES += EvtGenInterface/data
subdirs_src_EvtGenInterface_data := 
