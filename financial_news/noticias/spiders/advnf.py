# -*- coding: utf-8 -*-
import scrapy


class AdvnfSpider(scrapy.Spider):
    name = 'advnf'
    start_urls = ['https://br.advfn.com/jornal/acoes/balanco-trimestral/']

    def parse(self, response):
        articles = response.xpath('/html/body/div[4]/div[4]/div/div/div[1]/article')

        for article in articles:
            link = article.xpath('.')
            title = link.xpath('.//div/div/a/text()').extract_first()
            href = link.xpath('.//div/div/a/@href').extract_first()
            data = link.xpath('.//div/div/div[1]/time/text()').extract_first()
            image = link.xpath('.//div/a/img/@src').extract_first()
            yield{
                'title':title,
                'href':href,
                'data':data,
                'image':image,
            }
