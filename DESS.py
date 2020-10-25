import pandas as pd

from AnaExplo import export_dfcleaned

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()

### Fonction de remplacement de titre colonne

def replace_namecdf(df1,col_name,name_before,name_after):
    df1[df1[col_name] == name_before,col_name] = name_after
    print(df1[col_name])
    return None

def rename_coldf(df1, col_before, col_after):
    df1.rename(columns = {col_before : col_after}, inplace = True)
    return None

def delete_devantrelou(df1, col, lstrip_carac):
    df1[col] = df1[col].map(lambda x:x.lstrip(lstrip_carac))
    return None

def lets_barplot(df, col):
    import matplotlib.pyplot as plt
    import seaborn as sns
    data = df[col].value_counts()
    graph = sns.barplot(x = data.values, y = data.index)
    labels = [item.get_text() for item in graph.get_yticklabels()]
    graph.set_yticklabels(labels, fontsize= 10)
    plt.xlabel('Number', fontsize = 9)
    plt.show
    return None

