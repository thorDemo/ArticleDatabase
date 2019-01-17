### main_file.py 
    print(arg)
    pool = ThreadPool(7)
    # 整理文件 
    # request = makeRequests(ChangeName.change_file, arg)
    # 删除多余
    # request = makeRequests(FileDelete.delete_file, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
  * 先去掉整理文件的注释 先整理文件
  * 再去掉删除多余文件的注释 删除文件 切勿同时解除注释
### main_insert.py 
    这个用来把按关机词采集好的文章发布到数据库


* 注意有时候翻译会出错 翻译出来是空白的
* 文章有些编码错误 插入数据库会直接跳过
* 标题重复的也会直接跳过 10个一组插入数据库 如果有一个标题重复这10篇文章都插不进去


## 新增 mip 推送 
    可以推送百度 也可以推送神马 从数据库调取数据
    配置在 sm_mip_config.ini 
    配置在 bd_mip_config.ini 注意计算总量
## token 
    位置在：
        source/bd_token.txt
        source/sm_token.txt
    同类型的站可放多条
### 运行 sm_mip_post.py 即可
### 运行 bd_mip_post.py 即可

