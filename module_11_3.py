def introspection_info(obj):

    # Тип объекта
    type_obj = type(obj)

    # Атрибуты объекта
    attribute_obj_list = [attribute_obj for attribute_obj in dir(obj) if not callable(getattr(obj, attribute_obj))]

    # Методы объекта
    method_obj_list = [method_obj for method_obj in dir(obj) if callable(getattr(obj, method_obj))]

    # Получение модуля, к которому принадлежит объект
    modul_obj = getattr(obj, '__module__', None)

    return {
            "type": type_obj.__name__,
            "attributes": attribute_obj_list,
            "methods": method_obj_list,
            "module": modul_obj
            }

# Примеры работы

# Целое число
number_info = introspection_info(42)
print(number_info)

# Строка
number_info = introspection_info('hhh')
print(number_info)

# Список
number_info = introspection_info([1, 2, 3])
print(number_info)
