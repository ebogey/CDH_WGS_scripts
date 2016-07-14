from cyvcf2 import VCF
from get_samplelist import get_samplst, get_all_vcfsamples
import csv
import argparse

#Arguments for the command line when this script is run, adapted from Tom's de_novo.py script
p = argparse.ArgumentParser()
p.add_argument("--vcf", help= "REQUIRED: Specify the path to the vcf file to pull variants from.", required = True)
p.add_argument("--tissue", help= "OPTIONAL: Enter tissue type, pull variants found in these samples.", required = False)
p.add_argument("--family", help= "OPTIONAL: Enter a 3 digit family ID, pull variants found in these samples.", required = False)
p.add_argument("--out", help = "OPTIONAL: Name the output VCF.", required = False)
args = p.parse_args()

out = args.out

# csv iterator block adapted from stack overlow forum, http://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file, visited 7-14-16

sampledict = {} # Creates dictionary object that will contain the tissue type and family for each sample

reader = csv.reader(open('kardon_wfam.csv', 'r')) #Open csv file I made on 7-14-16, adapted from kardon.ped

#iterate through the opened csv file to start grabbing information from the columns, rows corresponding to each sample
for row in reader:
    sampledict[row[1]] = row[5], row[6]

print sampledict #Print to check dictionary looks correct

samlist = get_samplst(get_all_vcfsamples(args.vcf)) #Use functions from get_samplelist.py to start create the samplelist to be passed to cyvcf2

bigvcf = VCF(args.vcf, samples=samlist)