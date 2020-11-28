import scrapy
import json

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    start_urls = ['https://curiositystream.com/categories']

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en;q=0.9",
        "origin": "https://curiositystream.com",
        "referer": "https://curiositystream.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "x-4k-capable": "0",
        "x-api-version": "v3",
        "x-client-version": "v2.44.1-1-g807f97af9",
        "x-platform": "web",
        "x-session-token": "7c0470e5ac4a8e60e7316d28b91c1e9a45bbc6d9"
    }


    def parse(self, response):
        url = "https://api.curiositystream.com/v1/categories/"

        request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)

        yield request

    def parse_api(self, response):
        raw_data = response.body
        info_list = json.loads(raw_data)
        # print(info_list)
        # l = []
        for data in info_list:
            for cat in data['data']:
                for sub in cat['subcategories']:
                    d = {}
                    d['category'] = cat['name']
                    d['sub-category'] = sub['name']
                    d['img_url'] = sub['image_url']
                    # # l.append(d)
                    yield d
        
                    