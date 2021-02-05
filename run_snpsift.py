import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

snpsift_path = "/opt/apps/snpEff/SnpSift.jar"

#fields = 'POS REF ALT "ANN[0].EFFECT" "ANN[0].GENE" "GEN[0].AD" "GEN[0].VAF" "ANN[0].HGVS_P"' # DeepVariant output
fields = 'POS REF ALT AF "ANN[0].EFFECT" "ANN[0].GENE" "ANN[0].HGVS_P"' # LoFreq output

for i in files:
    if i.endswith(".ann.vcf"):
        fn = str('_'.join(i.split(".")[:-1])).rstrip()
        snpsift_cmd = f'java -jar {snpsift_path} extractFields ' + \
                     i.rstrip() + \
                     f" {fields} " + \
                     f" > {fn}.snpsift.txt"
        print(snpsift_cmd)
        os.system(snpsift_cmd)
