import sys
import os
import pathlib

ref = '/mnt/pathogen1/wanglab/ref/c_elegans/ce11.fa'
j8rde1 = "/mnt/pathogen1/wanglab/seq/2019j8rde1_aligned.bam"
rde1 = "/mnt/pathogen1/wanglab/seq/rde1_aligned.bam"
cwd = os.getcwd()
bsa_path = cwd+"/bsa/"
seq_path = cwd+"/seq/"
pathlib.Path(seq_path).mkdir(parents=True, exist_ok=True)
pathlib.Path(bsa_path).mkdir(parents=True, exist_ok=True)

def mimodd_se(r1):
    r1_name = r1.split("_")[0]
    r1_proc_name = r1_name+"_r1_proc.fq.gz"
    # QC
    fastp_SE_cmd = ("fastp -q 30 -i "+r1+" -o "+seq_path+r1_proc_name)
    os.system(fastp_SE_cmd)
    print(fastp_SE_cmd)
    sample = r1_name
    header_f = r1_name+"_header.sam"
    # generate header
    m_header = ("mimodd header --rg-id 000 --rg-sm "+sample+" --rg-ds '"+sample+\
                " data' -o "+seq_path+header_f)
    os.system(m_header)
    print(m_header)
    bam_f = r1_name+".bam"
    # convert fastq to bam
    m_se_convert = ("mimodd convert "+seq_path+r1_proc_name+\
                    " --iformat gz --oformat bam -h "+seq_path+header_f+" -o "+seq_path+bam_f)
    os.system(m_se_convert)
    print(m_se_convert)
    aligned_f = r1_name+"_aligned.bam"
    # align se seq to ce11 ref
    align_se = ("mimodd snap single "+ref+" "+seq_path+bam_f+" --iformat bam -o "+seq_path+aligned_f)
    #align_se = ("snap-aligner single /mnt/pathogen1/stahan/seq/ref/c_elegans/snap_index/ "+seq_path+bam_f+" -t 16 -m 80 -d 16 -h 2000 -o "+seq_path+aligned_f)
    os.system(align_se)
    print(align_se)  
    mutant = r1_name
    #sort_f = r1_name+"_aligned_sorted.bam"
    #sort_bam = ("samtools sort "+seq_path+aligned_f+" -o "+seq_path+sort_f)
    #os.system(sort_bam)
    # mkdir
    dir_name = bsa_path+mutant+"/"
    #os.mkdir(dir_name)
    pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)
    mutant = r1_name
    bcf_f = r1_name+"_variant_calls.bcf"
    # call variants
    varcall = ("mimodd varcall "+ref+" "+seq_path+aligned_f+" "+j8rde1+" "+rde1+" -o "+dir_name+bcf_f)
    os.system(varcall)
    print(varcall)
    bcf = bcf_f
    # extract variants
    extracted_f = r1_name+"_variants_extracted.vcf"
    varextract = ("mimodd varextract "+dir_name+bcf_f+" -o "+dir_name+extracted_f)
    os.system(varextract)
    print(varextract)
    vcf = extracted_f
    candidate_f = r1_name+"_candidate_variants_dp0.vcf"
    # subtract 2019 j8rde1 vars
    subtract = ("mimodd vcf-filter "+dir_name+extracted_f+" -s "+r1_name+\
                " 2019j8rde1 --dp 0 0 --gt 1/1 0/0 -o "+dir_name+candidate_f)
    os.system(subtract)
    print(subtract)
    candidates = candidate_f
    anno_vars = r1_name+"_candidate_variants_anno_dp10.vcf"
    # annotate variants with snpeff
    snpeff = ("mimodd annotate "+dir_name+candidate_f+" WBcel235.86 -o "+dir_name+anno_vars)
    os.system(snpeff)
    print(snpeff)
    snpeff = anno_vars
    # generate html variant file
    html_f = r1_name+"_candidate_variants_anno_report_dp0.html"
    vars_to_html = ("mimodd varreport "+dir_name+anno_vars+" -o "+dir_name+html_f+" -f html")
    os.system(vars_to_html)
    print(vars_to_html)
    pdf_f = r1_name+"_variants_linkage_map.pdf"
    # generate linkage map
    map_linkage = "mimodd map VAF "+dir_name+extracted_f+" -m "+r1_name+\
                " -u rde1 -r 2019j8rde1 -p "+dir_name+pdf_f
    os.system(map_linkage)
    print(map_linkage)
    
