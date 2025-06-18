# Приложение на основе e-commerceAdd commentMore actions
## Установка:
1. Клонируйте репозиторий:
```
https://github.com/makaka322/E-commerce
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Основные модули, реализованные в проекте:
- Модуль product.py. В нем реализован класс, содержащий информацию о товарах
- Модуль category.py. В нем реализован класс, содержащий информацию об категориях товаров 
и списки товаров из модуля product.py

## Тестирование
Для проекта реализованы тесты на pytest. Запустить можно командой `pytest .`
Покрытие:
```
src\__init__.py              0      0   100%
src\category.py             12      0   100%
src\product.py              10      0   100%
tests\__init__.py            0      0   100%
tests\conftest.py           12      1    92%
tests\test_category.py       6      0   100%
tests\test_product.py        5      0   100%
--------------------------------------------
TOTAL                       45      1    98%
