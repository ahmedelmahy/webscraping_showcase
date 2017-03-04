import scrapy

   

blood_pages = [ 1332, 1412] #
cancer_pages = [ 1336, 1364 ]
DM_pages = [1392]
cvs_pages = [ 292, 308, 340, 348, 356, 364, 304, 324, 344, 352, 360, 368, 1376]
chest_pages = [ 376, 384, 400, 408, 380, 388, 404 ]
git_pages = [ 464, 528, 540, 568, 576, 584, 592, 532, 564, 572, 580, 588,
             480, 488, 496, 504, 512, 520, 484, 492, 500, 508, 516, 596 ,
             460]
liver_spleen_pages = [ 412 ]
nervous_system_pages = [ 842, 848, 856, 864, 880, 888, 896, 844, 852, 860, 876,
                  884, 892, 900, 904, 908 ]
head_pages = [ 12, 20, 16 ]
mouth_teeth_pages = [ 208 ]
eye_pages = [ 24 ]
ENT_pages = [ 100, 144, 180 ]                  
bone_pages = [ 620, 628, 636, 644, 652, 692, 700, 764, 624, 632, 640,
                  648, 676, 696, 704, 768, 784, 788 ]  
urinary_system_pages = [1508, 1544, 1552, 1588, 1548, 1584]
reproductive_sexual_pages = [ 1596 , 1604, 1648, 1664, 1672, 1680, 1668, 1676,
                             1688, 1712, 1684,
                             1708, 1752, 1780, 1600, 1620, 1652, 1716, 1768]
pediatric_pages = [2272, 2280, 2288, 2296, 2304, 2312, 2320, 2328, 2336, 
                   2344, 2352, 2372, 2380, 2276, 2284, 2292, 2300, 2308, 
                   2316, 2324, 2332, 2340, 2348, 2356, 2376, 2384]
weight_problem_pages = [ 2484, 2508, 2524, 2504, 2512]
nutrition_pages = [ 2460, 2468, 2476, 2464, 2472]
pysical_health_pages = [ 2528, 2540]
general_pages = [ 2572, 2580, 2588, 2596, 2620, 2628, 2636, 2576, 2584,
                 2592, 2600, 2624, 2632, 2640, 2544, 2648, 2684, 2712, 
                 2664, 2688, 2716]
muscular_pages = [ 796, 804, 812, 800, 808]
skin_pages = [ 932 , 1040, 1068, 1112, 1136, 1144, 1152, 1160, 1168, 1214,
               1220, 1240, 1248, 1256, 1264, 1276, 1284, 1292, 1300, 1308,
               1316, 1324, 964, 1064, 1072, 1132, 1140, 1148, 1156, 1164, 
               1184, 1216, 1224, 1244, 1252, 1260, 1272, 1280, 1288, 1296,
               1304, 1312, 1320]
endocrine_pages = [1464]
obsgyn_pages = [ 1812, 1820, 1828, 1836, 1844, 1852, 1860, 1868, 1816, 
                1824, 1832, 1840, 1848, 1856, 1864, 1892, 1900, 1896, 1904,
                1932, 1952, 1876, 1884, 1880, 1908, 1948 , 1956, 1984, 2216, 
                2080]
general_surgery_athetics_pages = [ 2388 ]

#---------------
category_pages = skin_pages
urls_links = []
for k in category_pages: 
    j = 0
    while j < 144:
        i = 7 * j
        url='http://consult.islamweb.net/consult/index.php?page=listing&pid='+str(k)+'&order=&startno='+str(i)
        j = j + 1
        urls_links.append(url)
    
class QuotesSpider(scrapy.Spider):
    name = "islamweb_link"

    def start_requests(self):
   
        for url in urls_links:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        
        for quote in response.css(".ItemTitle>h2>a"):      
             yield {'links':response.urljoin(quote.xpath('@href').extract_first())}
            
        for newurl in urls_links:
            next_page=str(newurl)
            yield scrapy.Request(next_page, callback=self.parse)    
                
    import scrapy

