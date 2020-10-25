import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.offline as pyo
import plotly.graph_objs as go

from AnaExplo import export_dfcleaned
from AnaExplo import rename_coldf,drop_doppledanger

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()

rename_coldf(DESFN,'CountryCode','Country Code')
rename_coldf(DESFN,'SeriesCode','Indicator Code')
rename_coldf(DESFN,'DESCRIPTION','Desc Data')

#print(len(set(DESFN['CountryCode'])))

## 239 country code sur DESCFN

def diff(a,b):
    return list(list(set(a)-set(b))+ list(set(b) - set(a)))

a_desc = set(list(DESC['Country Code'].unique()))
b_desfn = set(list(DESFN['Country Code'].unique()))

# CountryCode_diff = a_desc - b_desfn
# print(CountryCode_diff)
# {'GRL', 'MAF', 'SXM'}

print(DESFN['Year'])
### colonne Year

if DESFN['Year'].str.contains('YR').any():
    DESFN['Year'] = DESFN['Year'].apply(lambda x: x[2:])

print("après filtrage",DESFN['Year'])

drop_doppledanger(DESD, DESFN, 'Country Code')

### Matplotlib / Seaborn Version
sns.set()
plt.title("Nombre de données par Année")
df_treated = DESFN.groupby('Year').count().reset_index()
graph = sns.barplot(x ="Year", y = 'Country Code', data=df_treated)
graph.set_xticklabels(labels=df_treated['Year'], rotation=45, size=12)
plt.ylabel('Data Numbers')
plt.savefig("graph//"+"DESFNcount.png")
plt.show

# print(df_treated)
# print(df_treated.columns)

#Plotly Version
data_toplot = [go.Bar(
    x=df_treated['Year'],
    y=df_treated['Country Code']
)]
layout_toshow = go.Layout(
    title='Nombre de données par Année'
)
fig = go.Figure(data = data_toplot, layout=layout_toshow)
pyo.plot(fig, filename='graph//DESFNcount.html')

##
DESC_CC_CN = DESC[['Country Code','Country Name']]
DESC_CC_R = DESC[['Country Code','Region',]]

### On ajoute à DESFN les données de régions à partir de la Data Frame DESC

df_merge_FN_C = pd.merge(DESFN,DESC_CC_CN,how='left',left_on='Country Code', right_on='Country Code')
df_merge_FN_C = pd.merge(df_merge_FN_C,DESC_CC_R,how='left',left_on='Country Code', right_on='Country Code')

print(df_merge_FN_C.head())

### On regroupe les données de DESFN par nom de pays

df_mFNC_gpby_cn = df_merge_FN_C.groupby('Country Name').count().reset_index()

### on trace pour voir

### matplotlib
plt.title('Numbers of data by country', size=12)
graph2 = sns.barplot(y='Year', x='Country Name', data=df_mFNC_gpby_cn.sort_values('Year', ascending=False))
graph2.set_xticklabels(labels=df_mFNC_gpby_cn.sort_values('Year', ascending=False)['Country Name'], rotation=90,
                   size=6)
plt.ylabel('Datas count', fontsize=12)
plt.show()

###

dfsorted = df_mFNC_gpby_cn.sort_values('Year', ascending=False)
data2_toplot = [go.Bar(
    x=dfsorted['Country Name'],
    y=df_treated['Year']
)]
layout2_toshow = go.Layout(
    title='Numbers of data by country'
)
fig2 = go.Figure(data = data2_toplot, layout=layout2_toshow)
pyo.plot(fig2, filename='graph//WithGroupby_count.html')