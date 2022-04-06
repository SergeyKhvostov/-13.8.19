numbers_tickers = int(input("Введите колличество билетов :"))
ticket_price = 0
for i in range(numbers_tickers):
    age = int(input("Введите возраст:"))
    i += 1
    if age < 18:
        print("Бесплатно")
    elif 18 <= age < 25:
        ticket_price += 990
        print("Стоимость билета 990 руб.")
    else:
        ticket_price += 1390
        print("Стоимость билета 1390 руб.")
if numbers_tickers > 3:
        ticket_price = ticket_price * 0.9
        print("Стоимость билетов со скидкой:", ticket_price)
else:
        print("Всего к оплате:", ticket_price)