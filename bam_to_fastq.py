import os
from pathlib import Path

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)+"/mapped_fastq/"
Path(outdir).mkdir(parents=True, exist_ok=True)

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
        if i.endswith("_sorted.bam"):
                fn = str('_'.join(i.split(".")[:-1]))
                bam_fastq = "bedtools bamtofastq -i "+i.rstrip()+" -fq "+outdir+fn+"_R1.fq -fq2 "+outdir+fn+"_R2.fq"
                print(bam_fastq)
                os.system(bam_fastq)
