import scrapy
from car_spider.items import DetailLinkItem
from car_spider.items import DetailItem
from datetime import datetime
from scrapy_redis.spiders import RedisCrawlSpider


class GuaziInfoLinkSpider(scrapy.Spider):
    name = 'guazi_info_link'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/dg/mzdcx3']

    # 加载href_list
    # def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        # with open("data/guazi/guazi_href.txt", "r", encoding='utf-8') as f:
        #     for line in f.readlines():
        #         self.start_urls.append("https://" + line.rstrip('\n'))
        #     f.close()

    # 解析得到detail_link
    def parse(self, response):
        # 当前页面
        print('Requesting.. ==> ' + response.request.url)

        # 采集当前页面信息
        hrefs = response.xpath('/html/body/div[6]/ul/li/a/@href').getall()
        for href in hrefs:
            dd = DetailLinkItem(href="https://www.guazi.com"+str(href).split('#')[0])
            yield dd
            yield scrapy.Request(url=dd['href'],callback=self.detail_parse)

        # 获取下一页
        next_link = response.xpath('//a[@class="next"]/@href').getall()
        if len(next_link) is not 0:
            uu = "https://www.guazi.com"+str(next_link[0]).rsplit('/', 1)[0]
            # yield scrapy.Request(url=uu, callback=self.parse)

    # 解析detail
    def detail_parse(self, response):

        yield DetailItem(
            crawled= datetime.now().timestamp(),
            spider= self.name,
            href= response.request.url,

            title=response.xpath('//h2[@class="titlebox"]/text()').getall()[0],
            mileage= response.xpath('//ul[@class="basic-eleven clearfix"]/li[2]/div/text()').getall()[0],
            emission= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[10]/td[2]/text()').getall()[0],
            gearbox= response.xpath('//ul[@class="basic-eleven clearfix"]/li[4]/div/text()').getall()[0],
            transfers= response.xpath('//ul[@class="basic-eleven clearfix"]/li[6]/div/text()').getall()[0],
            region=str(response.request.url).split('/', 4)[3],

            manufacturer= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[2]/td[2]/text()').getall()[0],
            level= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[3]/td[2]/text()').getall()[0],
            engine= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[4]/td[2]/text()').getall()[0],
            gearbox_d= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[5]/td[2]/text()').getall()[0],
            LWH= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[7]/td[2]/text()').getall()[0],
            wheelbase= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[8]/td[2]/text()').getall()[0],
            luggage= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[9]/td[2]/text()').getall()[0],
            curb_weight= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[1]/tr[10]/td[2]/text()').getall()[0],
            displacement= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[2]/td[2]/text()').getall()[0],
            intake_form= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[3]/td[2]/text()').getall()[0],
            cylinders= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[4]/td[2]/text()').getall()[0],
            horsepower= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[5]/td[2]/text()').getall()[0],
            torque= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[6]/td[2]/text()').getall()[0],
            fuel= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[7]/td[2]/text()').getall()[0],
            fuel_label= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[8]/td[2]/text()').getall()[0],
            fuel_supply= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[2]/tr[9]/td[2]/text()').getall()[0],
            drive_method= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[2]/td[2]/text()').getall()[0],
            assistance= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[3]/td[2]/text()').getall()[0],
            front_suspension= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[4]/td[2]/text()').getall()[0],
            back_suspension= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[5]/td[2]/text()').getall()[0],
            front_brake= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[6]/td[2]/text()').getall()[0],
            back_brake= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[7]/td[2]/text()').getall()[0],
            driving_brake= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[8]/td[2]/text()').getall()[0],
            front_tire= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[9]/td[2]/text()').getall()[0],
            back_tire= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[3]/tr[10]/td[2]/text()').getall()[0],
            front_airbag= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[2]/td[2]/text()').getall()[0],
            side_airbag= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[3]/td[2]/text()').getall()[0],
            head_airbag= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[4]/td[2]/text()').getall()[0],
            tire_pressure= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[5]/td[2]/text()').getall()[0],
            locking= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[6]/td[2]/text()').getall()[0],
            child_seat= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[7]/td[2]/text()').getall()[0],
            keyless= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[8]/td[2]/text()').getall()[0],
            abs= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[9]/td[2]/text()').getall()[0],
            esp= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[4]/tr[10]/td[2]/text()').getall()[0],
            sunroof= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[2]/td[2]/text()').getall()[0],
            skylight= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[3]/td[2]/text()').getall()[0],
            suction_door= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[4]/td[2]/text()').getall()[0],
            induction_trunk= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[5]/td[2]/text()').getall()[0],
            induction_wiper= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[6]/td[2]').getall()[0],
            back_wiper= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[7]/td[2]').getall()[0],
            windows= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[8]/td[2]/text()').getall()[0],
            mirror_elec= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[9]/td[2]/text()').getall()[0],
            mirror_heat= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[5]/tr[10]/td[2]/text()').getall()[0],
            steering_wheel= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[2]/td[2]/text()').getall()[0],
            cruise= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[3]/td[2]/text()').getall()[0],
            air_cond= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[4]/td[2]/text()').getall()[0],
            air_control= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[5]/td[2]/text()').getall()[0],
            gps= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[6]/td[2]/text()').getall()[0],
            radar= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[7]/td[2]/text()').getall()[0],
            image= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[8]/td[2]/text()').getall()[0],
            leather= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[9]/td[2]/text()').getall()[0],
            seat_heat= response.xpath('//div[@class="detailcontent clearfix js-detailcontent active"]/table[6]/tr[10]/td[2]/text()').getall()[0],
        )