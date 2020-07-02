# -*- coding: utf-8 -*-

# @Time : 2020/7/2 13:06 
# @Author : dzzhyk
# @File : SpiderUtil.py 
# @Software: PyCharm


# 清除末尾\n
def rrstrip(string):
    temp = string.rstrip('\n')
    return temp


# 清除末尾#bread
def rrbread(string):
    temp = string.rsplit('/', 1)[0]
    return temp


if __name__ == '__main__':
    pass