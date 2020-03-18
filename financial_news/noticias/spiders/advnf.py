# -*- coding: utf-8 -*-
import scrapy


class AdvnfSpider(scrapy.Spider):
    name = 'advnf'
    start_urls = ['http://http://br.advfn.com/jornal/acoes/balanco-trimestral/']

    def parse(self, response):
        pass
