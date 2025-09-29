import pandas
from pandas import Series, DataFrame

def run():
    file_content:pandas.DataFrame = pandas.read_csv('/Assets/names.csv', delimiter=';')
    lines:int = 0
    try:
        with open('/Assets/datei.csv') as file_handle:
            lines = len(file_handle.readlines())
    except FileNotFoundError as e:
        print(e)

    print(file_content)

    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.expand_frame_repr', FileNotFoundError)
    print(file_content)