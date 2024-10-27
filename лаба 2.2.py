salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for month in range(months):
    ost = salary - spend
    spend = spend * increase + spend
    money_capital = (ost * -1) + money_capital
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
