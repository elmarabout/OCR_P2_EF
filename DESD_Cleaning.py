import pandas as pd


DESC = pd.read_csv("data/DESC2.csv")
DESD = pd.read_csv("data/DESD2.csv")
DESFN = pd.read_csv('data/DESFN2.csv')
DESCS = pd.read_csv('data/DESCS2.csv')

def melt_it(df, id_vars, var_name, var_value):
    return df.melt(
        id_vars=[id_vars],
        value_vars=['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978',
                    '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                    '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996',
                    '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
                    '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
                    '2015', '2016', '2017', '2020', '2025', '2030', '2035', '2040', '2045',
                    '2050', '2055', '2060', '2065', '2070', '2075', '2080', '2085', '2090',
                    '2095', '2100'], var_name=var_name, value_name=var_value)



DESD_merge = pd.merge(DESD, DESC[['Country Code', 'Region']], how='left',
                  left_on='Country Code', right_on='Country Code')

print("before :", DESD_merge.shape)

without_region = (DESD_merge['Country Name'][DESD_merge['Region'].isnull()].unique().tolist())
print(without_region)


for elt in without_region:
    DESD_merge.drop(DESD_merge[DESD_merge['Country Name'] == str(elt)].index, inplace=True)

print("after :", DESD_merge.shape)
