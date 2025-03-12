from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAINS, NAME_PEP


class PepSpider(scrapy.Spider):
    name = NAME_PEP
    allowed_domains = DOMAINS
    start_urls = [f'https://{domain}/' for domain in DOMAINS]

    def parse(self, response):
        for link in response.css('tbody > tr > td > a::attr(href)').getall():
            yield response.follow(
                urljoin(response.url, link), callback=self.parse_pep
            )

    def parse_pep(self, response):
        pep_header = response.css('#pep-content > h1::text')
        yield PepParseItem({
            'number': pep_header.re_first(r'PEP (\d+)'),
            'name': pep_header.re_first(r'– (.+)'),
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text').get(),
        })
