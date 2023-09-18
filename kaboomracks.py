from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.item import Item
import scrapy
from pathlib import Path
import csv

class kaboomracks(scrapy.Spider):
    name = "kaboomracks"
    starting_urls = "file:///Users/evancole/Downloads/Telegram%20Desktop/ChatExport_2022-02-21/messages.html"

    def parse(self, response):
        text = response.xpath('//*[class="body"]')
        for listing in text:
            date = listing.xpath('.//*[class="pull_right date details"]//text()')
            #listing_text = listing.xpat('.//*[class="')
            yield{"date": date}
csv_path = Path.home() / "Documents" / "RunBitcoin" / "storage.csv"
storage = csv_path.open()
BOT_NAME = 'kaboomracks'
SPIDER_MODULES = ['kaboomracks.papa']
NEWSPIDER_MODULE = 'kaboomracks.papa'
ROBOTSTXT_OBEY = True
FEED_URI = "storage.csv"



with csv_path.open(mode = "w", encoding="utf-8", newline ="") as file:
    writer =  csv.DictWriter(file, fieldnames=["1", "2"])
    writer.writeheader()
    response.parse
