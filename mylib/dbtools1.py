from mylib.items import Article, TypeName
from peewee import IntegrityError

with open('source/jiaoyou_keywords.txt', 'r+', encoding='utf-8') as file:
    for line in file:
        print(line.strip('\n'))
        try:
            TypeName.insert({'name': line.strip('\n'), 'type': 'jiaoyou'}).execute()

        except IntegrityError:
            print('重复 跳过！')
