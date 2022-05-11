import scrapy
from testScrapy.items import TestscrapyItem
from scrapy.linkextractors import LinkExtractor


class AmazonProductSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["www.amazon.com"]

    # start_urls = [
    #     "https://www.amazon.in/deal/48e4aec5?showVariations=true&pf_rd_r=KE2MFQXBFSMD3JK7JRJ3&pf_rd_p=78c9b567-1104-4e60-a4cc-720319b5249d&pd_rd_r=7886be7a-2aa6-4d41-ba79-c5369ddd5bbc&pd_rd_w=kUdQl&pd_rd_wg=JfOtU&ref_=pd_gw_unk"
    # ]
    start_urls = [
        "https://freshindiaorganics.com/products/organic-lychee?variant=32413762846805"
    ]
    le_product_details = LinkExtractor(restrict_css='//div[@class="product-image"]/a')

    def parse(self, response):
        items = TestscrapyItem()

        title = response.xpath('//h1[@class="product-title"]/span/text()').extract()
        items['product_title'] = ''.join(title)

        description = response.xpath('//div[@class="short-description"]/text()').extract()
        items['product_description'] = ''.join(description)

        price = response.xpath('//div[@class="prices"]/span/text()').extract()
        items['product_price'] = ''.join(price)



        # titles = response.xpath('//div[@class="a-section octopus-dlp-asin-title"]/a/text()').extract()
        # for title in titles:
        #     items['product_name'] = ''.join(title).strip()
        # sale_prices = response.xpath('//span[@class="a-price-whole"]/text()').extract()
        # for sale_price in sale_prices:
        #     items['product_sale_price'] = ''.join(sale_price).strip()
        # sale_currencies = response.xpath('//span[@class="a-price-symbol"]/text()').extract()
        # for sale_currency in sale_currencies:
        #     items['product_sale_currency'] = ''.join(sale_currency).strip()
        # original_prices = response.xpath(
        #     '//span[@class="a-size-mini a-color-tertiary octopus-widget-strike-through-price a-text-strike"]/text()').extract()
        # for original_price in original_prices:
        #     items['product_original_price'] = ''.join(original_price).strip()
        # brands = response.xpath('//span[@class="a-size-base a-color-base a-text-bold"]/text()').extract()
        # for brand in brands:
        #     items['product_brand'] = ''.join(brand).strip()
        # image_urls = response.xpath('//img[@class="octopus-dlp-asin-image octopus-softline-asin-image"] ').extract()
        # for image_url in image_urls:
        #     items['product_image_url'] = ''.join(image_url).strip()
        # discount_perts = response.xpath(
        #     '//span[@class="a-size-mini a-color-tertiary octopus-widget-price-saving-percentage"]/text()').extract()
        # for discount_pert in discount_perts:
        #     items['product_discount_pert'] = ''.join(discount_pert).strip()

        yield items
