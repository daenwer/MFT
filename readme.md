### Создать файл в MFT
private_settings.py

### Сборка проекта
`docker-compose -f docker-compose.dev.yml build`
### Запуск проекта
`docker-compose -f docker-compose.dev.yml up`

### Вход в контейнер
#### База данных
`docker exec -it mft_postgres bash`
#### Приложение
`docker exec -it mft_web bash`

### Запуск тестов внутри контейнера
`pytest credit_app/tests.py`

### Запуск линетров внутри контейнера
`black .`<br/>
`isort .`<br/>
`flake8`<br/>