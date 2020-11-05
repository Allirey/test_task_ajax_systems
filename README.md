# Test task "Test Results"

 Подготовка запуска проекта
 
 ```
git clone https://github.com/Allirey/test_task0411
cd test_task0411/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
 ```

### Запуск api
```
python3 main_api.py
```
При первом запуске создастся sqlite3 бд, и заполнится тестовыми данными

Создание записи http://127.0.0.1:5000/api_v1/test_result/ - POST (принимает json с полями "device_type" (str), "operator" (str), "success" (int) )

Удаление записи http://127.0.0.1:5000/api_v1/test_result/{record_id} - DELETE (record_id - идентификатор записи в бд)

Просмотр статистики http://127.0.0.1:5000/api_v1/stat/?operator={name} - GET (name - имя оператора)


### Запуск gui

```
python3 main_ui.py
```