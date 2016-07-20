7-18-16
Made a bash script to pull variants for each sample. Took approximately 24 hours to run for all 25 samples. 

$for i in {60..84}; do python get_sample_info.py -v ~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz -s 15-00258$i -sp 'Exact' >test_stdout_singletest_15-00258$i.txt; done

However, should have named the output files ...bed not ...txt to make passing to bedtools intersect easier. I also have the positional output a single numerical value (i.e. 1, 2, etc) and should be chr1, chr2. Add to the get_sample_info.py script to fix this. 

7-19-16

Decided to force quit the bash script started yesterday. Looks like it stopped on sample ..84. Deleted the old files, reran with only first family (..60 to ..64), changed file output names and location.

$for i in {60..64}; do python get_sample_info.py -v ~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz -s 15-00258$i -sp 'Exact' >~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/UGPvars_15-00258$i.bed; done

7-20-16
Above line finished, output files looked good. I did want to make sure each file was unique and not reporting the same variants. Tried to use bedtools intersect to determine how much overlap in variant positions there were. Popped up a read in error, Thought it was due to the first 6 lines in the UGPvars..bed files having print statements about the options used, tried to use sed to remove these lines and accidently replaced the old files with empty files (rookie mistake). I also tried to use the hg19 exons bedfile, downloaded from the UCSC genome browser site on 7-19-16 (exons_hg19_bedfile.bed.gz), to intersect against one of our samples to see if I could just keep exon variants. This gave me an error about ranges in chrUn, used awk to remove these:

$awk '!/chrUn/' ~/Documents/CDH_WGS/Data/exons_hg19_bedfile.bed > ~/Documents/CDH_WGS/Data/exons_hg19_nochrun.bed

Appears to have worked fine (used head to see if other chromosomes still there (yes) and grepped for chrUn (nothing)). So now I am going to update get_sample_info.py to output bedtool friendly files and rerun for the first family.

I am also running samtools depth to start seeing if there are any anomalies in read coverage in the large chromosomal regions associated with CDh, as a first probe into whether our patients have these (LUMPY will be run to really get at this). I created a bash script using the -r option of samtools depth to look at the specific chromosomal ranges. From the output nothing really jumps out..

Updated get_sample_info.py ran with similar command line input as before:

$for i in {60..64}; do python get_sample_info.py -v ~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/FQF_Pipeline.GVCF.1.0.0_Final_Backgrounds_Longevity.vcf.gz -s 15-00258$i -sp 'Exact' -to bed >~/Documents/CDH_WGS/Data/VCFs/GATK_UGP/UGPvariants_15-00258$i.bed; done