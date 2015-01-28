# -*- coding: utf-8 -*-
# import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from bug.items import BugItem

class bugSpider(CrawlSpider):
    name = "bug"
    allowed_domains = ["appinn.com"]
    start_urls = [
    "http://www.appinn.com/"
    ]
    rules = (
    	Rule(LinkExtractor(allow=r"page/\d+/"),callback='parse_bug',follow=True),
    )

    def parse_bug(self,response):
        sel = Selector(response)
        print '��URL��'+response.url
        post = sel.xpath('//div[@class="spost post"]/h2')
        items = []

        for p in post:
            item = BugItem()
            item['link'] = p.xpath('a/@href').extract()
            item['title'] = p.xpath('a/text()').extract()
            items.append(item)
        return items
    def parse_start_url(self,response):
        item = self.parse_bug(response)
        return item