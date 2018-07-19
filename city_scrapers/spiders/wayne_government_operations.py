# -*- coding: utf-8 -*-

# THIS SPIDER USES A MIXIN FOR SHARED FUNCTIONALITY.
# MIXINS ARE STORED IN /city-scrapers/city-scrapers/mixins
# YOU CAN OVERRIDE THE MIXIN HERE BY CREATING YOUR OWN DEFINITION.

from city_scrapers.spider import Spider
from city_scrapers.mixins.wayne_commission import Wayne_commission


class Wayne_government_operationsSpider(Wayne_commission, Spider):
    name = 'wayne_government_operations'
    agency_id = 'Wayne County Committe on Government Operations'
    start_urls = ['https://www.waynecounty.com/elected/commission/government-operations.aspx']
    meeting_name = 'Wayne County Committee on Government Operations'

    @staticmethod
    def _parse_description(response):
        """
        Event description taken from static text at top of page.
        """
        desc_xpath = '//h2[contains(text(), "Government Operations")]/following-sibling::div/section/p/text()'
        desc = response.xpath(desc_xpath).extract_first()
        return desc
