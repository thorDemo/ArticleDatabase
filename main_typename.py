from mylib.items import TypeName
from peewee import IntegrityError

file = open('C:/Users/Administrator/Desktop/sontype.txt', 'r', encoding='utf-8')
for line in file:
    arg = line.split(' ')
    data = {
        'name': arg[0],
        'type': arg[1],
        'sontype': arg[2].strip('\n'),
    }
    print(data)
    try:
        TypeName.replace(data).execute()
    except IntegrityError:
        print('重复跳过')

