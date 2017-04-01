# news_spider
NIST's second homework

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import MySQLdb

def dbHandle():
    conn = pymysql.connect(
        host = "192.168.159.130",
        user = "root",
        passwd = "19970702",
        charset = "utf8",
        use_unicode = False
    )
    return conn
class NewsPipline(object):
    def process_item(self,item,spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE xinwen")
        sql = "INSERT INTO news(title,,url,body) VALUES(%s,%s,%s)"
        try:
            cursor.execute(sql,(item['title'],item['url'],item['body']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item

