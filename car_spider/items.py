# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


# 详情页链接
class DetailLinkItem(scrapy.Item):
    href = Field()


# 详情页数据
class DetailItem(scrapy.Item):

    crawled = Field()       # 抓取时间
    spider = Field()        # 爬虫名称
    href = Field()          # 来源

    title = Field()         # 标题
    mileage = Field()       # 表显里程
    emission = Field()      # 排放标准
    gearbox = Field()       # 变速箱
    transfers = Field()     # 过户次数
    region = Field()        # 城市 - 根据url解析得到

    manufacturer = Field()  # 厂商
    level = Field()         # 级别
    engine = Field()        # 发动机
    gearbox_d = Field()     # 变速箱详细信息
    LWH = Field()           # 长宽高
    wheelbase = Field()     # 轴距
    luggage = Field()       # 行李箱容积
    curb_weight = Field()   # 整备质量
    displacement = Field()  # 排量
    intake_form = Field()   # 进气形式
    cylinders = Field()     # 气缸数
    horsepower = Field()    # 最大马力
    torque = Field()        # 最大扭矩
    fuel = Field()          # 燃料类型
    fuel_label = Field()    # 燃油标号
    fuel_supply = Field()   # 供油方式
    drive_method = Field()  # 驱动方式
    assistance = Field()    # 助力类型
    front_suspension = Field()   # 前悬挂类型
    back_suspension = Field()    # 后悬挂类型
    front_brake = Field()   # 前制动类型
    back_brake = Field()    # 后制动类型
    driving_brake = Field() # 驱车制动类型
    front_tire = Field()    # 前轮胎类型
    back_tire = Field()     # 后轮胎类型
    front_airbag = Field()  # 主/副驾驶安全气囊
    side_airbag = Field()   # 前/后排侧气囊
    head_airbag = Field()   # 前/后排头部气囊
    tire_pressure = Field() # 胎压监测
    locking = Field()       # 车内中控锁
    child_seat = Field()    # 儿童座椅接口
    keyless = Field()       # 无钥匙启动
    abs = Field()           # 防抱死系统(ABS)
    esp = Field()           # 车身稳定控制(ESP)
    sunroof = Field()       # 电动天窗
    skylight = Field()      # 全景天窗
    suction_door = Field()  # 电动吸合门
    induction_trunk = Field()   # 感应后备箱
    induction_wiper = Field()   # 感应雨刷
    back_wiper = Field()    # 后雨刷
    windows = Field()       # 前/后电动车窗
    mirror_elec = Field()   # 后视镜电动调节
    mirror_heat = Field()   # 后视镜加热
    steering_wheel = Field()    # 多功能方向盘
    cruise = Field()        # 定速巡航
    air_cond = Field()      # 后排独立空调
    air_control = Field()   # 空调控制方式
    gps = Field()           # GPS导航
    radar = Field()         # 倒车雷达
    image = Field()         # 倒车影像系统
    leather = Field()       # 真皮座椅
    seat_heat = Field()     # 前/后排座椅加热


