import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["itjuzi.com"]

    start_urls = ["http://itjuzi.com/company/{}".format(n) for n in range(1700, 1800)] #get the range of company

    def parse(self, response):          #get informations about itjuzi
        item = DmozItem()
        website = response.css('.weblink').xpath('./@href').extract()[0]
        item['product'] = response.css('ul.bread').xpath('./li/a/text()')[2].extract()
        item['company'] = response.css(".des-more>div>span:nth-child(1)")[0].xpath('./text()').extract()
        item['location'] = response.css('.fa-map-marker')[0].xpath('../span/text()').extract()
        # item['website'] = website

        yield scrapy.Request(website, meta={'item': item}, callback=self.parse_item)
    def parse_item(self, response):                             #get informations about hire url
        url_list = response.xpath('//a/@href').extract()        #get all the urls in refer websites
        key_words = ['hire', 'career', 'careers', 'job', 'join', 'zhaopin']
        hire_urls = []
        for url in url_list:            #match keywords
            for key_word in key_words:
                if key_word in url:
                    hire_urls.append(url)

        item = response.meta['item']
        item['hire_urls'] = hire_urls
        yield item
