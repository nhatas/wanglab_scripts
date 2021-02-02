import os
from pathlib import Path


cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)+"/deepvariant_out/"
Path(outdir).mkdir(parents=True, exist_ok=True)

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
    if i.endswith("bam"):
        fn = str('_'.join(i.split(".")[:-1])).rstrip()
        dv = f"docker run -v '{path}':'/input' "+ \
            f"-v '{outdir}':'/output' "+ \
            f"google/deepvariant:'1.1.0' /opt/deepvariant/bin/run_deepvariant "+ \
            f"--model_type=WGS "+ \
            f"--ref=/input/nCoV-2019.reference.fasta "+ \
            f'--call_variants_extra_args="use_openvino=true" ' + \
            f"--reads=/input/{i.rstrip()} "+ \
            f"--output_vcf=/output/{fn}.vcf "+ \
            f"--output_gvcf=/output/{fn}.gvcf --num_shards=16"
        print(dv)
        os.system(dv)
