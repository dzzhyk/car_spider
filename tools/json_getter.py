# -*- coding: utf-8 -*-

# @Time : 2020/7/2 0:03 
# @Author : dzzhyk
# @File : json_getter.py 
# @Software: PyCharm

import json


# 拿到json数据中的部分内容
def getter(filepath, save_as, reverse):
    cnt = 0
    ss = '{\n"domain_name":['
    with open(filepath, "r", encoding="utf-8") as f:
        # 得到json字典
        dic = dict(json.load(f))
        for first in dic.keys():
            ls = list(dic.get(first))
            for i in ls:
                domain = '\"' + dict(i).get("domain") + '\"'
                name = '\"' + dict(i).get("name") + '\"'
                if reverse is False:
                    ss += "{" + name + ": " + domain + "},\n"
                else:
                    ss += "{" + domain + ": " + name + "},\n"
                cnt += 1
        f.close()
    ss += "]\n}"
    # 输出信息到json文件
    with open(save_as, "w", encoding="utf-8") as f1:
        f1.write(ss)
        f1.close()
    return cnt


def outter_txt(filepath, save_as):
    cc = 0
    with open(save_as, "w", encoding="utf-8") as f1:
        with open(filepath, "r", encoding="utf-8") as f:
            # 得到json字典
            dic = dict(json.load(f))
            for first in dic.keys():
                ls = list(dic.get(first))
                for i in ls:
                    # 输出信息到txt文件
                    domain = dict(i).get("domain")
                    f1.write(domain + "\n")
                    cc += 1
            f.close()
        f1.close()
    return cc


if __name__ == '__main__':
    cnt = getter("../meta_data/guazi/guazi_city.json", "../temp/guazi/guazi_domain_city.json", True)
    print("共计：" + str(cnt) + " 个城市代号")

    # cnt = outter_txt("../meta_data/guazi/guazi_city.json", "../temp/guazi/guazi_city_domain.txt")
    # print("共计：" + str(cnt) + " 个城市代号")

