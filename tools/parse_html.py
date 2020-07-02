# -*- coding: utf-8 -*-

# @Time : 2020/7/1 23:10 
# @Author : dzzhyk
# @File : parse_html.py 
# @Software: PyCharm


import bs4


# 解析并且返回HTML文本
def HTMLTextconvert(html):
    try:
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup
    except:
        print("HTMLConvertError!")
        return " "


# 数据清洗：检索HTML中的信息
def parse(html, reverse):
    ss = '{\n"model_code":['
    cnt = 0
    # 找到所有tbody标签下的所有内容，并且遍历所有节点
    for li in html.find("ul").children:
        # 添加判断：获得的内容是否为标签Tag类型
        if isinstance(li, bs4.element.Tag):
            for p in li.find("p").children:
                if isinstance(p, bs4.element.Tag):
                    # 得到a标签
                    # 获取车型中文及其代号
                    name = '\"' + p.text + '\"'
                    code = '\"' + p.attrs.get("href").split('/')[-2] + '\"'
                    # 生成类json格式
                    if reverse is False:
                        ss += "{" + name + ": " + code + "},\n"
                    else:
                        ss += "{" + code + ": " + name + "},\n"
                    cnt += 1
    ss += "]\n}"
    return ss, cnt


def outter_txt(html, filepath):
    # 输出信息到json文件
    cnt = 0
    with open(filepath, "w", encoding="utf-8") as f:
        # 找到所有tbody标签下的所有内容，并且遍历所有节点
        for li in html.find("ul").children:
            # 添加判断：获得的内容是否为标签Tag类型
            if isinstance(li, bs4.element.Tag):
                for p in li.find("p").children:
                    if isinstance(p, bs4.element.Tag):
                        # 得到a标签获取车型代号
                        code = p.attrs.get("href").split('/')[-2]
                        # 写入行
                        f.write(code + "\n")
                        cnt += 1
        f.close()
    return cnt


if __name__ == '__main__':
    with open("../meta_data/guazi/guazi_car_brand.html", "r", encoding="utf-8") as f:
        html = f.read()
        soup = HTMLTextconvert(html)

        cnt = outter_txt(soup, "../temp/guazi/guazi_car_code.txt")
        print("共计：" + str(cnt) + " 种车牌")

        # ss, cnt = parse(soup, True)
        # print("共计：" + str(cnt) + " 种车牌")
        # f.close()
        # # 输出信息到json文件
        # with open("../temp/guazi/guazi_car_code_brand.json" , "w", encoding="utf-8") as f1:
        #     print(ss)
        #     f1.write(ss)
        #     f1.close()

