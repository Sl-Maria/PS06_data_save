from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
parsed_data = []

url = "https://www.divan.ru/category/svet/"

# driver.get(url)
# time.sleep(3)
# lights = driver.find_elements(By.CLASS_NAME, 'wYUX2')

for i in range(1,7):
    page_url = url+f"page-{i}"
    driver.get(page_url)
    lights_page = driver.find_elements(By.CLASS_NAME, 'wYUX2')
    for light in lights_page:
        try:
            name = light.find_element(By.TAG_NAME, 'span').text
            price = light.find_element(By.TAG_NAME, 'meta').get_attribute('content')
            link = light.find_element(By.TAG_NAME, 'link').get_attribute('href')
            parsed_data.append([name, price, link])
        except:
            print("произошла ошибка при парсинге")
            continue
    time.sleep(3)

driver.quit()

for data in parsed_data:
    print(data)
print(f'Всего найдено {len(parsed_data)} светильников')

with open('svet.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
