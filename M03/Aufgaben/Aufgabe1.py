import pandas
from numpy.ma.core import where


def aufgabe():
    dataframe:pandas.DataFrame = pandas.DataFrame(
            {
                'Name':['Anna', 'Bob', 'Charlie', 'David'],
                'Alter':[25,32,45,29],
                'Stadt':['Berlin', 'Hamburg', 'München', 'Köln'],
                'Beruf':['Ingenieurin','Lehrer','Arzt','Designer']
            }
    )
    selection = dataframe[dataframe['Stadt']=='Berlin']
    print(selection)
    #print(dataframe.columns)