from cyvcf2 import VCF
from get_samplelist import get_samplst, get_all_vcfsamples
import csv
import argparse
import json

#Arguments for the command line when this script is run, adapted from Tom's de_novo.py script
p = argparse.ArgumentParser()
p.add_argument("-v","--vcf", help= "REQUIRED: Specify the path to the vcf file to pull variants from.", required = True)
p.add_argument("-s","--samples", help= "REQUIRED: Specify which samples you want to pull from vcf.", required = True)
p.add_argument("-sp","--specifier", help= "REQUIRED: Use 'Exact', 'Starts with', 'Ends with' or 'not' to tell how to use the input for --samples.", required = True)
p.add_argument("-t","--tissue", help= "OPTIONAL: Enter tissue type, pull variants found in these samples. Options: blood-maternal, blood-paternal, blood-proband, Skin, Diaphragm.", required = False)
p.add_argument("-f","--family", help= "OPTIONAL: Enter a 3 digit family ID, pull variants found in these samples.", required = False)
p.add_argument("-o","--out", help = "OPTIONAL: Name the output VCF.", required = False)

#Setting inputs as va
args = p.parse_args()
vcfarg = args.vcf
out = args.out
samp = args.samples
spec = args.specifier
tissue = args.tissue
family = args.family
print samp, spec, tissue, family

# csv iterator block adapted from stack overlow forum, http://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file, visited 7-14-16

sampledict = {} # Creates dictionary object that will contain the tissue type and family for each sample

reader = csv.reader(open('kardon_wfam.csv', 'r')) #Open csv file I made on 7-14-16, adapted from kardon.ped

#iterate through the opened csv file to start grabbing information from the columns, rows corresponding to each sample
for row in reader:
    sampledict[row[1]] = row[6], row[7]
sortsampdict = sorted(sampledict.keys())

#print sampledict #Print to check dictionary looks correct


# Code block to narrow sample list that will be passed to cyvcf2 based on whether a tissue type or family was specified on the command line
tempsamp = [] # Used to save the samples saved in this code block
if tissue != None:
    for k in sampledict:
        if sampledict[k][0] == tissue:
            tempsamp.append(k)
        else: continue
if family != None:
    for k in sampledict:
        if sampledict[k][1] == family:
            tempsamp.append(k)
        else: continue


samlist = get_samplst(get_all_vcfsamples(vcfarg), samp, spec) #Use functions from get_samplelist.py to start create the samplelist to be passed to cyvcf2
print samlist

finalsamplelist = []

if family or tissue != None:
    for i in tempsamp:
        if i in samlist:
            finalsamplelist.append(i)
        else: continue
else: finalsamplelist = samlist
print finalsamplelist

if len(finalsamplelist) == 0:
    print "ERROR: Looks like you are giving conflicting specifications. Please check the options given and/or that the sample you are looking for is in the vcf file you are using."
else:
    bigvcf = VCF(args.vcf, samples=finalsamplelist)

vcfinfo = []

print finalsamplelist

for v in bigvcf:
     print "chr"+v.CHROM, v.start, v.end, v.ID, v.REF, v.ALT, v.FILTER, v.QUAL, v.format('DP',int)


##outfile = open((out), "w")

##vcfdump = json.dumps(vcfinfo) # Converts the list made by v.samples() to a writable string

##outfile.write(vcfdump) # Write list created to fiLe

##outfile.close()


#for v in bigvcf:
#        print(v.CHROM, v.start, v.end, v.ID, v.REF, v.ALT, v.FILTER, v.QUAL, v.format('DP',int))
