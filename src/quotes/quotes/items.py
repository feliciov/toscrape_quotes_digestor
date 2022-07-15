import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def split_on_comma(value: str):
    return value.split(",")


class QuotesItem(scrapy.Item):
    quotation = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    author_link = scrapy.Field(
        output_processor=TakeFirst(),
    )
    keywords = scrapy.Field(
        input_processor=MapCompose(split_on_comma),
    )
