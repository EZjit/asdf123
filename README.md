# Asdf123
Простое приложение на стеке: Python, Flask, PostgreSQL, jQuery, gunicorn, Nginx

## Как развернуть локально

### Запуск вручную

#### Необходимые приложения
1) Прежде чем запускать приложение, убедитесь, что на вашей рабочей станции установлена ОС Linux, либо Linux дестрибутив запущен из-под виртуальной машины
2) Убедитесь, что у Вас установлена СУБД PostgreSQL:
```bash
pg_config --version
```
 Если, не установлена, ее необходимо установить:
https://www.postgresql.org/download/linux/ubuntu/

3) Убедитесь, что у Вас установлен сервер Nginx:
```bash
nginx -v
``` 
Если не установлен, установите:
https://nginx.org/en/docs/install.html

4) Убедитесь, что у Вас установлен Python:
```bash
python3 --version
```
Если не установлен, установите:
https://realpython.com/installing-python/#linux-how-to-build-python-from-source-code

5) Установите и/или обновите менеджер пакетов pip:
```bash
python -m ensurepip --upgrade
```

#### Устанавливаем и запускаем проект
1) Скопируйте проект из Github репозитория:
```bash
git clone https://github.com/EZjit/asdf123.git
```
2) Создайте и запустите виртуальное окружение:
```bash
python -m venv deployenv
source deployenv/bin/activate
```
3) Установите зависимости:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
4) Создайте и сконфигурируйте базу данных PostgreSQL:
```bash
sudo -u postgres psql

CREATE DATABASE flask_db;
CREATE USER flask_user WITH ENCRYPTED PASSWORD 'qwerty';
GRANT ALL PRIVILEGES ON DATABASE flask_db TO flask_user;
ALTER DATABASE flask_db OWNER TO flask_user;

\q
```
5) Скопируйте конфигурацию приложения в директорию с конфигами Nginx:
```bash
cd /<путь к проекту (локально)>
cp nginx/asdf123 /etc/nginx/sites-available
```
и создайте символьную ссылку на данный конфиг:
```bash
sudo ln -s /etc/nginx/sites-available/asdf123 /etc/nginx/sites-enabled
```
6) Перезапустите Nginx:
```bash
sudo systemctl restart nginx
```
и сконфигурируйте фаервол:
```bash
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
7) Запустите приложение:
```bash
gunicorn --config gunicorn-config.py wsgi:app
```
8) Приложение будет работать через Nginx локально на 80 порту: http://localhost:80. Также можно постучаться напрямую в gunicorn сервер через 8000 порт: http://localhost:8000
