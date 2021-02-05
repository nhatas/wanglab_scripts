#!conda install -c anaconda openpyxl -y

import os
import pandas as pd
from pathlib import Path
import openpyxl as pxl

cwd = os.getcwd()
path = Path(cwd)
files = [f for f in os.listdir(path) if os.path.isfile(f)]
filename = 'snpsift_output.xlsx' # change as needed

wb = pxl.Workbook()
wb.save(filename)
wb.close()
excel_book = pxl.load_workbook(filename)

for i in files:
    if i.endswith("snpsift.txt"):
        fn = '_'.join(i.split("_")[:-2])
        print(fn)
        df = pd.read_csv(i, sep='\t')
        df.columns = ['POS', 'REF','ALT', 'EFFECT', 'GENE', 'VAF', 'PROTEIN']
        df = df[df.VAF >= 0.5] # change to minimum variant allele frequency you wish to keep
        data = {'filename': fn} 
        df = df.append(data, ignore_index=True)
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            writer.book = excel_book
            writer.sheets = {worksheet.title: worksheet for worksheet in excel_book.worksheets}
            df.to_excel(writer, fn, index=False)
            writer.save()
