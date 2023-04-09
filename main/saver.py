def save(data):
    save = input('Сохранить? ')
    if (save == 'да' or save == 'Да'):
        data.to_csv('/Users/estaban/Desktop/Прогерство/CR_PYT/main/data.csv')
        print('Сохранено')
    else:
        print('ОК, ничего не сохраняем')