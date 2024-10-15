import bs4
import time
import json
import random
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
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
print('Введите цифру соответствия катнгории: 1- Smart; 2 - Talentsy')
file_name = input()
gross = ''
storage = ''
if file_name == '1':
    gross = 'onlayn-institut_detskoy_psihologii_smart_child_russia_moscow'
    storage = 'Smart'
elif file_name == '2':
    gross = 'talentsy_ru-onlayn_obuchenie_tvorchestvu'
    storage = 'Talentsy'


count = 1
while count <= 8:
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(
            f"https://otzovik.com/reviews/{gross}/{count}/")  # Открываем страницу
        time.sleep(3)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        # category = soup.find('h1', {'class': 'product-name'}).text.strip()
        # print(category)
        block = soup.find_all('div', {'class': 'item status4 mshow0'})
        reviews_list = []  # Список для хранения отзывов
        for i in block:
            name = i.find_next('a', {'class': 'user-login'}).find('span').text.strip()
            print(name)
            photo = i.find_next('a', {'class': 'avatar'}).find('img')['src']
            print('https://otzovik.com' + photo)
            pixx = ('https://otzovik.com' + photo)
            reputaciya = i.find_next('div', {'class': 'karma-line'}).text.strip()
            print(reputaciya)
            try:
                address = i.find_next('div', {'class': 'karma-line'}).find('div').text.strip()
                print(address)
            except:
                print('None')
                address = 'None'
            rating_div = i.find('div', class_='rating-score')

            # Получение значения атрибута title
            title_value = rating_div['title']

            # Вывод результата
            print(title_value)
            data = i.find_next('div', {'class': 'review-postdate'}).find('span').text.strip()
            print(data)
            content = i.find_next('div', {'class': 'review-body-wrap'})
            # title = content.find('h3').text.strip()
            # print(title)
            # textet = content.find('div', {'class': 'review-teaser'}).text.strip()
            # print(textet)
            revue_plus = content.find('div', {'class': 'review-plus'}).text.strip()
            print(revue_plus)
            revue_minus = content.find('div', {'class': 'review-minus'}).text.strip()
            print(revue_minus)
            all_otziv = i.find_next('div', {'review-bar'}).find('a')['href']
            print('https://otzovik.com' + all_otziv)
            url_text = ('https://otzovik.com' + all_otziv)

            with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options) as driver:  # Открываем хром
                try:
                    driver.get(
                        url_text)  # Открываем страницу
                    time.sleep(3)  # Время на прогрузку страницы
                    get_text = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                    all_text = get_text.find('div', {'class': 'review-body description'}).text.strip()
                    print(all_text)
                except:
                    continue
            print('\n')

            # Создаем словарь для текущего отзыва
            review = {
                "name": name,
                "photo": pixx,
                "reputaciya": reputaciya,
                "address": address,
                "raiting": title_value,
                "data": data,
                "good": revue_plus,
                "bad": revue_minus,
                "all_text": all_text,
                "link": url_text
            }

            # Добавляем отзыв в список
            reviews_list.append(review)

            # Запись в JSON-файл
            with open(f'{storage}.json', 'w', encoding='utf-8') as json_file:
                json.dump(reviews_list, json_file, ensure_ascii=False, indent=4)

            print(f"Данные сохранены в {storage}.json")

    count = count + 1
    print('Page_number: ' + str(count))
