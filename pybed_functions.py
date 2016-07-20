from pybedtools import BedTool

###Building functions from pybedtools (bedtools for python) to first filter sample variant files retrieved from FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz using my get_sample_info.py tool.###

def intersector(sampfile, filtfile, specfr):
    ###Takes two bed files and will intersect them. The specfr argument is used to tell whether to keep or remove the regions that overlap in the two files given.###

    sf = BedTool(sampfile)
    ff = BedTool(filtfile)

    if specfr == 'Keep':
        endfile = sf.intersect(ff, u=True)
    elif specfr == 'Discard':
        endfile = sf.intersect(ff, u=False)
    else: print "ERROR: Incorrect specifying argument given, please use 'Keep' or 'Discard'."

    return endfile
