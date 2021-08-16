from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = 'https://www.amazon.com/s?k=eminem+t+shirt&crid=3VVAYN88I00W&sprefix=T-shirt+emi%2Caps%2C342&ref=nb_sb_ss_ts-a-p_1_11'
ss = HTMLSession()
r = ss.get(url)
r.html.render(sleep = 1 , keep_page = True , timeout = False)
soup = BeautifulSoup(r.html.html , 'html.parser')
div = soup.find('div' , class_ = 's-main-slot s-result-list s-search-results sg-row')
divs = div.find_all('div' , class_ = 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20')
site_list = []
for d in divs :
    sites = d.find('a' , class_ = 'a-link-normal a-text-normal')['href']
    site = 'https://www.amazon.com'+sites
    site_list.append(site)
x = len(site_list)
for num in range(0 , x):
    
    r2 = ss.get(site_list[num])
    r2.html.render(sleep = 1 , timeout = False)
    name = r2.html.xpath('//*[@id="productTitle"]' , first = True).text,
    price = r2.html.xpath('//*[@id="priceblock_ourprice"]' , first = True)
    print('name : ' , name)
    if price == None :
        print('none')
        
    else:
        prix = price.text
        print('price: ' ,prix)
