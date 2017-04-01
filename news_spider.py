# news_spider
NIST's second homework

#coding:utf-8
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from news.items import NewsItem

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ["tech.163.com"]
    start_urls = ['http://tech.163.com/']

def parse_news(self,response):
    item = NewsItem
    self.get_title(response,item)
    self.get_url(response,item)
    self.get_body(response,item)
    return item

def get_title(self,response,item):
    title = response.xpath("//div/li[@class='list_item']/a/p[@class='nl-title']/text()").extract()
    if title:
        item['title'] = title

def get_url(self,response,item):
    url = reponse.xpath("//div/li[@class='list_item']/a/@herf").extract()
    if url:
	item['url'] = url

def get_body(self,response,item):
    body = response.xpath("//div@[class='post_text' id='endText' style='border-top:1px solid #ddd;']/p/text()").extract()
    if body:
	item['body'] = body
