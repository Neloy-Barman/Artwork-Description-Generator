import time
import base64
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

columns = ['ids', 'titles', 'descriptions']

artwork_details = []

def __main__():
    
    place = 'UnitedStates'
    id = "us"

    urls = pd.read_csv(f'csv_files/urls/{place}_urls.csv')['urls'].to_list()

    driver = webdriver.Chrome()
    x = 0
    for url in urls[:5]:
        x+= 1
        driver.get(url=url)

        # Title
        try:
            title = driver.find_element(by=By.XPATH, value="//span[@class='title f-headline-editorial o-article__inline-header-title']").get_attribute('textContent')
        except:
            print("Exception occured in the case of title!")
            title = ""
        
        # Description
        try:
            description_elements = driver.find_elements(by=By.XPATH, value="//div[@class='o-blocks']/p")
            description = ""
            for element in description_elements:
                description += element.text
        except:
            print("Exception Occured!!")
            description= ""
        
        img_src = driver.find_element(by=By.XPATH, value="//div[@class='m-article-header__img-container']/img").get_attribute('data-pin-media')
        image_data = requests.get(img_src).content

        with open(f'images/UnitedStates/{id}_{x}.jpg', "wb") as f:
            f.write(image_data)
        
        details = {
            'ids': f"{id}_{x}",
            'titles': title,
            'descriptions': description
        }

        # print(details)

        artwork_details.append(details)

        df = pd.DataFrame(data=artwork_details, columns=columns)
        
        df.to_csv("csv_files/details/UnitedSates.csv", index=False)


if __name__ == "__main__":
    __main__()