import numpy
import pandas
try:
    data_frame:pandas.DataFrame = pandas.DataFrame(
            {
                'Name':['Anna', 'Bob', 'Charlie', 'David'],
                'Alter':[numpy.nan,32, numpy.nan,29],
                'Stadt':['Berlin', 'Hamburg', 'München', 'Köln'],
                'Beruf':['Ingenieurin','Lehrer','Arzt','Designer']
            }
    )

    #print(f'Names:{data_frame["Name"]}')
    #print(f'Names:{data_frame[data_frame["Name"] == 'Bob']}')
    """
    data_frame = pandas.DataFrame(
            {
                "Name": ["Anna", "Bob", "Charlie", "David"],
                "Alter": [25, numpy.nan, 45, 29],
                "Stadt": ["Berlin", "Hamburg", numpy.nan, "Köln"]
            }
    )
    """

    average = (sum([0 if alter[2] is None or numpy.isnan(alter[2]) else alter[2] for alter in list(data_frame.itertuples())]) / len(list(data_frame.itertuples())))
    print(average)
    #print('old:'+data_frame)
    #print(list(data_frame.itertuples()))
    print('fds'+str([average for i in range(0,len(list([data_frame[data_frame["Alter"] is None or numpy.isnan(data_frame["Alter"])]])))]))

    data_frame.Alter.replace(
        to_replace=data_frame[data_frame["Name"] == 'Bob'],
        value=[average for i in range(0,len(list([data_frame[data_frame["Name"] == 'Bob']])))]
    )

    #data_frame.loc[data_frame['Alter'] is None or numpy.isnan(data_frame['Alter']),'Alter'] = average
    #print('new:'+data_frame.head())

except Exception as e:
    print(e)
#print(f'Names:{data_frame[data_frame["Name"] == 'Bob']}')
