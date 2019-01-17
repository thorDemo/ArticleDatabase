from mylib.many_sql import InsertAll
from mylib.items import Sentence
from mylib.items import db
from mylib.delete_file import FileDelete
import os


target = 'C:/Users/Administrator/Desktop/菜鸡小说'

# FileDelete.delete_file2(target)
for parent, dir_names, filename in os.walk(target):
    for name in filename:
        txt = '%s/%s' % (parent, name)
        file1 = open(txt, 'r', encoding='utf-8')
        temp = 2
        lines = []
        for line in file1:
            if temp:
                temp = temp - 1
                continue
            text = line.strip().replace('<br/><br/>', '\n').replace(' ', '').strip('>').replace('\u3000', '')
            lines.extend(text.split('\n'))
        # print(lines)
        num = 0
        string = ''
        arg = []
        for line in lines:
            string += line
            num += 1
            if num % 4 == 0:
                data = {
                    'line': string,
                    'type': 'story',
                    'keyword': ''
                }
                arg.append(data)
                string = ''
        print(arg)
        with db.atomic():
            Sentence.replace_many(arg).execute()
        print('-------------------------')
        file1.close()
