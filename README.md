# webscraping_showcase
In this project, I showcase my ability to scrape the web using python. I scraped two popular websites in the Middle East: youm7.com and islamweb.com. Also I showcase other skills such as : working with CSS and Xpath identifiers; using regular expressions; gainig benefit from previous project such as using the datefinder library (works only in python3) to extract dates from text; working with HTML, json files and webservers; 

## youm7.com
Youm7 is a very popular news website in the Middle East. In the first file, I built a spider to follow articles on the website. In the file I used regular expressions and CSS identifiers.

## islamweb.com
Islamweb is another popular website that provides religious, social and medical advice and consulation. The spider I built was to get the medical consulations (that appear in the form of questions and answers) for using them in a health research project. The spider includes two file : the first (the linker) to find the links to the webpages that include the medical consulations; the second uses the json file the results from the first sub-spider to scrape the links in it.

## alexu.edu.eg
The third project was to scrape my school website. More specifically, This not a spider but the website provides students results by the seat number through PHP requests. The program aims to send requests with all possible ids and extract the final total result of each student from the html file recieved. 



## *Note ##
The first two spiders should be used within a scrapy framework. The [tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html) was very helpful to me .  The three projects bring out json files which I import into R to do the analysis. I will include the analysis codes in R in another git repository. 
