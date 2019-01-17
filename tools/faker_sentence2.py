from mylib.many_sql import InsertAll
from mylib.items import Sentence
from mylib.items import db
from mylib.delete_file import FileDelete
import os
import re

target = 'C:/Users/Administrator/Desktop/news/中华励志网/'

# FileDelete.delete_file2(target)
number = 1
for parent, dir_names, filename in os.walk(target):
    for name in filename:
        txt = '%s/%s' % (parent, name)
        file1 = open(txt, 'r', encoding='utf-8')
        lines = []
        for line in file1:
            if line.strip() == '':
                continue
            p = re.compile('<[^>]+>')
            line = p.sub("", line)
            p = re.compile('style[^>]+>')
            line = p.sub("", line)
            text = line.replace(' ', '').replace('.com', '').replace('.', '').replace('\n', '')
            if len(text) < 30:
                continue
            # text.replace('。', '。@').replace('?', '')
            temp_arr = text.split('。')
            target_arr = []
            for it in temp_arr:
                target_arr.append('%s。' % it)
            lines.extend(target_arr)

        # print(lines)
        num = 0
        string = ''
        arg = []
        for line in lines:
            string += line
            num += 1
            if num % 3 == 0:
                data = {
                    'line': string,
                    'type': 'lizhi',
                    'keyword': ''
                }
                arg.append(data)
                string = ''
        print(arg)
        try:
            with db.atomic():
                Sentence.replace_many(arg).execute()
        except:
            pass
        print('-------------------------%s' % number)
        number += 1
        file1.close()
