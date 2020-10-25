import pandas as pd

from AnaExplo import export_dfcleaned

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()

#print(len(set(DESFN['CountryCode'])))

## 239 country code sur DESCFN

def diff(a,b):
    return list(list(set(a)-set(b))+ list(set(b) - set(a)))

a_desc = set(list(DESC['Country Code'].unique()))
b_desfn = set(list(DESFN['CountryCode'].unique()))

#CountryCode_diff = a_desc - b_desfn
#print(CountryCode_diff)
# {'GRL', 'MAF', 'SXM'}

### colonne Year

if DESFN['Year'].str.contains('YR').any():
    DESFN['Year'] = DESFN['Year'].apply(lambda x: x[2:])

