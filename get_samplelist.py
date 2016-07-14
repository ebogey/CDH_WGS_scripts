from cyvcf2 import VCF
import os.path
import sys
import os
import json



##Using lines from Tom's de_novo scripts on Github, cloned 7-12-16

def get_all_vcfsamples(vcfile):
    ###This will give a full list of the samples in the given vcf file###
    VCF_PATH = os.path.join("~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/", vcfile)

    #vcfile = input("Path and name of vcf file to get samples from. Must be typed correctly. /n") # Makes you type in the name of the vcf file you are grabbing sample names from, should change at some point to make more robust

    v = VCF(VCF_PATH) # Read in as vcf to cyvcf2

    samples = v.samples() # Cyvcf2 attribute pulls out sample names and creates a list

    outfile = open((vcfile + "_" + "samples.txt"), "w") # Print and write the list as a text file to be used for other stuff
    outfile.write(samples)
    return samples


def get_samplelist(samplelist):
    ###This will allow you to create a narrowed list of samples that can then be passed to cyvcf2 functions###

    samplst = []

    sampquery = input("What sample(s) do you want? ")

    modifquery = input("Please specify 'Exact', 'Starts with', 'Ends with' or 'not' to pull samples ")

    if modifquery == 'Exact':
        for i in samplelist:
            if i == sampquery:
                samplst.append()
            else: continue
    if modifquery == 'Starts with':
        for i  in samplelist:
            i = str(i)
            if i.startswith(sampquery) == True:
                samplst.append()
            else: continue
    if modifquery == 'Ends with':
        for i in samplist:
            i = str(i)
            if i.endswith(sampquery) == True:
                samplst.append()
            else: continue
    if modifquery == 'not':
        for i in samplelist:
            if i != sampquery:
                samplst.append()
    else: print "Incorrect modifier given."

    if len(samplst) == 0:
        print "Looks like that sample is not in the list given."
    else:
        outfile = open((sampquery + "_" + modifquery + "_" + "list.txt"), "w")
        return samplst
