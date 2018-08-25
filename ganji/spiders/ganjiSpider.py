# coding:utf-8
import scrapy
from ..items import GanjiItem

class GanjiSpider(scrapy.Spider):
    name = "ganjiF"
    # host_name = "http://sh.ganji.com/{}"
    start_urls = ["http://www.spbeen.com/tool/request_info/"]
    start_url = "http://www.spbeen.com/tool/request_info/"

    def start_requests(self):
        for i in range(10):
            yield scrapy.Request(self.start_url, dont_filter=True)

    def parse(self, response):

        # gj = GanjiItem()
        # items = response.xpath("//div[@class='f-main-list']/div[1]/div[@class='f-list-item ershoufang-list']")
        # for i in items:
        #     gj['title'] = ''.join(i.xpath("./dl/dd[1]/a/text()").extract())
        #     gj['price'] = int(''.join(i.xpath("./dl/dd[5]/div[1]/span[1]/text()").extract()))
        #     gj['unit'] = ''.join(i.xpath("./dl/dd[5]/div[1]/span[2]/text()").extract())
        #     gj['address'] = ''.join(i.xpath("./dl/dd[3]/span/a/text()").extract())
        #     gj['info'] = ''.join(i.xpath("./dl/dd[2]/span/text()").extract())
        #     yield gj
        info = {}
        info['user_agent'] = response.xpath('normalize-space(/html/body/div[2]/div[3]/div/div[2]/div[2]/text())').extract()
        info['ip'] = response.xpath('normalize-space(/html/body/div[2]/div[3]/div/div[3]/div[2]/text())').extract()
        print(info)

        # next_links = response.xpath("//a[@class='next']/@href").extract()
        # if len(next_links) > 0:
        #     next_link = self.host_name.format(next_links[0])
        #     print(next_link)
        #     yield scrapy.Request(next_link, callback=self.parse)
        # else:
        #     print("*"*20+"no--next--page"+"*"*20)