# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input("Введите количество секунд, которое хотите перевести: "))
res_hour = user_time // 3600
ost_sec = user_time % 3600
res_minute = ost_sec//60
res_second = ost_sec % 60
print(f"{res_hour}:{res_minute}:{res_second}")
