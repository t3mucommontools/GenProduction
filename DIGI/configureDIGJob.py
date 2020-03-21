#!/usr/bin/env python

import os
import sys
import argparse
#/DMuNuEta_MuMuGammaPi0_GEN_11_03_2020/cherepan-DMuNuEta_MuMuGammaPi0-8dd0aec734ac5b9a5b01503b49b30d66/USER

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--input-sample",help="Path to the GEN sample; [Default: %(default)s] ", type = str, action="store", default = 'dat_as_cfi.py')
    parser.add_argument("-nu", "--nu",help="Units per job; [Default: %(default)s] ", action="store", default = 20)
    parser.add_argument("-tag", "--tag",help="Put the date tag for a conveniente navigation; [Default: %(default)s] ",  type=str, action="store", default = "10_03_2020")
    args = parser.parse_args()

    sample = args.input_sample

    print args.input_sample

    jobprefix = args.input_sample.split("/")[1]
    config = jobprefix+"_DIGI.py"
    with open('digi_config.py', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace('<output_name>', args.input_sample.split("/")[1]+"_DIGI.root") # chomp .py at the end

            with open(config, 'w') as file:
                file.write(filedata)

    crabconf=open("crab_cfg_"+jobprefix+".py","w")
    crabconf.write ("from WMCore.Configuration import Configuration  \n")
    crabconf.write ("config = Configuration()  \n\n")
    crabconf.write ("config.section_(\"General\")  \n")
    crabconf.write ("config.General.requestName = '"+jobprefix+"_" +args.tag+"'\n")
    crabconf.write ("config.General.workArea =  'crab_area' \n")
    crabconf.write ("config.General.transferLogs = True \n\n")
    crabconf.write ("config.section_(\"JobType\") \n")
    crabconf.write ("config.JobType.allowUndistributedCMSSW = True \n")
    crabconf.write ("config.JobType.pluginName = 'Analysis' \n")
    crabconf.write ("config.JobType.psetName = '%s'  \n"  % config)
    crabconf.write ("config.JobType.maxMemoryMB = 5000 \n")
    crabconf.write ("config.JobType.numCores = 4 \n")
    crabconf.write ("config.section_(\"Data\")  \n\n")
    crabconf.write ("config.Data.inputDataset = '%s' \n" % (sample) )
    crabconf.write ("config.Data.splitting = 'FileBased' \n")
    crabconf.write ("config.Data.unitsPerJob = %s \n" % args.nu)
    crabconf.write ("config.Data.totalUnits = -1 \n")
    crabconf.write ("config.Data.inputDBS = 'phys03' \n")
    crabconf.write ("config.Data.outLFNDirBase = '/store/user/cherepan/' \n")
    crabconf.write ("config.Data.outputDatasetTag = '%s' \n" % (jobprefix+'_DIGI'+args.tag))
    crabconf.write ("config.Data.publication = True \n\n")
    crabconf.write ("config.section_(\"Site\") \n")
    crabconf.write ("config.Site.storageSite = 'T2_US_Florida' \n")
    crabconf.write ("dont_check_proxy =  1 \n")



    print "Crab and gen fragment configured "

