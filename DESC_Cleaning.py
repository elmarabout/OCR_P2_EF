import pandas as pd

from AnaExplo import export_dfcleaned

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()


DESC = pd.read_csv("data/DESC2.csv")
DESD = pd.read_csv("data/DESD2.csv")
DESFN = pd.read_csv('data/DESFN2.csv')
DESCS = pd.read_csv('data/DESCS2.csv')

# print(DESC.columns)
# Index(['Unnamed: 0', 'Country Code', 'Short Name', 'Country Name', 'Long Name',
#        '2-alpha code', 'Currency Unit', 'Special Notes', 'Region',
#        'Income Group', 'WB-2 code', 'National accounts base year',
#        'National accounts reference year', 'SNA price valuation',
#        'Lending category', 'Other groups', 'System of National Accounts',
#        'Alternative conversion factor', 'PPP survey year',
#        'Balance of Payments Manual in use', 'External debt Reporting status',
#        'System of trade', 'Government Accounting concept',
#        'IMF data dissemination standard', 'Latest population census',
#        'Latest household survey',
#        'Source of most recent Income and expenditure data',
#        'Vital registration complete', 'Latest agricultural census',
#        'Latest industrial data', 'Latest trade data',
#        'Latest water withdrawal data'],
#       dtype='object')

region_count = DESC['Region'].value_counts()

DESC_na = DESC[DESC.isna().any(axis=1)]
DESC_wna = (DESC_na[DESC_na['Region'].isna()])

DESC.drop(index=DESC_wna.index, inplace=True)

