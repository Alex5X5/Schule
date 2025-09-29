import pandas
import copy

df:pandas.DataFrame = pandas.DataFrame(
    {
        'Datum':pandas.date_range(start='24-01-01',periods=5, freq='D'),
        'Umsatz':[100,200,150,300,250],
    }
)

#df['Datum'] = pandas.to_datetime(df['Datum'])
#df.update({'Datum':df['Datum'].dt.day_name()})
#gesamtumdatz:float = sum([umsatz for umsatz in df['Umsatz']])
#print(f'gesamtumdatz: {gesamtumdatz}')
#print(f'frame:\n{df}')



df1:pandas.DataFrame = pandas.DataFrame(
    {
        'ID':[1, 2, 3],
        'Name':['Anna', 'Bob', 'Charlie']
    }
)

df2:pandas.DataFrame = pandas.DataFrame(
    {
        'ID':[2, 3, 4],
        'Alter':[32,45,29]
    }
)

print(f'outer:\n{copy.copy(df1).set_index('ID').merge(copy.copy(df2).set_index('ID'), how="inner")}')
print(f'outer:\n{copy.copy(df1).join(df2, lsuffix='ID')}')
print(f'inner:\n{copy.copy(df1).merge(df2, how="inner")}')
print(f'cross:\n{copy.copy(df1).merge(df2, how="cross")}')
#df1_ = copy.copy(df1).update({'Stadt':['','','','']})
print(f'with Stadt:\n{copy.copy(df1).join(df2, how='inner', lsuffix='ID')}')
