# -*- coding: utf-8 -*-
import scrapy
from yuxing.items import YuxingItem

class YuSpider(scrapy.Spider):
    name = 'yu'
    allowed_domains = ['ucchip.com']
    start_urls = ['http://ucchip.com/']

    def parse(self, response):
        item = YuxingItem()
        abc = response.xpath("//div[@class='row text-center']//text()").extract()
        ab = "".join(abc)
        ab.replace("\n", "")

        item['jishu'] = ab
        cmk = response.xpath("//section[@id='portfolio']//div[@class='col-md-4 col-sm-6 portfolio-item']//div[@class='portfolio-caption']//text()").extract()
        ck = "".join(cmk)
        item['chanping'] = ck.replace("\n", "")

        lpl = response.xpath("//div[@class='modal-body']//text()").extract()
        lp = "".join(lpl)

        item['news'] =lp.replace("\n","")
        zp = response.xpath("//section[@id='team']//text()").extract()
        zc = "".join(zp)
        item['zhaoping'] = zc

        yield item
