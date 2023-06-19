# Асинхронный парсер PEP.

## Описание:
Парсер документов PEP на базе фреймворка Scrapy.
Выводит собранную информацию в два файла .csv:
* В первый файл парсится список всех PEP: номер, название и статус.
* Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество) и подсчитывает общее количество всех документов.

## **Как запустить проект**:

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:STI-xa/scrapy_parser_pep.git
```

* Cоздать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

* Запустить паука pep:
```
scrapy crawl pep
```
После завершения работы парсера в директории /results появятся файлы pep_{datetime}.csv и status_summary_{datetime}.csv.


## **Стэк технологий**:
* ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![image](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
* ![image](https://camo.githubusercontent.com/d2b9fadbbee82782eba05c3036fef87f222cd4dee9acd21e216b0a943d1c926b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5363726170792d322e352e312d626c61636b3f7374796c653d666c6174)
