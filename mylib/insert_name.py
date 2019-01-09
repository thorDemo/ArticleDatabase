from mylib.items import UserName
from mylib.items import db


file_path = 'C:/Users/Administrator/Desktop/target/人名词典.txt'
arg = []

with open(file_path, 'r+', encoding='utf8') as file:
    count = 0
    for line in file:
        name = line.split(' ')[0]
        print(name)
        data = {
            'name': name,
            'type': 'real'
        }
        arg.append(data)
        if len(arg) == 100:
            with db.atomic():
                UserName.replace_many(arg).execute()
                arg = []
                print(count)
        count += 1
