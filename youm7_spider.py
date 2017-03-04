import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        #url = 'http://www.youm7.com/story/2016/10/28/%D8%A7%D9%84%D8%A7%D9%81%D8%AA%D8%A7%D8%A1-%D8%A7%D8%B7%D9%84%D8%A7%D9%82-%D8%B5%D8%A7%D8%B1%D9%88%D8%AE-%D8%B9%D9%84%D9%89-%D9%85%D9%83%D8%A9-%D8%B6%D8%B1%D8%A8-%D9%85%D9%86-%D8%A7%D9%84%D8%AC%D9%86%D9%88%D9%86-%D9%88%D8%A7%D8%B9%D8%AA%D8%AF%D8%A7%D8%A1-%D8%B9%D9%84%D9%89/2942607'
        #url='http://www.youm7.com/story/2016/10/29/%D8%A7%D9%84%D8%B3%D9%8A%D8%B3%D9%89-%D9%8A%D8%AE%D8%B5%D8%B5-100-%D9%85%D9%84%D9%8A%D9%88%D9%86-%D8%AC%D9%86%D9%8A%D9%87-%D9%84%D8%AA%D8%B9%D9%88%D9%8A%D8%B6-%D8%A3%D8%B3%D8%B1-%D8%B6%D8%AD%D8%A7%D9%8A%D8%A7-%D8%A7%D9%84%D8%B3%D9%8A%D9%88%D9%84/2943539'        
        url='http://www.youm7.com/story/2016/10/29/%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3-%D9%8A%D8%AE%D8%B5%D8%B5-50-%D9%85%D9%84%D9%8A%D9%88%D9%86-%D8%AC%D9%86%D9%8A%D9%87-%D9%84%D9%85%D8%AA%D8%B6%D8%B1%D8%B1%D9%89-%D8%A7%D9%84%D8%B3%D9%8A%D9%88%D9%84-%D9%8850-%D8%A3%D8%AE%D8%B1%D9%89-%D9%84%D8%A5%D8%B5%D9%84%D8%A7%D8%AD/2943499'        
        #url='http://www.youm7.com/Home/Search?allwords=%D8%A7%D9%84%D8%B3%D9%8A%D8%B3%D9%8A'
        #for url in urls:
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('.articleCont'):      
            h=quote.css('div::text').extract()
            #hh=[x.encode('utf-8') for x in h]

            yield {
                'text': h
                }
            l=quote.css('a').extract()
            l2=[ x for x in l if "story" in x ]
            l3=[ x for x in l2 if "img" not in x ]
            urls=[]
            for item in l3:
                o=re.findall(r'href=[\'"]?([^\'" >]+)', item)[0]
                o='http://www.youm7.com'+o    
                urls.append(o)
            
            #if next_page is not None:
                #next_page = response.urljoin(next_page)
            for newurl in urls:
                next_page=str(newurl)
                yield scrapy.Request(next_page, callback=self.parse)    
                
                #'links': quote.css('a').extract(),
                # type(quote.css('div::text').extract()[0])


    
#remove them the next time
'''
import json
import codecs

with open('/home/ahmed/tutorial/quotes.json', 'r') as f:
    data = json.load(f,)
    
    
output_file = codecs.open("/home/ahmed/tutorial/quotes.json", "r", encoding="utf-8")
j=json.load(output_file)
'''