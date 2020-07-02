# -*- coding: utf-8 -*-

# @Time : 2020/7/2 11:17 
# @Author : dzzhyk
# @File : href_clean.py 
# @Software: PyCharm

import json
from car_spider.util import SpiderUtil


# href数据清洗
def clean(car_code_txt, filename, save_to):
    cnt = 0
    with open(car_code_txt, "r", encoding='utf-8') as car_code:
        ff = open(filename, "r", encoding='utf-8')
        fout = open(save_to, "w", encoding='utf-8')
        for code in car_code.readlines():
            code_mod = SpiderUtil.rrstrip(code)
            ff_mod = SpiderUtil.rrstrip(ff.readline())
            dic = dict(json.loads(ff_mod))
            # 读取列表
            ls = list(dic[code_mod])
            for href_dic in ls:
                # # 生成临时域名
                for k, v in dict(href_dic).items():
                    v_mod = SpiderUtil.rrbread(v)
                    model = v_mod.split('/')[-2]
                    sub = v_mod.split('/')[-1]
                    if model == "rudong":
                        print(href_dic)
                        fout.write("/" +sub + "\n")
                    else:
                        fout.write("/" + model + "/" +sub + "\n")
                    cnt += 1
        fout.close()
        ff.close()
        car_code.close()
    return cnt


# 标准href生成
def generate(domain_url, subhref, save_to):
    cnt = 0
    f_sub = open(subhref, "r", encoding='utf-8')
    fout = open(save_to, "w", encoding='utf-8')
    temp = []

    for sub in f_sub.readlines():
        temp.append(SpiderUtil.rrstrip(sub))

    for sub_mod in temp:
        fout.write(domain_url + "/www" + sub_mod + "\n")
        cnt += 1
    return cnt


if __name__ == '__main__':
    # cnt = clean("../temp/guazi/guazi_car_code.txt", "../meta_data/guazi/guazi_model_href.json", "../temp/guazi/cleaned/guazi_subhref_cleaned.txt")
    # print("共计生成：" + str(cnt) + " 条临时subhref_cleaned记录")

    cnt = generate("www.guazi.com",
                   "../temp/guazi/cleaned/guazi_subhref_cleaned.txt",
                   "../data/guazi/guazi_href.txt")
    print("共计生成：" + str(cnt) + " 条href")