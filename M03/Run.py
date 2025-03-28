import pandas
from pandas import DataFrame

data_frame:pandas.DataFrame = pandas.DataFrame(
        {
            'Name':['Anna', 'Bob', 'Charlie', 'David'],
            'Alter':[25,32,45,29],
            'Stadt':['Berlin', 'Hamburg', 'München', 'Köln'],
            'Beruf':['Ingenieurin','Lehrer','Arzt','Designer']
        }
)

print(f'Names:{data_frame["Name"]}')
#    data_frame.to_csv('test.csv', mode='w')