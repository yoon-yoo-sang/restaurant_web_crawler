import scrapy
from scrapy.crawler import CrawlerProcess


class RestaurantWebCrawler(scrapy.Spider):
    name = "web_crawler"

    def start_requests(self):
        urls = [
            "https://map.naver.com/v5/search/%ED%95%A9%EC%A0%95%EC%97%AD%EB%A7%9B%EC%A7%91/place/34393996?c=14126196.9109348,4516040.3185648,13,0,0,0,dh&placePath=%3Fentry%253Dpll"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_httpbin)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))


if __name__ == '__main__':
    process = CrawlerProcess()
    crawler = process.create_crawler(RestaurantWebCrawler)
    process.crawl(crawler)
    process.start()
