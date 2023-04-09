import saver
import adder
def id_changer(data, id=None):
        if id == None:
            id = int(input('Введите id: '))
        data = data.T
        print('Вы хотите изменить эту заметку: ')
        metka = data.pop(id).values
        print(*metka)
        data = data.T
        quest = input ('Что вы хотите изменить? ')
        if quest == 'Заголовок':
            adder.adder(data, info=metka[1])
        elif quest == 'Тело':
             adder.adder(data, title=metka[0])
        else:
            print('Такие изменения не положены')

def title_changer(data):
    title = input('Введдите заголовок для поиска: ')
    id = data[data['Заголовок'] == title].index
    id_changer(data, id[0])