
import scrapy
import json


# 根据车品牌分别抓取所有品牌下车系信息
class GuaziBrandModelSpider(scrapy.Spider):
    name = 'guazi_brand_model'
    allowed_domains = ["www.guazi.com"]
    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 生成url信息
        self.start_urls = []
        with open("temp/guazi/guazi_car_brand_code.json", "r", encoding="utf-8") as f:
            # 固定从rudong这个地区下搜索即可
            url = "https://www.guazi.com/rudong/"
            # 获取车品牌列表，内容为字典
            code_list = list(dict(json.load(f)).get("model_code"))
            for code in code_list:
                for key in dict(code):
                    # 生成url
                    self.start_urls.append(str(url + dict(code).get(key)))
            f.close()

    def parse(self, response):

        # 获取当前车牌code
        code = response.request.url.split('/')[-1]
        if code is '':
            code = 'UNKNOWN'
        # 写入json文件
        js = {code: []}

        with open("meta_data/guazi/guazi_model_href.json", "a", encoding='utf-8') as f:
            lines = response.xpath('//div[@class="dd-car js-tag js-option-hid-info"]//ul//li')
            for line in lines:
                model = str(line.xpath('.//a//text()').get())
                model_after = model.replace('\n', '').replace('\r', '').strip(' ')
                model_href = line.xpath('.//a//@href').get()
                js.get(code).append({model_after: model_href})

            f.write(str(js).replace("'", '"')+"\n")
            f.close()
