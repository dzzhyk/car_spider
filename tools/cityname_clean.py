# -*- coding: utf-8 -*-

# @Time : 2020/7/2 11:51 
# @Author : dzzhyk
# @File : cityname_clean.py 
# @Software: PyCharm


# 有几个地名由于重名是中文编码访问404，暂时不采集
def clean(filename, save_to):
    cnt = 0
    with open(filename, "r", encoding='utf-8') as fin:
        with open(save_to, "w", encoding='utf-8') as fout:
            for line in fin.readlines():
                if line.isascii():
                    fout.write(line)
                    cnt += 1
                else:
                    print("check out：" + line)
            fout.close()
        fin.close()
    return cnt


if __name__ == '__main__':
    cnt = clean("../temp/guazi/guazi_city_domain.txt", "../temp/guazi/cleaned/guazi_city_domain_cleaned.txt")
    print("Done! 有效数据：" + str(cnt))