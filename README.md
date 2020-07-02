# car_spider —— 基于scrapy的二手车销售信息爬虫

## 环境需求

[requirements.txt](./requirements.txt)

## 主要内容
目前仅支持爬取瓜子二手车车源信息，可获取详情页信息大致如下：<br>
输出文件的每一行是一个如下形式的json数据<br>
[输出文件](data/guazi/guazi_detail.txt)为：data/guazi/guazi_detail.txt
```json
{
    "crawled": 1593691514.158705,
    "spider": "guazi_info_link",
    "href": "https://www.guazi.com/cq/a4338ba56fa9aeb0x.htm",
    "title": "\r\n        马自达CX-3 2018款 2.0L 自动豪华型(进口)\r\n                                    ",
    "mileage": "1.08万公里",
    "emission": "国5",
    "gearbox": "自动",
    "transfers": "0次过户\r\n            ",
    "region": "cq",
    "manufacturer": "马自达(进口)",
    "level": "小型SUV",
    "engine": "2.0L/148马力/L4",
    "gearbox_d": "6挡手自一体",
    "LWH": "4275/1765/1548",
    "wheelbase": "2570",
    "luggage": "-",
    "curb_weight": "1232",
    "displacement": "2.0",
    "intake_form": "自然吸气",
    "cylinders": "4缸",
    "horsepower": "148",
    "torque": "192",
    "fuel": "汽油",
    "fuel_label": "92号",
    "fuel_supply": "直喷",
    "drive_method": "前置前驱",
    "assistance": "电动助力",
    "front_suspension": "麦弗逊式独立悬架",
    "back_suspension": "扭力梁式非独立悬架",
    "front_brake": "通风盘式",
    "back_brake": "盘式",
    "driving_brake": "手刹",
    "front_tire": "215/60 R16",
    "back_tire": "215/60 R16",
    "front_airbag": "标配/标配",
    "side_airbag": "标配/-",
    "head_airbag": "标配/标配",
    "tire_pressure": "-",
    "locking": "标配",
    "child_seat": "标配",
    "keyless": "-",
    "abs": "标配",
    "esp": "标配",
    "sunroof": "-",
    "skylight": "-",
    "suction_door": "-",
    "induction_trunk": "-",
    "induction_wiper": "<td width=\"50%\" class=\"td2\">-</td>",
    "back_wiper": "<td width=\"50%\" class=\"td2\">标配</td>",
    "windows": "标配/标配",
    "mirror_elec": "标配",
    "mirror_heat": "标配",
    "steering_wheel": "标配",
    "cruise": "-",
    "air_cond": "-",
    "air_control": "自动",
    "gps": "选配",
    "radar": "-",
    "image": "标配",
    "leather": "-",
    "seat_heat": "-/-"
}
```

可获取[瓜子二手车网](www.guazi.com)city-domain对照表

## 项目结构
```
├─car_spider
│  ├─car_spider
│  │  ├─spiders
│  ├─constant
│  ├─data
│  │  └─guazi
│  │      ├─devided
│  │      ├─getted
│  │      └─merged
│  ├─log
│  ├─meta_data
│  │  └─guazi
│  ├─temp
│  │  └─guazi
│  │      └─cleaned
│  ├─tools
│  ├─util
```

## log
2020.7.2 ==> 初步完成基本功能

## author
[dzzhyk@qq.com](mailto:dzzhyk@qq.com)