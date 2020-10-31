import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.offline as pyo
import plotly.graph_objs as go


DESC = pd.read_csv("data/DESC2.csv")
DESD = pd.read_csv("data/DESD2.csv")
DESFN = pd.read_csv('data/DESFN2.csv')
DESCS = pd.read_csv('data/DESCS2.csv')

list_countrycode = DESCS['Country Code'].unique().tolist()
print(list_countrycode)

print(DESCS.columns)

desclist = DESCS['DESCRIPTION'].unique().tolist()
desc_count = DESCS['DESCRIPTION'].value_counts()