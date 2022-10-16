money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0 # количество месяцев, которое можно прожить
while True:
    money_capital = money_capital + salary - spend
    spend = spend + spend * increase
    month += 1
    if money_capital < 0:
        break
if money_capital < 0:
    month -= 1
# TODO Оформить решение

print(month)
