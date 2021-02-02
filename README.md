# wanglab_scripts

## run_fastp.py
### QC sequencing data with fastp. Run script in the same directory as the sequencing files you want to QC. Modify the following code `-w 16 -q 30` to indicate the number of threads you want to use (set to 16) and the quality score cutoff (30). Output located in a parent directory `/qc_data/`.

## run_bbmap.py
### Align sequencing data (usually QC'd first) to a reference genome (set to SARS-CoV-2 Wuhan reference) using BBMap. Run script in the same directory as the QC'd sequencing files. Set `ref` to the reference genome you wish to align to. Currently the script is set to output mapped reads using the `outm` BBMap parameter. To output both mapped and unmapped reads, change `outm` to `out`. Output located in a parent directory `/alignment_data/`.

## sort_bams.py
### Sort bam files with samtools. Run the script in the same directory as the BAM files you want to sort. Filenames will have extensions removed and `_sorted.bam` appended in the same directory as the script. 

## bam_to_fastq.py
### Coverts BAM files in the same directory as the script ending in `_sorted.bam` to R1 and R2 FASTQ files using bedtools. Output located in a parent directory `/mapped_fastq/`.

## run_covspades.py
### De-novo assembly of FASTQ files using the CoronaSPAdes assembler. To use the default SPAdes assembler, change `coronaspades.py` to `spades.py` in the script. Output assembly folders located in parent directory `/assembly/`.

## run_deepvariant.py
### Variant calling using Google's DeepVariant Docker container. Requires BAM files and their indexes to be in the same directory as the scripts. Also requires the reference genome, `nCoV-2019.reference.fasta`, and its index, to be in the same folder as the script. Output located in a parent directory `/deepvariant_out/`.

## run_snpeff.py
### Annotates VCF files generated with files aligned to `nCoV-2019.reference.fasta`. Required to be in the same folder as the VCF files. Output annotated VCF files will have `.ann.vcf` appended to the filename. 

## run_snpsift.py
### Requires SNPEff annotated VCF files. Modify the `fields` variable to designate the fields you wish to extract from the annotated VCF files. Parsed annotated VCF files will have `.snpsift.txt` appended to them. 
