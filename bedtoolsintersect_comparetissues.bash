#!/bin/sh

# Full bash script to first pull out the variants with my python tool, then filter against exons and the repeats.

# for i in {75..84}; do python get_sample_info.py -v ~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz -s 15-00258$i -q 90 -sp 'Exact' -to 'bed' >~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/UGPvariants_highGQ_15-00258$i.bed; done

# for i in {75..84};do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/UGPvariants_highGQ_15-00258$i.bed -b ~/Documents/CDH_WGS/io/hg19_col3_sorted_unique_exons.bed -wa | /Users/kardonlab/bedtools2/bin/bedtools intersect -a stdin -b ~/Documents/CDH_WGS/Data/sorted_repeats_hg19.bed -v | uniq >~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed; done


# This should run each of the other variant files in this family against the connective tissue sample. The -v option will make it so only connective tissue variants are kept.

#for j in {62..64}; for i in {60..64}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.uniq2$i.bed; done

for j in {75..84}; do for i in {75..84}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$j.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-00258$j.uniq2_$i.bed; done; done

for j in {75..84}; do for i in {75..84}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/Data/hg19_genes_commonnames.bed -b ~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-00258$j.uniq2_$i.bed | uniq >~/Documents/CDH_WGS/io/family_comparisons/genes_UGPvariants_highGQ_exonsonly_uniq_15-00258$j.uniq2_$i.bed; done; done

#for j in {72..74}; for i in {70..74}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.uniq2$i.bed; done

#for j in {77..79}; for i in {75..79}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.uniq2$i.bed; done

#for j in {82..84}; for i in {80..84}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-002586$j.uniq2$i.bed; done


# This will do the same thing for the patient blood sample.

#for i in {60..64}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-0025862.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-0025862_uniq2$i.bed; done

# This will do it with the skin sample.

#for i in {60..64}; do /Users/kardonlab/bedtools2/bin/bedtools intersect -a ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-0025863.bed -b ~/Documents/CDH_WGS/io/UGPvariants_highGQ_exonsonly_uniq_15-00258$i.bed -v >~/Documents/CDH_WGS/io/family_comparisons/UGPvariants_highGQ_exonsonly_uniq_15-0025863_uniq2$i.bed; done