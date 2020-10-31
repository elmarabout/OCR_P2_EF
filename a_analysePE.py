import pandas as pd
import os
import missingno as msno
import matplotlib.pyplot as plt
import pprint

##### fonctions crées

from z_functions_tools import load_describe_df, show_duplicate, show_msno, export_dfcleaned,df_withoutna
from z_functions_tools import killemptiness,rename_coldf, delete_devantrelou,replace_namecdf, diff

## définition de l'espace de travail
root = os.path.dirname(os.path.abspath(__file__))
source = "src"
nest = root+'\\'+source

### On charge les fichiers sources du dossier src pour charger les dataframes correspondantes

list_df = list(load_describe_df(nest))

DESCS,DESC, DESD, DESFN, DESS = list_df[0],list_df[1],list_df[2],list_df[3],list_df[4]

DESCS,DESC, DESD, DESFN, DESS = DESCS.copy(),DESC.copy(), DESD.copy(), DESFN.copy(), DESS.copy()

print(DESC['Table Name'].head)

# Cherchons les doublons

print("Les doublons sont ", show_duplicate(list_df))
# -> Pas de doublons

# on peut observer graphiquement le nombre de données manquante

show_msno(list_df)

####### on harmonise les noms de colonnes

DESC = rename_coldf(DESC,'Table Name','Country Name')

DESCS = rename_coldf(DESCS,'CountryCode','Country Code')
DESCS = rename_coldf(DESCS,'SeriesCode','Indicator Code')

DESFN = rename_coldf(DESFN,'CountryCode','Country Code')
DESFN = rename_coldf(DESFN,'SeriesCode','Series Code')

DESD = rename_coldf(DESD,'Indicator Code','Series Code')

# Complétude - Na values

list_df2 = DESCS,DESC, DESD, DESFN, DESS
DESCS2,DESC2, DESD2, DESFN2, DESS2 = killemptiness(list_df2)

# vérification de la bonne récupération des bonnes DF avec les bonnes colonnes renomées
print("DESCS2 :\n",DESCS2.columns,"DESC2 :\n",DESC2.columns,
      "DESD :\n",DESD2.columns,"DESFN2 :\n",
      DESFN2.columns,"DESS2 :\n", DESS2.columns)

# On identifie les différences ensuite

# d = diff(DESCS2['Country Code'],DESD2['Country Code'])
# print(set(DESCS2['Country Code'].tolist()))
# print(set(DESD2['Country Code'].tolist()))

DESCS2.to_csv("data/DESCS2.csv")
DESC2.to_csv("data/DESC2.csv")
DESD2.to_csv("data/DESD2.csv")
DESFN2.to_csv("data/DESFN2.csv")
DESS2.to_csv("data/DESS2.csv")
#
# DESD.iloc[:10,:].to_csv("data/DESD_head.csv")