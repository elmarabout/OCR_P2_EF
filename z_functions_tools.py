import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

import os
root = os.path.dirname(os.path.abspath(__file__))
source = "src"
nest = root+'\\'+source


def load_describe_df(nest):
    list_df = []
    for file in os.listdir(nest):
        list_df.append(pd.read_csv(nest+"\\"+file))
        #df = pd.read_csv(nest+"\\"+file)
    return list_df[0],list_df[1],list_df[2],list_df[3],list_df[4]

def describe_light(list_df):
    for df in list_df:
        df_shape = df.shape
        df_col = df.columns
        df_info = df.info()
        df_desc = df.head()
        print("la df est :\n", df, "\n de dimension : :\n",df_shape, "\nles colonnes sont:\n", "\n", df_col,
          "\n info :\n", df_info, "\n description :\n", df_desc, "---------")
    return None

def killemptiness(list_df):
    list_dfkilled=[]
    for elt in list_df:
        pct_na = elt.isna().sum() / len(elt)
        pct_max = 0.99
        missing_feature = pct_na[pct_na > pct_max].index
        elt.drop(missing_feature, axis =1, inplace=True)
        #elt.dropna(inplace=True)
        list_dfkilled.append(elt)
    print("après un nettoyage au taux de ",str(pct_max),"on a ",list_dfkilled[0].shape, list_dfkilled[1].shape, list_dfkilled[2].shape, list_dfkilled[3].shape,list_dfkilled[4].shape)
    return list_dfkilled

def replace_namecdf(df1, col_name, name_before, name_after):
    df1[df1[col_name] == name_before, col_name] = name_after
    print(df1[col_name])
    return None


def rename_coldf(df1, col_before, col_after):
    if col_before in df1.columns:
        df1.rename(columns={col_before: col_after}, inplace=True)
        print("verification nom de colonnes: \n" + str(col_after in df1.columns))
        return df1
    else:
        return "not is the df"

def delete_devantrelou(df1, col, lstrip_carac):
    df1[col] = df1[col].map(lambda x: x.lstrip(lstrip_carac))
    return None

def show_duplicate(list_df):
    list_elt_dup = []
    for elt in list_df:
        duplicates = elt.duplicated()
        list_elt_dup.append(elt[duplicates])
    print(list_elt_dup)


def show_msno(list_df):
    for i, elt in enumerate(list_df):
        msno.matrix(elt)
        plt.savefig("C:\\Users\\felvy\\PycharmProjects\\OCR_projects\\OCR_P2_EF\\missingo\\"+str(i)+".png")

def df_withoutna(list_df):
    list_dfwna = []
    for elt in list_df:
        eltwna = elt.dropna()
        print("les valeurs manquantes sont ci-dessous \n",eltwna.isna().sum())
        list_dfwna.append(eltwna)
        print("la dimension de la df est maintenant :\n",eltwna.shape,"----")
    return list_dfwna[0].shape,list_dfwna[0].shape,list_dfwna[0].shape,list_dfwna[0].shape

def export_dfcleaned():
    dfkilled = killemptiness()
    DESCS = dfkilled[0]
    DESC = dfkilled[1]
    DESD = dfkilled[2]
    DESFN = dfkilled[3]
    DESS = dfkilled[4]
    return DESCS,DESC, DESD, DESFN, DESS

def diff(li1, li2):
    li1 = li1.unique().tolist()
    li2 = li2.unique().tolist()
    diffs = list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))
    print(len(diffs), "differences between the two columns")
    print("Here are the differences \n", diffs)
    return (set(li1) - set(li2)), (set(li2) - set(li1))