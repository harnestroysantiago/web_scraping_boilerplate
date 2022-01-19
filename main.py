from bs4 import BeautifulSoup as bs
import requests
import lxml


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"


def getdata(url):
    sauce = requests.get(url).text
    soup = bs(sauce, 'lxml')
    return soup


def getsingledata(url):
    data = getdata(url)
    listing = data.find(
        'div', {'class': 'col-sm-4 col-lg-4 col-md-4'}).find('div', {'class': 'caption'})
    listing_name = listing.find('a', {'class': 'title'}).text
    listing_price = listing.find('h4', {'class': 'pull-right price'}).text
    listing_desc = listing.find('p', {'class': 'description'}).text

    # print(f'\n{listing}\n')
    print(f'\nname: {listing_name}')
    print(f'price: {listing_price}')
    print(f'description: {listing_desc}\n')


getsingledata(url)
