# Реализация проекта автотестов на Selenuim + pytest с паттерном page-object-model

## Структура проекта:
1. Base - базовые сущности
2. Pages - директория со страницами
3. Locators - директория с локаторами
4. Tests - директория с тестами
5. Config - директория с конфигурациями
6. Data - директория с данными
7. Allure-results - директория для загрузки отчетов
8. Downloads - директория для скачивания
9. Screenshots - директория для скриншотов
10. conftest.py 
11. Dockerfile
12. docker-compose.yml
13. requirements.txt - файл с зависимостями 
14. .gitignore

## Требования:
1. Приложение Allure
2. JAVA 22
3. Python 3.12.3
4. Docker
5. Git

## Запуск проекта через docker-compose
1. Скачать проект с githab
2. Установить docker
3. В conftest.py раскомментировать headless режим
4. Запустить в терминале docker-compose up
5. После завершения создастся папка allure-results с отчетами о тестах
6. Для просмотра отчетов allure serve allure-results
7. Создание HTML документа allure generate allure-results

## Запуск проекта ручное:
1. Скачать проект с githab
2. Установить python
3. Установить allure
4. Установить зависимости pip3 install -r requirements.txt
5. Запустить тесты. pytest -v -s --alluredir allure-results
6. Просмотр отчета. allure serve allure-results
7. Создание HTML документа allure generate allure-results 

### Установка allure для windows через scoop 
В командной строка вводим: scoop install allure

### Установка scoop
1. Запускаем PowerShell от имени администратора
2. Set-ExecutionPolicy RemoteSigned -scope CurrentUser
3. iwr -useb get.scoop.sh | iex
https://scoop.sh/ - больше информации

### Установка allure для linux
1. wget https://github.com/allure-framework
2. sudo tar -zxvf allure-2.22.4.tgz -C /opt/
3. sudo ln -s /opt/allure-2.22.4/bin/allure /usr/bin/allure
   
### Установка JAVA
1. Скачать с сайта https://www.java.com/ru/download/
2. При установке выбрать пункт добавить переменную среды JAVA_HOME

### Установка Docker
Для windows скачать https://docs.docker.com/desktop/install/windows-install/

Для linux:
1. sudo apt update
2. sudo apt install default-jdk # Последняя версия
3. sudo apt install openjdk-22-jdk # 22-ая версия

### Установка Python
Для windows скачать https://www.python.org/downloads/

Для linux: sudo apt-get update && sudo apt-get install python3.12