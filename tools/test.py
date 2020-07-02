# -*- coding: utf-8 -*-

# @Time : 2020/7/2 2:16 
# @Author : dzzhyk
# @File : test.py 
# @Software: PyCharm

# 测试

if __name__ == '__main__':
    # brand_name = "audi"
    # js = {
    #     brand_name: [
    #
    #     ]
    # }
    #
    # model = "audiA6"
    # model_href = "/audi/audiA6"
    #
    # js.get(brand_name).append({model: model_href})
    #
    # print(str(js).replace("\'", '\"'))

    path = "https://www.guazi.com/casdasdasd/82741f747e26a463x.htm"
    ls = path.split('/', 4)[3]
    print(ls)