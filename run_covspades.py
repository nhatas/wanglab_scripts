import os
from pathlib import Path

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)+"/assembly/"
Path(outdir).mkdir(parents=True, exist_ok=True)

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for i in files:
	for j in files:
		fn1 = str(i)
		fn2 = str(j)
		if fn1 != fn2:
			if i.split("_")[1] == j.split("_")[1]:
				if "R1" in fn1:
					if "R2" in fn2:
						spades_cmd = "/opt/apps/SPAdes-3.15.0-"+ \
						"corona-2020-07-06/coronaspades.py -1 "+ \
						fn1+" -2 "+fn2+ \
						" -o "+outdir+'covspades_assembly_'+'_'.join(i.split(".")[:-1])
						print(spades_cmd)
						os.system(spades_cmd)
