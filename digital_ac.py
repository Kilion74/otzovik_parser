import bs4
import time
import random
import json
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

# Список пользовательских агентов
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/113.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/112.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
    'Mozilla/5.0 (Linux; Android 11; Pixel 4 XL Build/RQ3A.210705.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Linux; Android 5.1; Nexus 5 Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'
]


# Функция для получения случайного пользовательского агента
def get_random_user_agent():
    return random.choice(user_agents)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(get_random_user_agent())
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                      options=chrome_options) as driver:  # Открываем хром
    driver.get("https://digital-academy.ru/reviews/mezhdunarodnaya-shkola-professij")  # Открываем страницу
    time.sleep(30)  # Время на прогрузку страницы
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    # btn = driver.find_element(By.XPATH, '//*[@id="pdopage"]/div[2]/div').click()
    # time.sleep(5)
    block = soup.find('div', {'id': 'comments'}).find_all('div', {'class': 'mt-8'})
    print(len(block))
    reviews_list = []  # Список для хранения отзывов
    for i in block:
        name = i.find('span', {'itemprop': 'name'}).text.strip()
        print(name)
        data = i.find('div', {'itemprop': 'datePublished'}).text.strip()
        print(data)
        good = i.find('div', {'class': 'ec-message__votes-item'}).text.strip()
        print(good)
        discription = i.find('div', {'itemprop': 'reviewBody'}).text.strip()
        print(discription)
        ocenra = i.find('div', {'class': 'course__stars leading-4'}).find_all('span', {'style': 'width: 100%;'})
        print(len(ocenra))
        ocenka = (len(ocenra))
        print('\n')

        # Создаем словарь для текущего отзыва
        review = {
            "name": name,
            "ocenka": ocenka,
            "data": data,
            "good": good,
            "discriptin": discription
        }

        # Добавляем отзыв в список
        reviews_list.append(review)

        # Запись в JSON-файл
        with open(f'Digital_mshp.json', 'w', encoding='utf-8') as json_file:
            json.dump(reviews_list, json_file, ensure_ascii=False, indent=4)

        print("Данные сохранены в reviews.json")
