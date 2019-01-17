import os


# 这个是用来删除过大的 文章
class FileDelete:

    # 这个是文件目录
    @staticmethod
    def get_file_size(file_path):
        fsize = os.path.getsize(file_path)
        fsize = fsize/float(1024)
        return round(fsize, 2)

    @staticmethod
    def delete_file(dir_path):
        for parent, dir_names, filename in os.walk('%sArticle' % dir_path):
            for name in filename:
                txt = os.path.join(parent, name)
                size = FileDelete.get_file_size(txt)
                if size > 50 or size < 0.5:
                    print('%s %s' % (txt, size))
                    os.remove(txt)

    @staticmethod
    def delete_file2(dir_path):
        for parent, dir_names, filename in os.walk('%s' % dir_path):
            for name in filename:
                txt = os.path.join(parent, name)
                size = FileDelete.get_file_size(txt)
                if size > 100 or size < 0.5:
                    print('%s %s' % (txt, size))
                    os.remove(txt)