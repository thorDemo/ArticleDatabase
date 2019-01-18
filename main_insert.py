from mylib.many_sql import InsertAll
from configparser import ConfigParser
# from threadpool import ThreadPool, makeRequests


config = ConfigParser()
config.read('config.ini', 'utf-8')
arg1 = []
# for num in range(1, 7):
#     try:
#         target = config.get('article', 'target%s' % num)
#         path = config.get('article', 'path%s' % num)
#         InsertAll.insert_all(target, path)
#     except Exception as e:
#         print(e)
#         continue
target = config.get('article', 'target1')
path = config.get('article', 'path1')
InsertAll.insert_all(target, path)

target = config.get('article', 'target2')
path = config.get('article', 'path2')
InsertAll.insert_all(target, path)

target = config.get('article', 'target3')
path = config.get('article', 'path3')
InsertAll.insert_all(target, path)

target = config.get('article', 'target4')
path = config.get('article', 'path4')
InsertAll.insert_all(target, path)

target = config.get('article', 'target5')
path = config.get('article', 'path5')
InsertAll.insert_all(target, path)

target = config.get('article', 'target6')
path = config.get('article', 'path6')
InsertAll.insert_all(target, path)

target = config.get('article', 'target7')
path = config.get('article', 'path7')
InsertAll.insert_all(target, path)

target = config.get('article', 'target8')
path = config.get('article', 'path8')
InsertAll.insert_all(target, path)

target = config.get('article', 'target9')
path = config.get('article', 'path9')
InsertAll.insert_all(target, path)

target = config.get('article', 'target10')
path = config.get('article', 'path10')
InsertAll.insert_all(target, path)

target = config.get('article', 'target11')
path = config.get('article', 'path11')
InsertAll.insert_all(target, path)

target = config.get('article', 'target12')
path = config.get('article', 'path12')
InsertAll.insert_all(target, path)

target = config.get('article', 'target13')
path = config.get('article', 'path13')
InsertAll.insert_all(target, path)