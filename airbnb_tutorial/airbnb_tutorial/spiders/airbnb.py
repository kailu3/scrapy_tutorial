# -*- coding: utf-8 -*-
import scrapy


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['http://www.airbnb.com/']

    def start_requests(self):
        url = ('https://www.airbnb.ca/api/v2/explore_tabs?_format=for_explore_search_web'
               '&_intents=p1&auto_ib=false&client_session_id=6c7f3e7b-c038-4d92-b2b0-0bc7c25f1054&currency=CAD'
               '&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true'
               '&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18'
               '&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en-CA&luxury_pre_launch=false&metadata_only=false'
               '&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&query=Canc%C3%BAn%2C%20Mexico&query_understanding_enabled=true'
               '&refinement_paths%5B%5D=%2Fhomes&s_tag=b7cT9Z3U&satori_version=1.1.9&screen_height=948&screen_size=medium'
               '&screen_width=1105&search_type=section_navigation&selected_tab_id=home_tab&show_groupings=true'
               '&supports_for_you_v3=true&timezone_offset=-240&version=1.5.7')

        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        _file = "first_page.json"
        with open(_file, 'wb') as f:
            f.write(response.body)

