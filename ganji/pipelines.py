# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class GanjiPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect("E:\my_scrapy\ganji\ganji.sqlite")
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        insert_sql = "insert into rent_room_detail VALUES ('{}','{}', '{}','{}','{}','{}','{}','{}','{}')".\
            format(item['title'], item['price'], item['house_type'], item['address'], item['decorate_degree'],
                   item['area'], item['floor'], item['head_direction'], item['phone'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item

    def spider_close(self, spider):
        self.con.close()

