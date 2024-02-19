import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options 


columns = ['ids', 'artists', 'mediums', 'titles', 'descriptions', 'urls']

artwork_details = []
failed_urls = []

def failed(url, place):
    failed_urls.append(url)
    data = {
        "failed_urls": failed_urls
    }

    df = pd.DataFrame(data=data)
    df.to_csv(f"csv_files/details/failed_urls_{place}.csv", index=False)

def __main__():
    
    # Remember to change these two.
    place = 'China'
    id = "ch"

    urls = pd.read_csv(f'csv_files/urls/{place}_urls.csv')['urls'].to_list()

    print(f"Artworks from this place: {place}\n\n")


    driver = webdriver.Chrome()
    x = 0
    for url in urls:
        saved = 0
        x += 1
        driver.get(url=url)

        # Title
        try:
            title = driver.find_element(by=By.XPATH, value="//span[@class='title f-headline-editorial o-article__inline-header-title']").get_attribute('textContent').replace("\n", "")
        except:
            print("Exception occured in title scraping!!")
            title = ""
        
        # Description
        try:
            description_elements = driver.find_elements(by=By.XPATH, value="//div[@class='o-blocks']/p")
            description = ""
            for element in description_elements:
                description += element.text
            description = description.replace("\n", "")
        except:
            print("Exception occured in description scraping!!")
            description= ""
        
        # Artist
        try:
            artist = driver.find_element(by=By.XPATH, value="//dd[@itemprop='creator']/span[@class='f-secondary']").text.replace("\n", "")
        except:
            print("Exception occured in artist scraping!!")
            artist = ""
        
        # Medium
        try:
            medium = driver.find_element(by=By.XPATH, value="//dd[@itemprop='material']/span[@class='f-secondary']").text.replace("\n", "")
        except:
            print("Exception occured in medium scraping!!")
            medium = ""
        
        # Image
        try:
            img_src = driver.find_element(by=By.XPATH, value="//div[@class='m-article-header__img-container']/img").get_attribute('data-pin-media')
            image_data = requests.get(img_src).content

            format_ = img_src.split(".")[-1]
            
            with open(f'images/{place}/{id}_{x}.{format_}', "wb") as f:
                f.write(image_data)
            saved = 1
        except:
            print('Error occured in Image')
    
     
        # If saved or not saved 
        if saved:
            details = {
                'ids': f"{id}_{x}",
                'titles': title,
                'descriptions': description,
                'artists': artist,
                'mediums': medium,
                'urls': url,
            }
            artwork_details.append(details)
            # print(artwork_details)
            df = pd.DataFrame(data=artwork_details, columns=columns)
            df.to_csv(f"csv_files/details/{place}.csv", index=False)
        else:
            failed(url=url, place=place)
            print('Details not saved........')
        
        time.sleep(1)
    
    driver.close()

if __name__ == "__main__":
    __main__()