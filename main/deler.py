import saver

def id_deler(data, id=None):
        if id == None:
            id = int(input('Введите id: '))
        data = data.T
        print('Вы хотите удалить эту заметку: ')
        print(*data.pop(id).values)
        data = data.T
        saver.save(data)

def title_deler(data):
    title = input('Введдите заголовок для поиска: ')
    id = data[data['Заголовок'] == title].index
    id_deler(data, id[0])