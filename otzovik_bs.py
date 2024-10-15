import requests  # pip install requests
import time
import random
import json
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml
# # Задайте путь к вашему файлу с прокси
# proxy_file_path = 'proxies.txt'
#
# # Считываем прокси из файла и сохраняем в список
# with open(proxy_file_path, 'r') as file:
#     proxies = file.read().splitlines()
#     print(proxies)
#
# # Выбираем случайный прокси
# random_proxy = random.choice(proxies)
# print(f'Используем прокси: {random_proxy}')
#
# # Настраиваем прокси для запроса
# proxies_dict = {
#     'http': f'http://{random_proxy}',
#     'https': f'http://{random_proxy}',


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


# session = requests.Session()
# session.headers.update(headers)

# Функция для получения случайного пользовательского агента
def get_random_user_agent():
    return random.choice(user_agents)


count = 1
while count <= 10:
    url = f'https://otzovik.com/reviews/nacionalniy_issledovatelskiy_institut_dopolnitelnogo_professionalnogo_obrazovaniya_russia_moscow/{count}/'
    headers = {'User-Agent': get_random_user_agent(),
               "Accept-Language": "en-US,en;q=0.9",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}
    # Выполняем запрос с использованием случайного прокси
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.text
        # Задержка от 1 до 5 секунд
        time.sleep(random.uniform(1, 5))
        block = BeautifulSoup(data, 'lxml')
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
            rating_div = i.find_next('div', class_='rating-score')

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
            get_text = requests.get(url_text, headers=headers)
            get_text.raise_for_status()  # Проверка на ошибки HTTP
            data = get_text.text
            # Задержка от 1 до 5 секунд
            time.sleep(random.uniform(1, 5))
            liss = BeautifulSoup(data, 'lxml')
            all_text = liss.find('div', {'class': 'review-body description'}).text.strip()
            print(all_text)

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
            with open(f'NIIDPO.json', 'w', encoding='utf-8') as json_file:
                json.dump(reviews_list, json_file, ensure_ascii=False, indent=4)

            print("Данные сохранены в reviews.json")

    except requests.exceptions.RequestException as e:
        print(f'Ошибка при выполнении запроса: {e}')
    count += 1