def mimodd_pe(r1,r2):
    r1_name = str(r1.split("_")[0])
    r2_name = str(r2.split("_")[0])
    r1_proc_name = r1_name+"_r1_proc.fq.gz"
    r2_proc_name = r2_name+"_r2_proc.fq.gz"
    fastp_PE_cmd = ("fastp -q 30 -i "+r1+" -I "+r2+" -o "+seq_path+r1_proc_name+\
                    " -O "+seq_path+r2_proc_name)
    os.system(fastp_PE_cmd)
    print(fastp_PE_cmd)
    sample = r1_name
    header_f = r1_name+"_header.sam"
    m_header = ("mimodd header --rg-id 000 --rg-sm "+sample+" --rg-ds '"+sample+\
                " data' -o "+seq_path+header_f)
    os.system(m_header)
    print(m_header)
    bam_f = r1_name+".bam"
    m_pe_convert = ("mimodd convert "+seq_path+r1_proc_name+" "+seq_path+r2_proc_name+\
                    " --iformat gz_pe --oformat bam -h "+seq_path+header_f+" -o "+seq_path+bam_f)
    os.system(m_pe_convert)
    print(m_pe_convert)    
    aligned_f = r1_name+"_aligned.bam"
    align_pe = ("mimodd snap paired "+ref+" "+seq_path+bam_f+" --iformat bam -t 16 -m 80 -d 16 -h 2000 -o "+seq_path+aligned_f)
    #align_pe = ("snap-aligner paired /mnt/pathogen1/stahan/seq/ref/c_elegans/snap_index/ "+seq_path+bam_f+" -o "+seq_path+aligned_f)
    os.system(align_pe)
    print(align_pe)
    mutant = r1_name
    dir_name = bsa_path+mutant+"/"
    #os.mkdir(dir_name)
    pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)
    mutant = r1_name
    bcf_f = r1_name+"_variant_calls.bcf"
    #sort_f = r1_name+"_aligned_sorted.bam"
    #sort_bam = ("samtools sort "+seq_path+aligned_f+" -o "+seq_path+sort_f)
    #os.system(sort_bam)
    varcall = ("mimodd varcall "+ref+" "+seq_path+aligned_f+" "+j8rde1+" "+rde1+" -o "+dir_name+bcf_f)
    os.system(varcall)
    print(varcall)
    bcf = bcf_f
    extracted_f = r1_name+"_variants_extracted.vcf"
    varextract = ("mimodd varextract "+dir_name+bcf_f+" -o "+dir_name+extracted_f)
    os.system(varextract)
    print(varextract)    
    vcf = extracted_f
    candidate_f = r1_name+"_candidate_variants_dp10.vcf"
    subtract = ("mimodd vcf-filter "+dir_name+extracted_f+" -s "+r1_name+\
                " 2019j8rde1 --dp 0 0 --gt 1/1 0/0 -o "+dir_name+candidate_f)
    os.system(subtract)
    print(subtract)
    candidates = candidate_f
    anno_vars = r1_name+"_candidate_variants_anno_dp0.vcf"
    snpeff = ("mimodd annotate "+dir_name+candidate_f+" WBcel235.86 -o "+dir_name+anno_vars)
    os.system(snpeff)
    print(snpeff)
    snpeff = anno_vars
    html_f = r1_name+"_candidate_variants_anno_report_dp0.html"
    vars_to_html = ("mimodd varreport "+dir_name+anno_vars+" -o "+dir_name+html_f+" -f html")
    os.system(vars_to_html)
    print(vars_to_html)
    pdf_f = r1_name+"_variants_linkage_map.pdf"
    # generate linkage map
    map_linkage = "mimodd map VAF "+dir_name+extracted_f+" -m "+r1_name+\
                " -u rde1 -r 2019j8rde1 -p "+dir_name+pdf_f
    os.system(map_linkage)
    print(map_linkage)
        

def main():
    arg_list = []
    arguments = sys.argv[1:]
    
    if (len(arguments) == 1):
        for arg in arguments:
            arg_list.append(arg)
        mimodd_se(arg_list[0])
    elif (len(arguments) == 2):
        for arg in arguments:
            arg_list.append(arg)
        mimodd_pe(arg_list[0],arg_list[1])
 
if __name__ == '__main__':
    main()
