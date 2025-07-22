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
src\__init__.py                  0      0   100%
src\category.py                 32      1    97%   31
src\new_product.py              14      0   100%
src\product.py                  40      1    98%   20
src\product_iterator.py         14      0   100%
tests\__init__.py                0      0   100%
tests\conftest.py               41      6    85%   58-62, 78, 101
tests\test_category.py          28      0   100%
tests\test_new_products.py      17      0   100%
tests\test_product.py           49      0   100%
----------------------------------------------------------
TOTAL                          235      8    97%

