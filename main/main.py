import pandas as pd
import adder, reader, deler, changer
from datetime import datetime

data = pd.read_csv('/Users/estaban/Desktop/Прогерство/CR_PYT/main/data.csv', index_col=0)

print(f'          Наши возможности:       \nread   add   remove   change   see all')
action = input("Какое действие совершить? ")
if action == 'add': 
    adder.adder(data)

elif action == 'read':
    search = input('Поиск по id, Заголовку или Времени? ')
    if search =='id':
        reader.id_reader(data)
    elif search =='Заголовку':
        reader.title_reader(data)
    elif search == 'Времени':
        inter = input('Вы ищете заметки в интервале дней или одном дне? ')
        if inter == 'одном дне':
            yar = int(input('Год заметки: '))
            month = int(input('Месяц заметки: '))
            day = int(input('День заметки: '))
            reader.time_reader(data, start_date=datetime(yar, month, day))
        elif inter == 'интервале дней':
            print('Начало интервала')
            st_yar = int(input('Год заметки: '))
            st_month = int(input('Месяц заметки: '))
            st_day = int(input('День заметки: '))
            print('Конец интервала')
            end_yar = int(input('Год заметки: '))
            end_month = int(input('Месяц заметки: '))
            end_day = int(input('День заметки: '))
            reader.time_reader(data, start_date=datetime(st_yar, st_month, st_day), end_date=datetime(end_yar, end_month, end_day))
    else: 
        print('Такого поиска у нас нет')

elif action == 'remove': 
    search = input('Удаление по id или Заголовку? ')
    if search =='id':
        deler.id_deler(data)
    elif search =='Заголовку':
        deler.title_deler(data)
    else: 
        print('Такого способа удаления у нас нет')

elif action =='change': 
    search = input('Изменение по id или Заголовку? ')
    if search =='id':
        changer.id_changer(data)
    elif search =='Заголовку':
        changer.title_changer(data)
    else: 
        print('Такого способа изменения у нас нет')

elif action == 'see all':
    print(data)

else: 
    print('Hello')
