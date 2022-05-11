import scrapy.spiders
from testScrapy.items import TestscrapyItem
from scrapy.selector import Selector


class MySpider(scrapy.spiders.Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath(response, "//h3[@class='result-heading']")
        items = []
        for title in titles:
            item = TestscrapyItem()
            item["title"] = title.select("a/text()").extract()
            item["link"] = title.select("a/@href").extract()
            # items.append(item)
            print("title: "+item["title"])
            print("link: "+item["link"])
        # return items
