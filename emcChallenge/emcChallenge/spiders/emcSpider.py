from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors import IGNORED_EXTENSIONS
import scrapy


class genericSpider(scrapy.Spider):
    name = "generic"
    data = None
    start_urls = []
    allowed_domains = []

    def parse(self, response):
        print(response.url)

        # Extract internal links from webpage
        IGNORED_EXTENSIONS.append('gz')
        IGNORED_EXTENSIONS.append('tar')
        urlextract = LinkExtractor(allow_domains=self.allowed_domains)

        # Store internal links
        links = urlextract.extract_links(response)
        links = [l.url for l in links]
        if response.url not in self.data:
            self.data[response.url] = links
        yield

        # Follow internal links
        for url in links:
            yield scrapy.Request(url, self.parse)
