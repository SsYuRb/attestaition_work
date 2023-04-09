import pandas as pd
from datetime import datetime, timedelta

def id_reader(data):
    id = int(input('Введите id: '))
    print(*data.iloc[id])

def title_reader(data):
    title = input('Введдите заголовок для поиска: ')
    print(*data.loc[data['Заголовок'] == title].values[0])

def time_reader(data, start_date=None, end_date=None):
    delta = timedelta(days=1)  
    data['Время'] = pd.to_datetime(data['Время'])
    if end_date == None:
        selected_rows = data[data['Время'].dt.date == start_date.date()]
    else:
        selected_rows = data[data['Время'].between(start_date, end_date + delta)]
    print(selected_rows)