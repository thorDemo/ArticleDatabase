from peewee import *
from datetime import datetime

db = MySQLDatabase('xbw', host='142.234.162.83', port=3306, user='root', passwd='123456', charset='utf8')
# db = MySQLDatabase('xbw', host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')


class Article(Model):
    id = AutoField()
    title = CharField(max_length=255)
    description = TextField()
    keywords = CharField(max_length=255)
    author = CharField(max_length=255)
    content = TextField()
    pic = CharField(max_length=255)
    type = CharField(max_length=255)
    pub_time = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    url = CharField(max_length=255)

    class Meta:
        table_name = 'article'
        database = db


class Pic(Model):
    id = AutoField()
    path = CharField(max_length=255)
    type = CharField(max_length=255)

    class Meta:
        table_name = 'pic'
        database = db


class TypeName(Model):
    id = AutoField()
    name = CharField(max_length=255)
    type = CharField(max_length=255)
    sontype = CharField(max_length=255)

    class Meta:
        table_name = 'typename'
        database = db


class UserName(Model):
    id = AutoField()
    name = CharField(max_length=255)
    type = CharField(max_length=255)

    class Meta:
        table_name = 'typename'
        database = db
