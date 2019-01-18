# -*- coding:utf-8 -*-
import os, shutil
from snownlp import SnowNLP
from random import sample, choice
from datetime import datetime
from re import sub
from mylib.items import Article, db
from peewee import IntegrityError, DataError, InternalError

# 这个是用来插入数据库的
# 这个是文件目录
# dirPath = 'C:/Users/Administrator/Desktop/历史/Article/'
# 这个是文章类型 拼音 gushi == 股市
# article_type = 'lishi'


class InsertAll:

    @staticmethod
    def time_now():
        today = datetime.today()
        return today.strftime("%Y%m%d")

    @staticmethod
    def rand_char(num):
        str_char = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        return ''.join(sample(str_char, num))

    @staticmethod
    def insert_table(it):
        Article.delete().where(Article.title == it['title']).execute()
        Article.insert(it).execute()

    @staticmethod
    def rand_list():
        list_name = ['news', 'shenghuo', 'bbs', 'blog', 'keji']
        return choice(list_name)

    @staticmethod
    def insert_all(dir_path, article_type='news'):
        arg = []
        print('%s/Article/' % dir_path)
        print(article_type)
        for parent, dir_names, filename in os.walk('%s/Article/' % dir_path):
            count = 1
            for name in filename:
                txt = os.path.join(parent, name)
                print(txt, count)
                count += 1
                if '[' in name:
                    # searchWords = parent.split('_')[1]
                    # keyword = '%s,%s' % (searchWords, name.split(']')[0].lstrip('['))
                    keyword = '%s' % (name.split(']')[0].lstrip('['))
                    title = name.split(']')[1].strip('.txt')
                    parse_txt = open(txt, 'r+', encoding='gb18030')
                    content = ''
                    for line in parse_txt:
                        content += line
                    parse_txt.close()
                    try:
                        content1 = sub(r'<img .*?/>|<img .*?>', '', content)
                        content1 = sub(r'&nbsp|&ns', '', content1)
                        content1 = sub(r'[<b></b><div></div><br><br/><p></p>\s\n\t]', '', content1)
                        s = SnowNLP(content1)
                        # type_name = InsertAll.rand_list()
                        description = ','.join(s.summary(3))
                        if len(description) > 100:
                            description = description[0:100] + '...'
                        data = {
                            'title': sub(r'&nbsp', '', title),
                            'description': description,
                            'keywords': keyword,
                            'author': '佚名',
                            'content': sub(r'&nbsp', '', content),
                            'type': article_type,
                            'url': '/%s/%s%s.html' % (article_type, InsertAll.time_now(), InsertAll.rand_char(5)),
                        }
                        arg.append(data)
                        print(data)
                        if len(arg) == 10:
                            with db.atomic():
                                Article.replace_many(arg).execute()
                                arg = []
                                print(count)
                    except (IntegrityError, ZeroDivisionError, DataError, InternalError) as e:
                        print(e)
                        print('重复 跳过')

                else:
                    # keyword = parent.split('_')[1]
                    keyword = '%s' % (name.split(']')[0].lstrip('['))
                    title = name.strip('.txt')
                    parse_txt = open(txt, 'r+', encoding='gb18030')
                    content = ''
                    for line in parse_txt:
                        content += line
                    parse_txt.close()
                    try:
                        content1 = sub(r'<img .*?/>|<img .*?>', '', content)
                        content1 = sub(r'[<b></b><div></div><br><br/><p></p>\s\n\t]', '', content1)
                        s = SnowNLP(content1)
                        description = ','.join(s.summary(3))
                        if len(description) > 100:
                            description = description[0:100] + '...'
                        data = {
                            'title': sub(r'&nbsp', '', title),
                            'description': description,
                            'keywords': keyword,
                            'author': '佚名',
                            'content': sub(r'&nbsp|&ns', '', content),
                            'type': article_type,
                            'url': '/%s/%s%s.html' % (article_type, InsertAll.time_now(), InsertAll.rand_char(5)),
                        }
                        arg.append(data)
                        if len(arg) == 10:
                            with db.atomic():
                                Article.replace_many(arg).execute()
                                arg = []
                                print(count)
                    except (IntegrityError, ZeroDivisionError, DataError, InternalError) as e:
                        print(e)
                        print('重复 跳过')

        with db.atomic():
            try:
                Article.replace_many(arg).execute()
                print('完成！')
            except (IntegrityError, ZeroDivisionError, DataError, InternalError) as e:
                print(e)
                print('重复 跳过')
