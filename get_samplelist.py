from cyvcf2 import VCF

##Using lines from Tom's de_novo scripts on Github, cloned 7-12-16

def get_all_vcfsamples(vcfpath):
    #vcfile = input("Path and name of vcf file to get samples from. Must be typed correctly. /n") # Makes you type in the name of the vcf file you are grabbing sample names from, should change at some point to make more robust
    
    v = VCF(vcf) # Read in as vcf to cyvcf2

    samples = v.samples() # Cyvcf2 attribute pulls out sample names and creates a list

    outfile = open((vcfile + "samples.txt"), "w") # Print and write the list as a text file to be used for other stuff
    
    return samples
