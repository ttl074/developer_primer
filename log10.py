
import pandas as pd
import numpy as np
import sys
if len(sys.argv) != 2:
    print('Needs input gct')
    exit(0)
vcf = sys.argv[1]
df = pd.read_table(vcf,sep='\t',skiprows=2)
rows = df.columns[2::]
for r in rows:
    df[r] = np.log(df[r])
df.to_csv('log.gct',sep='\t')


