# XSS

Поле `feedback` уязвимо к XSS-атаке

### Пример успешного проведения атаки:

`feedback: <img onerror='alert("Успешная XSS-атака!");' src='invalid-image' />`
