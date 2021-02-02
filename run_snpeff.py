import os
from pathlib import Path

files = [f for f in os.listdir('.') if os.path.isfile(f)]
cwd = os.getcwd()
path = Path(cwd)

snpeff_path = "/opt/apps/snpEff/snpEff.jar"

for i in files:
    if i.endswith(".vcf"):
        fn = str('_'.join(i.split(".")[:-1])).rstrip()
        snpeff_cmd = f"java -Xmx8g -jar {snpeff_path} " + \
                     f"MN908947.3 "+i.rstrip() + \
                     f" > {fn}.ann.vcf"
        print(snpeff_cmd)
        os.system(snpeff_cmd)
        os.rename("snpEff_genes.txt",fn+"_snpeff_genes.txt")
        os.rename("snpEff_summary.html",fn+"_snpeff_summary.html")
