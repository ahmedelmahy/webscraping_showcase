import scrapy
import json
import re
import datefinder

with open('/home/ahmed/Documents/myprojects/islamweb_scrapping/islamweb_links_skin.json') as json_data:
    djson = json.load(json_data)
urls=[]
for item in djson :
    urls.append(item['links'])


class QuotesSpider(scrapy.Spider):
    name = 'islamweb'
    def start_requests(self):
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
        
    def parse(self, response):
        q = response.css('.ItemContent>h5>font').extract()[0]
        a = response.css('.ItemContent>h5>font').extract()[1]
        date1 = response.css("#ContentCenter>table").extract_first()
        date2 = re.sub('[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]','', date1)
        regex_for_removing_english = re.compile('[a-zA-Z]')
        date3 = regex_for_removing_english.sub('', date2)
        date_matches = datefinder.find_dates(date3)
        for match in date_matches:
            final_date = str(match)
        

        
        viewerscss = response.css("#ContentCenter>p>font").extract_first()
        viewers = re.findall(ur'[\u0621][\u0629]:</font> (.*?) ',viewerscss, re.UNICODE)

        yield {'question': q,'answer': a, 'date': final_date, 'viewers': viewers}
            
           
        for newurl in urls:
            next_page=str(newurl)
            yield scrapy.Request(next_page, callback=self.parse)    
         