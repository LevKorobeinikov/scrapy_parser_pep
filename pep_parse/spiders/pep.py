import scrapy

from urllib.parse import urljoin

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    DOMAINS, NUMBER_PEP, NAME_PEP, NAME, STATUS_PEP, URLS

)


class PepSpider(scrapy.Spider):
    name = NAME_PEP
    allowed_domains = DOMAINS
    start_urls = URLS

    def parse(self, response):
        for link in response.css('tbody > tr > td > a::attr(href)').getall():
            yield response.follow(
                urljoin(response.url, link), callback=self.parse_pep
            )

    def parse_pep(self, response):
        data = {
            NUMBER_PEP: response.css(
                '#pep-content > h1::text').re_first(r'PEP (\d+)'),
            NAME: response.css(
                '#pep-content > h1::text').re_first(r'– (.+)'),
            STATUS_PEP: response.css(
                'dt:contains("Status") + dd > abbr::text').get(),
        }
        yield PepParseItem(data)
