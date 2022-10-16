salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = salary - spend
for i in range (2, months+1):
    spend *= 1+increase
    need_money += salary - spend

print(round(-need_money))
