from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from emcChallenge.spiders.emcSpider import genericSpider
from urllib.request import urlopen
from urllib import error

import tldextract
import json

if __name__ == "__main__":
    weburl = None
    depth = 0
    print("Type 'exit' to quit")
    while True:
        # Get Starting link
        inp = input("Enter URL you wish to crawl ('http://www.example.com'): ")
        if inp == "exit":
            exit(1)
        try:
            weburl = urlopen(inp)
        except (ValueError, error.HTTPError, error.URLError):
            print("Invalid URL address. Please enter again\n")
            continue
        break

    while True:
        # Get how deep the spider should go in the network
        depth = input("Enter how deep the spider should go: ")
        if depth == "exit":
            exit(1)
        try:
            depth = int(depth)
        except ValueError:
            print("Invalid Input")
            continue
        if depth <= 0:
            print("Invalid depth")
            continue
        break

    # Create Dictionary which stores visited website as key and internal links on page as the values
    visitedPages = {}

    # Change a few settings for crawler
    setting = Settings()
    setting.set("COOKIES_ENABLED", False)
    setting.set("LOG_LEVEL", 'INFO')
    setting.set("DEPTH_LIMIT", depth)

    # Determine the domain of starting website. Used to limit crawler
    extractUrl = tldextract.extract(weburl.geturl())
    domain = extractUrl.registered_domain

    # Initialize Crawler
    process = CrawlerProcess(setting)
    genericSpider.start_urls.append(weburl.geturl())
    genericSpider.allowed_domains.append(domain)
    genericSpider.data = visitedPages

    # Start Crawler
    process.crawl(genericSpider)
    process.start()
    process.stop()

    print("Spider crawl finish\n"
          "Writing results to JSON file")
    with open('CrawlerResults.json', 'w') as fp:
        json.dump(visitedPages, fp)
    print("Finished web crawler")
