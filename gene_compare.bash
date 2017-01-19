#!/bin/sh

for j in {60..84}; do for i in {60..84}; do awk '{print $4}' ~/Documents/CDH_WGS/io/family_comparisons/genes_UGPvariants_highGQ_exonsonly_uniq_15-00258$j.uniq2_$i.bed >~/Documents/CDH_WGS/io/family_comparisons/$j.uniq2_$i.justgenes.txt; done; done # Pull final column with gene names from the comparison files

for j in {60..84}; do for i in {60..84}; do grep -Fxf ~/Documents/CDH_WGS/io/family_comparisons/$j.uniq2_$i.justgenes.txt ~/Documents/CDH_WGS/CDH_WGS_scripts/CDH_genes.txt >~/Documents/CDH_WGS/io/family_comparisons/$j.uniq2_$i.just_CDH_genes.txt; done; done #Compares the previously created files to the CDH associated genes, keep just the ones that overlap in the two files