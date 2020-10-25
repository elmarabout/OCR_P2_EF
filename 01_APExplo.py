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
        df_info = df.info()
        df_desc = df.head()
        print("la df est\n",file,"\n","les colonnes sont:\n","\n",df_col,
            "\n info :\n",df_info,"\n description :\n",df_desc
             ,"---------------")
    return list_df[0],list_df[1],list_df[2],list_df[3],list_df[4]

list_df = list(load_describe_df())

## Cherchons les doublons

def show_duplicate():
    list_elt_dup = []
    for elt in list_df:
        duplicates = elt.duplicated()
        list_elt_dup.append(elt[duplicates])
    print(list_elt_dup)

print("Les doublons sont ", show_duplicate())
##pas de doublon d'après le programme

## Complétude - Na values

def show_msno():
    for elt in list_df:
        print(elt.isna().sum())
        msno.bar(elt)
        plt.show()

def df_withoutna():
    list_dfwna = []
    for elt in list_df:
        eltwna = elt.dropna()
        print("les valeurs manquantes sont ci-dessous \n",eltwna.isna().sum())
        list_dfwna.append(eltwna)
        print("la dimension de la df est maintenant :\n",eltwna.shape,"----")
    return list_dfwna[0].shape,list_dfwna[0].shape,list_dfwna[0].shape,list_dfwna[0].shape

# c'est nul comme méthode brut, il ne reste plus rien dans les dataframes

## Je souhaite nettoyer les dataframes des colonnes parcimonieuses
list_dfkilled=[]
def killemptiness():
    for elt in list_df:
        pct_na = elt.isna().sum() / len(elt)
        missing_feature = pct_na[pct_na > 0.98].index
        elt.drop(missing_feature, axis =1, inplace=True)
        #elt.dropna(inplace=True)
        list_dfkilled.append(elt)
    print("après un nettoyage à 80% on a ",list_dfkilled[0].shape, list_dfkilled[1].shape, list_dfkilled[2].shape, list_dfkilled[3].shape,list_dfkilled[4].shape)
    return list_dfkilled

def export_dfcleaned():
    dfkilled = killemptiness()
    DESCS = dfkilled[0]
    DESC = dfkilled[1]
    DESD = dfkilled[2]
    DESFN = dfkilled[3]
    DESS = dfkilled[4]
    return DESCS,DESC, DESD, DESFN, DESS

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()

def replace_namecdf(df1, col_name, name_before, name_after):
    df1[df1[col_name] == name_before, col_name] = name_after
    print(df1[col_name])
    return None


def rename_coldf(df1, col_before, col_after):
    if col_before in df1.columns:
        df1.rename(columns={col_before: col_after}, inplace=True)
        print("after action renaming",df1[col_after])
        return None
    else:
        return "not is the df"

def delete_devantrelou(df1, col, lstrip_carac):
    df1[col] = df1[col].map(lambda x: x.lstrip(lstrip_carac))
    return None

####### on harmonise les noms de colonnes

rename_coldf(DESC,'Table Name','Country Name')

rename_coldf(DESCS,'CountryCode','Country Code')
rename_coldf(DESCS,'SeriesCode','Indicator Code')
rename_coldf(DESCS,'DESCRIPTION','Desc Data')

rename_coldf(DESFN,'CountryCode','Country Code')
rename_coldf(DESFN,'SeriesCode','Indicator Code')
rename_coldf(DESFN,'DESCRIPTION','Desc Data')

rename_coldf(DESS,'SeriesCode','Indicator Code')

#### drop duplicate

