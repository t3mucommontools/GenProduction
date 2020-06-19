#!/usr/bin/env python

import os
import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input-file",help="Name of the gen fragment  file stored in pythia dir; [Default: %(default)s] ", action="store", default = 'dat_as_cfi.py')
    parser.add_argument("-ne", "--ne",help="Units per job; [Default: %(default)s] ", action="store", default = 10000)
    parser.add_argument("-nj", "--nj",help="NJOBS; [Default: %(default)s] ", action="store", default = 20)
    parser.add_argument("-tag", "--tag",help="Put the date tag for a conveniente navigation; [Default: %(default)s] ",  type=str, action="store", default = "10_03_2020")
    args = parser.parse_args()

    datasetsFile = 'python/'+args.input_file
    if not os.path.isfile(datasetsFile):
        print "File %s not found!!!" % datasetsFile
        sys.exit()

    jobprefix = args.input_file.split("_")[0]+"_"+args.input_file.split("_")[1]
    config = jobprefix+"_GEN.py"
    with open('gen_config.py', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace('<gencard>', args.input_file[:-3]) # chomp .py at the end
            filedata = filedata.replace('<outputfile>', jobprefix+"_EvtGen_GEN_2018.root")

            with open(config, 'w') as file:
                file.write(filedata)

    crabconf=open("crab_cfg_"+jobprefix+".py","w")
    crabconf.write ("from WMCore.Configuration import Configuration  \n")
    crabconf.write ("config = Configuration()  \n\n")
    crabconf.write ("config.section_(\"General\")  \n")
    crabconf.write ("config.General.requestName = '"+jobprefix+"_" +args.tag+ "'\n")
    crabconf.write ("config.General.workArea =  'crab_area' \n")
    crabconf.write ("config.General.transferLogs = True \n\n")
    crabconf.write ("config.section_(\"JobType\") \n")
    crabconf.write ("config.JobType.allowUndistributedCMSSW = True \n")
    crabconf.write ("config.JobType.pluginName = 'PRIVATEMC' \n")
    crabconf.write ("config.JobType.psetName = '%s'  \n"  % config)
    crabconf.write ("config.JobType.eventsPerLumi = 30000 \n")
    crabconf.write ("config.JobType.allowUndistributedCMSSW = True \n")
    crabconf.write ("config.JobType.numCores = 2 \n\n")
    crabconf.write ("config.section_(\"Data\")  \n\n")
    crabconf.write ("config.Data.outputPrimaryDataset = '%s' \n" % (jobprefix+"_GEN_"+args.tag) )
    crabconf.write ("config.Data.splitting = 'EventBased' \n")
    crabconf.write ("config.Data.unitsPerJob = %s \n" % args.ne)
    crabconf.write ("NJOBS = %s \n" % args.nj)
    crabconf.write ("config.Data.totalUnits = config.Data.unitsPerJob * NJOBS \n")
    crabconf.write ("config.Data.inputDBS = 'phys03' \n")
    crabconf.write ("config.Data.outLFNDirBase = '/store/user/cherepan/' \n")
    crabconf.write ("config.Data.outputDatasetTag = '%s' \n" % (jobprefix +"_"+args.tag ))
    crabconf.write ("config.Data.publication = True \n\n")
    crabconf.write ("config.section_(\"Site\") \n")
    crabconf.write ("config.Site.storageSite = 'T2_US_Florida' \n")
    crabconf.write ("dont_check_proxy =  1 \n")



    print "Crab and gen fragment configured: "
    print "crab_cfg_"+jobprefix+".py"
    print config
