import pandas as pd
import os
import missingno as msno
import matplotlib.pyplot as plt

root = os.path.dirname(os.path.abspath(__file__))

folder = "data"
nest = root+'\\'+folder

def load_describe_df():
    list_df = []
    for file in os.listdir(nest):
        list_df.append(pd.read_csv(nest+"\\"+file))
        df = pd.read_csv(nest+"\\"+file)
        df_shape = df.shape
        df_col = df.columns
        df_info = df.info
        df_desc = df.head()
        print("la df est",file,"\n","les colonnes sont:","\n",df_col,
            "\n info :",df_info,"\n description :",df_desc
             ,"---------------")
        return list_df

list_df = load_describe_df()

## Cherchons les doublons

def show_duplicate():
    list_elt_dup = []
    for elt in list_df:
        duplicates = elt.duplicated()
        list_elt_dup.append(elt[duplicates])
    print(list_elt_dup)

##pas de doublon d'après le programme

## Complétude - Na values

def show_msno():
    for elt in list_df:
        print(elt.isna().sum())
        msno.matrix(elt)
        plt.show()

def df_withoutna():
    list_dfwna = []
    for elt in list_df:
        print(elt.dropna().isna().sum())
        list_dfwna.append(elt.dropna())
    return list_dfwna