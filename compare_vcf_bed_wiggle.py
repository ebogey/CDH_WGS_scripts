import argparse
import csv

parser = argparse.ArgumentParser(description='Find shared positions in a given vcf and bed file, allowing for +/- x bp start site.')
parser.add_argument('file1', metavar='F1', help='First file to compare.')
parser.add_argument('file2', metavar='F2', help='Second file to compare.')
parser.add_argument('basepairs', metavar='N', help='Number of basepairs + or - to include when comparing start sites.')

args = parser.parse_args()
firstfile = args.file1
secondfile = args.file2
basepairN = int(args.basepairs)

if firstfile.endswith(".vcf") == True:
    vcfile = firstfile
elif firstfile.endswith(".bed") == True:
    bedfile = firstfile
else: print("File 1 is not a vcf or bed file.")

if secondfile.endswith(".vcf") == True:
    vcfile = secondfile
elif secondfile.endswith(".bed") == True:
    bedfile = secondfile
else: print("File 2 is not a vcf or bed file.")


VCFreader = csv.reader(open(vcfile, 'r'), delimiter='\t')
BEDreader = csv.reader(open(bedfile, 'r'), delimiter='\t')

VCFposlist = []
BEDposlist = []

for row in VCFreader:
    VCFposlist.append(int(row[1]))
for row in BEDreader:
    BEDposlist.append(int(row[1]))

fullmatchlist = [i for i in VCFposlist if i in BEDposlist]

BEDposlistplus1 = [x+1 for x in BEDposlist]
BEDposlistneg1 = [x-1 for x in BEDposlist]
BEDposlistplus2 = [x+2 for x in BEDposlist]
BEDposlistneg2 = [x-2 for x in BEDposlist]
BEDposlistplus3 = [x+3 for x in BEDposlist]
BEDposlistneg3 = [x-3 for x in BEDposlist]

posplus1 = [i for i in VCFposlist if i in BEDposlistplus1]
posneg1 = [i for i in VCFposlist if i in BEDposlistneg1]
posplus2 = [i for i in VCFposlist if i in BEDposlistplus2]
posneg2 = [i for i in VCFposlist if i in BEDposlistneg2]
posplus3 = [i for i in VCFposlist if i in BEDposlistplus3]
posneg3 = [i for i in VCFposlist if i in BEDposlistneg3]

VCFreader = csv.reader(open(vcfile, 'r'), delimiter='\t')
BEDreader = csv.reader(open(bedfile, 'r'), delimiter='\t')

for row in VCFreader:
    for l in fullmatchlist:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posplus1:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posplus2:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posplus3:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posneg1:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posneg2:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
for row in VCFreader:
    for l in posneg3:
        if int(row[1]) == int(l):
            print(str(row).strip('[').strip(']').replace("'",'').replace(', ','\t'))
        else: continue
