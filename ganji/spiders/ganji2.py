# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import requests, json
from urllib import parse

class Ganji2Spider(CrawlSpider):
    name = 'ganji2'
    allowed_domains = ['sh.ganji.com']
    start_urls = ['http://sh.ganji.com/fang1/']

    rules = (
        Rule(LinkExtractor(allow=r'http://sh.ganji.com/fang1/\d+x.htm'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://sh.ganji.com/fang1/o\d+')),
    )


    def parse_item(self, response):
        i = {}
        # print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        i['title'] = ''.join(response.xpath('//p[@class="card-title"]/i/text()').extract())
        i['price'] = int(''.join(response.xpath('//span[@class="num"]/text()').extract()))
        i['address'] = ''.join(response.xpath(".//span[contains(text(),'所在地址')]/../span[@class='content']/a/text()").extract())
        i['house_type'] = ''.join(response.xpath('//ul[@class="er-list f-clear"]/li[1]/span[2]/text()').extract())
        i['decorate_degree'] = ''.join(response.xpath('//ul[@class="er-list f-clear"]/li[5]/span[2]/text()').extract())
        i['area'] = ''.join(response.xpath('//ul[@class="er-list f-clear"]/li[2]/span[2]/text()').extract()).replace(r'&nbsp','')
        i['floor'] = ''.join(response.xpath('//ul[@class="er-list f-clear"]/li[4]/span[2]/text()').extract())
        i['head_direction'] = ''.join(response.xpath('//ul[@class="er-list f-clear"]/li[3]/span[2]/text()').extract())

        user_id = response.xpath('.//input[@id="user_id_hide"]/@value').extract_first()
        puid = response.xpath('.//input[@id="puid"]/@value').extract_first()

        phone = response.xpath(".//div[@id='full_phone_show']/@data-phone").extract_first()
        url = 'http://sh.ganji.com/ajax.php?dir=house&module=secret_phone&user_id={}&puid={}&major_index=1&phone={}&isPrivate=1'.format(
            user_id, puid, parse.quote(phone))
        yield scrapy.Request(url, callback=self.get_phone, dont_filter=True, meta={'i':i})

    def get_phone(self, response):
        i = response.meta.get('i')
        info = json.loads(response.text)
        i['phone'] = ''.join(info.get('secret_phone'))
        yield i
        # print(i)