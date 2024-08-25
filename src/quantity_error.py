class IncorrectProductQuantityError(Exception):
    """Класс исключения при некорректном количестве товара."""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Невозможно добавить товар с нулевым количеством.'

    def __str__(self):
        return self.message
