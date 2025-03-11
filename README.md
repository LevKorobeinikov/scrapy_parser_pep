##Описание

Парсер на базе Scrapy предназначен для сбора данных документов (PEP)[https://www.python.org/]. Парсер cобирает номера, названия и статусы всех PEP и  сохраняет сводку (статус, количество).

## Техгологии

- **Python 3.9** 
- **Scrapy 2.5.1**

## Установка  

1. Клонирование репозитория:
    ```bash
    git clone git@github.com:LevKorobeinikov/scrapy_parser_pep.git
    cd scrapy_parser_pep
    ```

2. Создать и активировать виртуальное окружение:

    Для Windows:
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
    Для Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Обновить PIP:
    Для Windows:
    ```bash
    python -m pip install --upgrade pip
    ```
    Для Linux/macOS:
    ```bash
    python3 -m pip install --upgrade pip
    ```

4. Установка зависимостей:
    ```bach
    pip install -r requirements.txt
    ```

## Запуск

В активированном виртуальном окружении ввести команду в консоли:

 ```bach
    scrapy crawl pep
    ```

## Автор проекта - [Коробейников Лев Сергеевич](https://github.com/LevKorobeinikov)