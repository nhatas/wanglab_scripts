import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
    if i.endswith("bam"):
        fn = str('_'.join(i.split(".")[:-1])).rstrip()
        sort_mapped = "samtools sort -@ 8 "+i.rstrip()+" -o "\
        +fn+"_sorted.bam"
        print(sort_mapped)
        os.system(sort_mapped)
