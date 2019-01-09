from mylib.items import Pic, db
from peewee import IntegrityError, DataError, InternalError
import os


for parent, dir_names, filename in os.walk('C:/Users/Administrator/Desktop/life'):
    for name in filename:
        target = os.path.join(parent, name)
        txt = target.strip('.txt').split('-')[1]
        file = open(target, 'r', encoding='utf-8')
        arg = []
        count = 1
        for line in file:
            print(line)
            data = {
                'type': txt,
                'path': line.strip('\n')
            }
            count += 1
            arg.append(data)
            try:
                if len(arg) == 20:
                    with db.atomic():
                        Pic.replace_many(arg).execute()
                        arg = []
                        print(count)
            except (IntegrityError, ZeroDivisionError, DataError, InternalError) as e:
                print(e)
                print('重复 跳过')