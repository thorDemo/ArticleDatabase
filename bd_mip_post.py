from mylib.items import Article
from configparser import ConfigParser
import subprocess
import logging
import re
import time
import json

# ————————————
logger = logging.getLogger(__name__)            # 日志配置
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log/my_log.log', encoding='utf-8')
handler.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(handler)
logger.addFilter(ch)
# ————————————


# # 推送url到神马
def post_all_url(token):
    post = str(token).replace('urls.txt', 'source/urls.txt')
    print(post)
    output = subprocess.Popen(post, shell=True, stdout=subprocess.PIPE)
    out, err = output.communicate()
    try:
        http = eval(out)
        if b'success' in out:
            print('推送成功条 %s 条 校验成功 %s 条 剩余额度 %s 目标网址 %s'
                  % (http['success'], http['success_mip'], http['remain'], domain))
            logger.info('推送成功条 %s 条 校验成功 %s 条 剩余额度 %s 目标网址 %s'
                        % (http['success'], http['success_mip'], http['remain'], domain))
            return int(http['remain'])
        else:
            print('推送失败! error: %s' % http['message'])
            logger.error('推送失败! error: %s' % http['message'])
            return 0
    except IndexError as index:
        logger.debug(index)
        time.sleep(3)


# 生成推送链接
def get_all_urls(post_list, post_num):
    print('%s %s' % (post_list, post_num))
    path_all = Article.select(Article.url).where(Article.type == post_list).order_by(Article.id).limit(post_num)
    urls_all = open('source/urls.txt', 'w+')
    for it in path_all:
        urls_all.write('http://%s%s\n' % (domain, it.url))
    urls_all.close()
    print('获取完毕')


if __name__ == '__main__':
    config = ConfigParser()
    config.read('bd_mip_config.ini', 'utf-8')
    array_path = []
    array_number = []
    # 读取配置文件
    for num in range(1, 15):
        try:
            list_path = config.get('article', 'path%s' % num)
            number = config.get('article', 'num%s' % num)
        except Exception as e:
            print(e)
            continue
        array_number.append(number)
        array_path.append(list_path)

    tokens = open('source/bd_token.txt', 'r')
    # 判断
    is_domain = int(config.get('article', 'domain'))
    is_list = int(config.get('article', 'list'))
    remain = 0
    for line in tokens:
        domain = re.findall(r'site[=](.+?)[&]', line)[0]
        # 推送主页
        if is_domain == 1:
            print('推送主页 yes 开始进程')
            target = open('source/urls.txt', 'w')
            target.write('http://mip.jz-card.com/')
            target.close()
            remain = post_all_url(line)
        else:
            print('推送主页 false 跳过')
        # post_all_url(token)
        # 推送列表页
        if is_list == 1:
            print('推送列表 yes 开始进程')
            target = open('source/urls.txt', 'w')
            for path in array_path:
                target.write('http://%s/%s/\n' % (domain, path))
            target.close()
            post_all_url(line)
        else:
            print('推送列表 false 跳过')
        # 推送内容页
        for num in range(0, len(array_number)):
            number = int(array_number[num])
            path = array_path[num]
            if num == len(array_number) - 1:
                if remain > 2000:
                    get_all_urls(path, 2000)
                else:
                    get_all_urls(path, remain)
            else:
                get_all_urls(path, number)
            remain = post_all_url(line)
