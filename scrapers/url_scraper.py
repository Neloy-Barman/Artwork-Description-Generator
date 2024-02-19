import math
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


artstyle_places = [
    {
        "place": "United%20States",
        "results": 38523,
    },
    {
        "place": "France",
        "results": 15036,
    },
    {
        "place": "Japan",
        "results": 13432,
    },
    {
        "place": "England",
        "results": 8161,
    },
    {
        "place": "Italy",
        "results": 4850,
    },
    {
        "place": "Germany",
        "results": 4386,
    },
    {
        "place": "China",
        "results": 3959,
    },
    {
        "place": "Netherlands",
        "results": 2155,
    },
]

results_per_page = 50

art_details_urls = []
failed_urls = []


def failed_page_urls(url):
    failed_urls.append(url)
    data = {
        "failed_urls": failed_urls
    }

    df = pd.DataFrame(data=data)
    df.to_csv("csv_files/urls/failed_pages_urls.csv", index=False)

def __main__():
    base_url = "https://www.artic.edu/collection?" 
    
    for i in range(len(artstyle_places)-6, len(artstyle_places)-5):
        print(f"For place: {artstyle_places[i]['place']}__", end="")
        total_pages = math.ceil(artstyle_places[i]['results'] / results_per_page)
        print(f"Total pages: {total_pages}>>>>>>>>>>>>>>>>>>>>>>>>") 

        driver = webdriver.Chrome()

        for j in range(0, total_pages):
            page_no = j + 1
            place = f"place_ids={artstyle_places[i]['place']}"
            page = f"page={page_no}"

            url = base_url + place + "&" + page

            driver.get(url=url)

            time.sleep(2)

            url_elements = driver.find_elements(by=By.XPATH, value="//li[@class='m-listing m-listing--variable-height o-pinboard__item s-positioned']/a")

            urls = [element.get_attribute('href') for element in url_elements]
            print(f"Page No: {page_no}------------------------------------->")
            # print(f"These are the data: {urls}")

            if len(urls) == 0:
                failed_page_urls(url=url)
                print("Failed................")
                continue

            art_details_urls.extend(urls)

            data = {"urls": art_details_urls}

            df = pd.DataFrame(data=data)

            df.to_csv(f"csv_files/urls/{artstyle_places[i]['place'].replace('%20','')}_urls.csv", index=False)


        driver.close()

if __name__ == "__main__":
    __main__()