import os
from pathlib import Path

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)+"/qc_data/"
Path(outdir).mkdir(parents=True, exist_ok=True)

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
    for j in files:
        fn1 = str(i)
        fn2 = str(j)
        if fn1 != fn2:
            if "R1" in fn1:
                if "R2" in fn2:
                    if fn1.split("_")[1] == fn2.split("_")[1]:
                        fn1 = i
                        fn2 = j
                        fastp_cmd = "fastp -w 16 -q 30 -i "+ \
                                    fn1.rstrip()+" -I "+fn2.rstrip()+ \
                                    " -o "+ outdir + str('_'.join(fn1.split("-")[:-2])).rstrip()+ \
                                    "_QC_R1.fq.gz "+ \
                                    " -O "+ outdir + str('_'.join(fn2.split("_")[:-2])).rstrip()+ \
                                    "_QC_R2.fq.gz "
                        print(fastp_cmd)
                        os.system(fastp_cmd)
                        os.rename("fastp.json",str('_'.join(fn1.split("_")[:-2]))+"_fastp.json")
                        os.rename("fastp.html",str('_'.join(fn2.split("_")[:-2]))+"_fastp.html")
