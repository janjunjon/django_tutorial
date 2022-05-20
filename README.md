# OmniDatabank on Django

## Overview
* this is a web app, OmniDataBank, which includes `cm`, `gmail_app` and other apps.  

## Django Tutorial
1. `pip install django`  
2. `django-admin startproject mysite`  
3. `python3 manage.py startapp polls`  
4. `touch polls/urls.py`  

## Memo
* if you still doesn't install mysql, execute these commands.  
`sudo apt install mysql-server`  
`sudo mysql_secure_installation`  

* if you encount an error, `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'`, you execute these commands.  
`sudo service mysql restart`  
`sudo service mysql enable`  

* if you encount an error, `ERROR 1698 (28000): Access denied for user 'root'@'localhost'`, you execute these commands.  
`sudo mysql -u root -p`  
`ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`  

* if you use `mysql` and `django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.` is displayed, add these scripts for `root_DIR/app_name/__init__.py` 
`import pymysql`  
`pymysql.install_as_MySQLdb()`  

* run django webserver.  
`python3 manage.py runserver`  


