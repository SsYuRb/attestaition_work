import pandas as pd
import saver
import datetime

def adder(data, title=None, info=None):
    if title == None:
        title = input("Заголовок новой заметки: ")
    if info == None:
        info = input("Тело заметки: ")
    new = pd.DataFrame({'Заголовок': title, 'Тело': info, 'Время': pd.to_datetime(datetime.datetime.now())}, index=[0])
    data = pd.concat([data, new], ignore_index=True,  names=['Заголовок', 'Тело', 'Время'])
    saver.save(data)