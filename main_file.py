from configparser import ConfigParser
from mylib.delete_file import FileDelete
from mylib.changeName import ChangeName
from threadpool import ThreadPool, makeRequests


config = ConfigParser()
config.read('config.ini', 'utf-8')
arg = []
for num in range(1, 8):
    try:
        target = config.get('article', 'target%s' % num)
        path = config.get('article', 'path%s' % num)
    except:
        continue
    arg.append(target)

print(arg)
pool = ThreadPool(7)
# 整理文件
# request = makeRequests(ChangeName.change_file, arg)
# 删除多余
request = makeRequests(FileDelete.delete_file, arg)
[pool.putRequest(req) for req in request]
pool.wait()

