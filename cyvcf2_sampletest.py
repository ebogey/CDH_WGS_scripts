"""Using cyvcf2 to extract just CDH_WGS UGP connective tissue patient variants"""

"""Connective tissue sample ids- 15-0025864, 15-0025869, 15-0025874, 15-0025879, 15-0025884"""

from cyvcf2 import VCF, Variant, Writer


samples = ['15-0025864', '15-0025869']

vcf= VCF("/Users/kardonlab/Documents/CDH_WGS/Data/VCFs/GATK_UGP/FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz", samples=samples)

for v in vcf:
        print(v.var_type, v.REF, v.ALT)
