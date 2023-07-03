import requests
from bs4 import BeautifulSoup

def get_keyword_number(keyword):
    ##keyword="나루토"
    #url = "https://www.google.com/search?q={}".format(keyword)
    url = "https://www.google.com/search?q={}&hl=en".format(keyword)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    #res = requests.get(url)
    #print(type(res.text))

    soup = BeautifulSoup(res.text, 'lxml')
    #print(type(soup))

    number = soup.select_one('#result-stats')
    #print(number)
    #print(number.text)
    number = number.text

    #print(number[number.find('약'):number.rfind('개')])
    #print(number[number.find('약')+2:number.rfind('개')])
    #print(number[number.find('약')+2:number.rfind('개')].replace(',',''))

    #number = int(number[number.find('약')+2:number.rfind('개')].replace(',',''))
    number = int(number[number.find('About')+6:number.rfind('results')-1].replace(',',''))
    print(number)

    return(number)

if __name__ == "__main__":
    print(get_keyword_number("나루토"))