import Paths

print(Paths.assets_path('names.csv'))
df:pandas.DataFrame = pandas.read_csv(Paths.assets_path('names.csv'))
