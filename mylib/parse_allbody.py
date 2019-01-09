# -*- coding:utf-8 -*-
import hashlib
# from scrapy.utils.python import to_bytes
import os, shutil
from snownlp import SnowNLP
from random import sample
import time
from datetime import datetime
from re import sub
from mylib.items import Article
from peewee import IntegrityError, DataError, InternalError


def time_now():
    today = datetime.today()
    return today.strftime("%Y%m%d")


def rand_char(num):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(sample(str, num))


def rand_list():
    list = ['news', 'keji', 'bbs', 'blog', 'shenghuo']


def insert_table(it):
    Article.delete().where(Article.title == it['title']).execute()
    Article.insert(it).execute()


searchWords = '新闻资讯'
dirPath = r'F:\新蜘蛛池\article_news'

for parent, dir_names, filename in os.walk(dirPath):
    count = 1
    for name in filename:
        txt = os.path.join(parent, name)
        print(txt, count)
        count += 1
        if '[' in name:
            searchWords = parent.split('_')[1]
            # keyword = '%s,%s' % (searchWords, name.split(']')[0].lstrip('['))
            keyword = '%s' % (name.split(']')[0].lstrip('['))
            title = name.split(']')[1].strip('.txt')
            parse_txt = open(txt, 'r+', encoding='gb18030')
            content = ''
            for line in parse_txt:
                content += line
            parse_txt.close()
            try:
                s = SnowNLP(content)
                data = {
                    'title': sub(r'&nbsp', '', title),
                    'description': ','.join(s.summary(3)),
                    'keywords': keyword,
                    'author': '佚名',
                    'content': sub(r'&nbsp', '', content),
                    'type': 'news',
                    'url': '/news/%s%s.html' % (time_now(), rand_char(5)),
                }
                Article.delete().where(Article.title == data['title']).execute()
                Article.insert(data).execute()
            except (IntegrityError, ZeroDivisionError, DataError, InternalError):
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
                s = SnowNLP(content)
                data = {
                    'title': sub(r'&nbsp', '', title),
                    'description': ','.join(s.summary(3)),
                    'keywords': keyword,
                    'author': '佚名',
                    'content': sub(r'&nbsp', '', content),
                    'type': 'news',
                    'url': '/news/%s%s.html' % (time_now(), rand_char(5)),
                }
                Article.delete().where(Article.title == data['title']).execute()
                Article.insert(data).execute()
            except (IntegrityError, ZeroDivisionError, DataError, InternalError):
                print('重复 跳过')



