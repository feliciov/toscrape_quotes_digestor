import scrapy


class QuotestoscrapeSpider(scrapy.Spider):
    name = 'quotestoscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "quotation": quote.css('span.text::text').get(),
                "author": quote.css("small.author::text").get(),
                "author_link":quote.css("small.author+a[href]").get(),
                "keywords":quote.css("div.tags").css("a::text").getall(),
            }
        if (next_url:= response.css("ul.pager li.next a::attr('href')").get()):
            yield scrapy.Request(
                response.urljoin(next_url),
                callback=self.parse,
            )
            