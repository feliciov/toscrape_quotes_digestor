import scrapy


class QuotestoscrapeSpider(scrapy.Spider):
    name = 'quotestoscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
