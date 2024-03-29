cmsDriver.py Configuration/GenProduction/python/ZTau3Mu.py 		\
	--fileout file:ZTau3Mu_BPH-RunIISummer19UL17GEN-evtgen.root	\
	--mc 																												\
	--eventcontent RAWSIM 																			\
	--datatier GEN 																							\
	--conditions 106X_mc2017_realistic_v6  											\
	--beamspot Realistic25ns13TeVEarly2017Collision 						\
	--step GEN 																									\
	--geometry DB:Extended 																			\
	--era Run2_2018																							\
	--nThreads 4																								\
	--python ZTau3Mu_GEN.py 																		\
	--no_exec \
	-n 100
