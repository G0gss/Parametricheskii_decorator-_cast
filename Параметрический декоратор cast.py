def cast(mtype): 
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            result = func(*args, **kwargs) 
            try:
                return mtype(result) 
            except ValueError:
                return result 
        return wrapper 
    return decorator

# Таким образом, `cast` - это высокоуровневый декоратор, который принимает тип и возвращает 
# низкоуровневый декоратор, который принимает функцию и возвращает обернутую в нее функцию.

# Пример использования
@cast(int)
def add(a, b):
    return a + b

print(add(2, 3))
print(add("2", "3"))
