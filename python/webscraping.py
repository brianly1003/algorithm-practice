import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # Make a request to the website you want to scrape
    URL = "https://xsmb.vn/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="Centre_BANGKQ_title")

    for result in results:
        if result.name == "h2":
            print(result.text)

    
