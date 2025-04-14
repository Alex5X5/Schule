import os
import pandas

import Paths

print(Paths.assets_path(''))
df:pandas.DataFrame = pandas.read_csv(Paths.assets_path('names.csv'))
