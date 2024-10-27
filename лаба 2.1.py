money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
all_capital = salary+money_capital
month = 0
while spend < all_capital:
    all_capital -= spend
    month += 1
    spend = (spend * increase) + spend
    all_capital += salary
print("Количество месяцев, которое можно протянуть без долгов:", month)
