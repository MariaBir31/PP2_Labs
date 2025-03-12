import time  # Импортируем модуль для задержки

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Переводим миллисекунды в секунды
    return pow(number, 0.5)  # Вычисляем квадратный корень

num = int(input("Введите число: "))  
delay = int(input("Введите задержку (в мс): "))  

print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")









