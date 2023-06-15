import scrapy

class LeetSpider(scrapy.Spider):
    name = "leet"
    allowed_domains = ["www.gamehouse.com"]
    start_urls = ["https://www.gamehouse.com/blog/leet-speak-cheat-sheet/"]

    def parse(self, response):
        for section in response.css(".letter.col-md-4"):
            letter = section.css("b::text").get().lower()
            leet_format_letter = section.xpath("./br/following-sibling::text()").getall()
            yield {
                "letter": [letter, leet_format_letter]
            }