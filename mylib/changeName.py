import os


class ChangeName:
    # 这个是整理后的文件夹
    # target = 'C:/Users/Administrator/Desktop/绯闻/Article/'
    # 这个是采集新闻放置的文件夹
    # dirPath = 'C:/Users/Administrator/Desktop/绯闻/'
    # 标题文件夹
    # title = 'C:/Users/Administrator/Desktop/绯闻/title/'

    @staticmethod
    def change_file(target):
        os.mkdir('%s/Article/' % target)
        # os.mkdir(title)
        for parent, dir_names, filename in os.walk(target):
            for name in filename:
                try:
                    txt = os.path.join(parent, name)
                    print(txt)
                    keywords = parent.split('_')[1]
                    print(keywords)
                    if '[' in name:
                        parse = name.replace('[', '[%s,' % keywords)
                        file1 = open('%s/Article/%s' % (target, parse), 'w+', encoding='gb18030')
                    else:
                        file1 = open('%s/Article/[%s]%s' % (target, keywords, name), 'w+', encoding='gb18030')
                    file2 = open(txt, 'r+', encoding='gb18030')
                    for line in file2:
                        file1.write(line)
                    file1.close()
                    file2.close()
                except:
                    pass
