money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

rest_money = money_capital - spend + salary
month = 1
while rest_money >= (spend * (1 + increase)):
    spend *= (1 + increase)
    rest_money += (salary - spend)
    month += 1

print(month)
