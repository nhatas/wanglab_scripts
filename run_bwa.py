import os
from pathlib import Path

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)+"/alignment_data/"
Path(outdir).mkdir(parents=True, exist_ok=True)

ref = "/mnt/pathogen1/josh/ref/nCoV-2019.reference.fasta"
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
    for j in files:
        fn1 = str(i)
        fn2 = str(j)
        if fn1 != fn2:
            if "R1" in fn1:
                if "R2" in fn2:
                    if fn1.split("_")[1] == fn2.split("_")[1]:
                        R1 = str(''.join(fn1)).rstrip()
                        R2 = str(''.join(fn2)).rstrip()
                        fn = str('_'.join(fn1.split("_")[:-2]))
                        bwa_cmd = f"bwa mem -t 8 {ref} {str(R1)} {str(R2)} " + \
                                        f"| samtools sort -@ 8 -o {str(fn.rstrip())}.bam -"
                        print(bwa_cmd)
                        os.system(bwa_cmd)
