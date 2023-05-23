from bs4 import BeautifulSoup
from requests import get

url = 'https://www.vuokraovi.com/vuokra-asunnot/turku?page=1&pageType=' # Переменная для ссылки
houses = []  # Создаем пустой список для хранения информации о домах
count = 1

# Запрос и парсинг страницы
while count <= 5:
    url = 'https://www.vuokraovi.com/vuokra-asunnot/turku?page=1&pageType=' + str(count) #Новые страницы, не работает в данном случае
    print(url) # Написание каждой url поотдельности
    response = get(url)  # Отправляем GET-запрос к указанному URL
    html_soup = BeautifulSoup(response.text, 'html.parser')  # Создаем объект BeautifulSoup для парсинга HTML

    # Поиск информации о домах на странице
    house_data = html_soup.find_all('div', class_="list-item-container")  # Ищем все элементы <div> с классом "list-item-container"
    if house_data != []: # Проверяет есть ли чтото в указаном обьекте
        houses.extend(house_data)  # Добавляем найденные данные о домах в список houses
    else:
        print('empty')
        break
    count += 1

print(len(houses))  # Выводим количество найденных домов
print(houses[0])  # Выводим информацию о первом доме
print()

n = int(len(houses)) - 1
count = 0

# Создание файла для записи данных
file_path = "news.txt"
file = open(file_path, "w", encoding="utf-8")

# Вывод информации о домах и запись в файл
while count <= 5:
    info = houses[int(count)]
    price = info.find('span', {"class": "price"}).text
    title = info.find('span', {"class": "capitalize"}).text
    print(title, ' ', price)
    # Запись данных в файл
    file.write(title + ' ' + price + '\n')
    count += 1

# Закрытие файла
file.close()
