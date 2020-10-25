import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.offline as pyo
import plotly.graph_objs as go

from AnaExplo import export_dfcleaned
from AnaExplo import rename_coldf,drop_doppledanger

DESCS,DESC, DESD, DESFN, DESS = export_dfcleaned()

print(DESCS[['Indicator Name','Indicator Code','2010s']])