money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 1
rest_money = money_capital + salary - spend
while rest_money >= rest_money + salary - spend * (1 + increase):
    spend *= 1 + increase
    rest_money += salary - spend
    month += 1

print(month)
