# импортируем модуль
import requests
# отправляем запрос с заголовками по нужному адресу
req = requests.get("https://ya.ru", headers)
# считываем текст HTML-документа
src = req.text
print(src)


# ладно забей это не работает