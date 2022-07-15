import scrapy
from scrapy.loader import ItemLoader

from quotes.items import QuotesItem


class QuotestoscrapeSpider(scrapy.Spider):
    name = "quotestoscrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # load quotes
        for quote in response.css("div.quote"):
            l = ItemLoader(item=QuotesItem(), selector=quote)

            l.add_css(
                "quotation",
                "span.text",
            )
            l.add_css(
                "author",
                "small.author",
            )
            l.add_css(
                "author_link",
                "small.author+a::attr(href)",
            )
            l.add_css(
                "keywords",
                "div.tags meta.keywords::attr('content')",
            )

            yield l.load_item()

        # pagination
        if next_url := response.css("ul.pager li.next a::attr('href')").get():
            yield scrapy.Request(
                response.urljoin(next_url),
                callback=self.parse,
            )
