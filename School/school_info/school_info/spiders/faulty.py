from __future__ import absolute_import
import scrapy
import datetime
import re
from school_info.items import *
import urlparse
from scrapy.http.request import Request
from bs4 import BeautifulSoup as BS

class FaultySpider(scrapy.Spider):
    name = "faulty"
    # def start_requests(self):
    base_url = 'http://www.colorado.edu/mechanical/our-people/faculty'
    start_urls = ['http://www.colorado.edu/mechanical/our-people/faculty']
    

    def parse(self, response):
        detail_url = 'http://www.colorado.edu'
        if response.url == self.base_url:
            name_split = self.get_fulty_names(response)
            # print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            print name_split
            name_split = list(set(name_split))
            for name in name_split:
                # name = name.split("/")[-2]
                print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                url = urlparse.urljoin(detail_url, name)
                # url = urlparse.urljoin(response.url, name)
                print url
                yield Request(url)
        else:    
            item = self.get_detail(response)
            yield item


    def get_fulty_names(self, response):
        # name_list = response.xpath('//div[contains(@class,"region region-content clearfix")]').xpath('//table[contains(@class,"people-list-table")]').xpath('//td[contains(@class,"person-table-name")]/strong/a/text()').extract()
        name_split = response.xpath('//div[contains(@class,"person-view-mode-grid")]/strong/a/@href').extract()
        return name_split

    def get_detail(self, response):
        item = FaultyItem()

        item['email'] = response.xpath('//a[contains(@href,"mailto")]/text()').extract_first()
    
            
        item['name'] = response.xpath('//h1[contains(@id,"page-title")]/text()').extract_first()
        
    
        item['phone'] = response.xpath('//div[contains(@class,"person-phone person-contact-info-item")]/text()').extract()

        # item['title'] = response.xpath('//div[contains(@class, "side-nav col-sm-3")]/p/b/text()').extract_first()
        item['link'] = response.url
        item['college'] = response.xpath('//div[contains(@id,"cu-footer")]/p/strong/a/text()').extract()
        item['profession'] = response.xpath('//h2[contains(@class,"block-title")]/a/text()').extract()
        # item['img'] = response.xpath('//img[contains(@alt,"Profile Photo")]/@src').extract_first()

        # item['background'] = self.fecth_background(response)

        # item['location'] = response.xpath('//div[contains(@class,"newThreeColCenter")]/p')[0].extract().replace("<br>", ",").replace("<p>","").replace("</p","")
        return item

    # def fetch_phone(self, response):
    #     match = re.search(r"Ph:[' ']*(.*)<br>Fax", response.body)
    #     if match:
    #         return re.search(r"Ph:[' ']*(.*)<br>Fax", response.body).group(1)
    #     else:
    #         return ''

    # def fecth_background(self, response):

    #     script = ''.join(response.xpath("//script").extract())
    #     match = re.search('tabNum == 1(.*)tabNum == 2', script)
    #     if match:    
    #         html = BS(match.group(0))
    #         li_list = html.findAll('li')
    #     else:
    #         return ""
    #     background = ''
    #     print li_list
    #     info = []
    #     if li_list:
    #         for li in li_list:
    #             info.append(li.text)
    #         return ','.join(info)
    #     else:
    #         return ""
