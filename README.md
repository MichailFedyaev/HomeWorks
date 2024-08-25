# `Banking operations widget`

Программа скрывает номер карты и счета, а также фильтрует и сортирует банковские счета по дате и оплате.

## Project dependencies:
- The program uses the version Python 3.12
- flake8 = "7.0.0"
- black = "24.4.2"
- isort = "5.13.2"
- mypy = "1.10.0"
- pytest = "^8.3.2"
- pytest-cov = "^5.0.0"

## Функции, классы которые мы будем использовать в этой версии кода:
- Класс Category который работает со списком товаров.
- Класс ProductIterator для итерации по товарам в категории.
- Класс Smartphone который работает с категорией "Смартфоны".
- Класс LawnGrass который работает с категорией "Трава газонная".
- Класс Order для представления заказа.
- Класс исключений QuantityError при не корректном выводе товара.
- Абстрактный класс OrderCategoryProperties для общих свойств классов Заказ и Категория.
- Абстрактный класс BaseProduct для представления продукта.
- Класс-миксин PrintMixin, который печатает в консоль информацию о инициализации экземпляров класса.
- Класс Product который работает с объектами класса продуктов
- Функция для преобразования json файла в список словарей.
- Функция для чтения файла и создания объекты классов.

## Структура проекта
Был добавлен pytest, для запуска тестов и проверки классов а также pytest-cov, для анализа покрытия кода тестами
Была добавлена папка (htmlcov) с отчетом покрытия тестами в формате HTML.
Тесты функционала с помощью pytest-cov:

---------- coverage: platform win32, python 3.12.1-final-0 ----------- 
Name                     Stmts   Miss  Cover
----------------------------------------------------
src\__init__.py                      0      0   100%
src\base_product.py                  7      1    86%
src\category.py                     48      1    98%
src\lawn_grass.py                   11      0   100%
src\order.py                        21      0   100%
src\order_category_property.py       8      1    88%
src\print_mixin.py                   5      0   100%
src\product.py                      37      1    97%
src\quantity_error.py                5      0   100%
src\smartphone.py                   12      0   100%
tests\__init__.py                    0      0   100%
tests\conftest.py                   64      0   100%
tests\test_category.py              48      0   100%
tests\test_lawn_grass.py            17      0   100%
tests\test_order.py                 27      0   100%
tests\test_print_mixin.py           13      0   100%
tests\test_product.py               55      0   100%
tests\test_smartphone.py            18      0   100%
----------------------------------------------------
TOTAL                              396      4    99%




# Инструкция по установке
Чтобы скачать репозиторий:

`git clone github.com/MichailFedyaev/HomeWorks.git`

Затем вам необходимо установить основные зависимости для запуска проекта в вашей системе:

```pip install -r requirements.txt```

## Контакт для обратной связи
За дополнительной информацией обращайтесь: `drovosekov1910@mail.ru`