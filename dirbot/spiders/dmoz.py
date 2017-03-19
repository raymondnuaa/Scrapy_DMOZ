# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from dirbot.items import WebsiteLoader

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        
        #hxs = Selector(response)
        #sites = hxs.select('//ul[@class="directory-url"]/li')
        sites = response.xpath("//div[@class='site-item ']")

        for site in sites:
            il = WebsiteLoader(response=response, selector=site)
            il.add_xpath('name', "div[@class='title-and-desc']/a/div/text()")
            il.add_xpath('url', "div[@class='title-and-desc']/a/@href")
            il.add_xpath('description', "div/div[@class='site-descr ']/text()")
            yield il.load_item()
        