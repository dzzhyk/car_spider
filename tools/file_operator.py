# -*- coding: utf-8 -*-

# @Time : 2020/7/2 17:01 
# @Author : dzzhyk
# @File : file_operator.py
# @Software: PyCharm


# 文件分割
def divide(filename, save_path, line_count):
    cc = 1
    lis = []
    with open(filename, "r", encoding='utf-8') as src:
        # 源文件名称
        name = src.name.split('/')[-1].split('.')[0]
        prefix = save_path + "/" + name + "_part_"
        for line in src.readlines():
            lis.append(line)
            if len(lis) >= line_count:
                fout = open(prefix +str(cc), "w", encoding='utf-8')
                for l in lis:
                    fout.write(l)
                fout.flush()
                fout.close()
                cc += 1
                lis.clear()
                continue
        if len(lis) > 0:
            fout = open(prefix + str(cc), "w", encoding='utf-8')
            for l in lis:
                fout.write(l)
            fout.flush()
            fout.close()
        src.close()
    print("divide done at：" + save_path)


# 文件合并
def merge(filename, location, parts, save_path):
    suffix = "_part_"
    path = save_path + "/" + filename
    with open(path, "a", encoding='utf-8') as fout:
        for i in range(1, parts+1):
            target = location+"/"+filename+suffix+str(i)
            fin = open(target, "r", encoding='utf-8')
            for line in fin.readlines():
                fout.write(line)
            fout.flush()
            fin.close()
        fout.close()
    print("merge done to：" + path)


if __name__ == '__main__':
    divide("../data/guazi/guazi_href.txt", "../data/guazi/devided", 30)
    # merge("guazi_href", "../data/guazi/devided",  8, "../data/guazi/merged")