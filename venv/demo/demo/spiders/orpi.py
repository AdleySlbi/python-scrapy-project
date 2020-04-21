import scrapy

class Orpi(scrapy.Spider):
    name = "orpi"

    start_urls = ["https://www.orpi.com/"]
    # start_urls = ["https://www.orpi.com/recherche/buy?transaction=buy&resultUrl=&agency=&minSurface=&maxSurface=&newBuild=&oldBuild=&minPrice=&maxPrice=&sort=date-down&layoutType=mixte&nbBedrooms=&page=&minLotSurface=&maxLotSurface=&minStoryLocation=&maxStoryLocation="]

    def parse(self, response):
            self.logger.info('hello this is my first spider')
            # quotes = response.css('div.quote')
            # for quote in quotes:
            #     yield {
            #         'text': quote.css('.text::text').get(),
            #         'author': quote.css('.author::text').get(),
            #         'tags': quote.css('.tag::text').getall(),
            #     }